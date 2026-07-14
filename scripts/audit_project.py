#!/usr/bin/env python3
"""Static preflight for Product UI Design Studio HTML/Tailwind prototypes.

This catches common structural, accessibility, theme, framework-leakage, and React-readiness risks.
It does not prove WCAG conformance and does not replace browser, keyboard, or
screen-reader testing.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from dataclasses import asdict, dataclass
from html.parser import HTMLParser
from pathlib import Path
from typing import Iterable

PROHIBITED_EXTENSIONS = {".jsx", ".tsx", ".vue", ".svelte"}
PROHIBITED_TERMS = (
    "from 'react'",
    'from "react"',
    "next/link",
    "next/image",
    "createRoot(",
    "ReactDOM",
    "createApp(",
)
RAW_COLOR_RE = re.compile(r"(?:#[0-9a-fA-F]{3,8}\b|(?:rgb|hsl|oklch|lab|lch)\()")
HREF_RE = re.compile(r'href=["\']([^"\']+)["\']', re.IGNORECASE)
HTML_TAG_RE = re.compile(r"<html\b([^>]*)>", re.IGNORECASE)
INLINE_EVENT_RE = re.compile(r"\son(?:click|change|submit|input|keydown|keyup|keypress|focus|blur|load|error)\s*=", re.IGNORECASE)
CLASS_QUERY_RE = re.compile(r"(?:querySelector(?:All)?\s*\(\s*[\'\"]\.|getElementsByClassName\s*\()", re.IGNORECASE)
INNER_HTML_RE = re.compile(r"\.innerHTML\s*=", re.IGNORECASE)
CLASS_LIST_STATE_RE = re.compile(r"\.classList\.(?:add|remove|toggle|replace)\s*\(", re.IGNORECASE)
CLASS_OR_STYLE_RE = re.compile(r'(?:style=["\'][^"\']*|class=["\'][^"\']*)', re.IGNORECASE)

SEVERITY_ORDER = {"blocker": 0, "critical": 1, "major": 2, "minor": 3, "cosmetic": 4}


@dataclass(frozen=True)
class Finding:
    severity: str
    code: str
    message: str
    file: str | None = None


class PageParser(HTMLParser):
    """Collect only the static signals useful to this preflight."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: list[str] = []
        self.label_for: set[str] = set()
        self.controls: list[tuple[str, dict[str, str], bool]] = []
        self.links: list[dict[str, str]] = []
        self.images: list[dict[str, str]] = []
        self.iframes: list[dict[str, str]] = []
        self.buttons: list[dict[str, object]] = []
        self.dialogs: list[dict[str, str]] = []
        self.headings: Counter[str] = Counter()
        self.has_main = False
        self.has_nav = False
        self.has_skip_link = False
        self.has_viewport = False
        self.label_depth = 0
        self.form_depth = 0
        self.button_stack: list[dict[str, object]] = []
        self.title_depth = 0
        self.svg_stack: list[dict[str, object]] = []
        self.svgs: list[dict[str, object]] = []
        self.nonsemantic_clickables: list[str] = []
        self.component_names: list[str] = []

    @staticmethod
    def attrs_dict(attrs: list[tuple[str, str | None]]) -> dict[str, str]:
        return {key.lower(): (value or "") for key, value in attrs}

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        a = self.attrs_dict(attrs)

        if a.get("id"):
            self.ids.append(a["id"])
        if a.get("data-component"):
            self.component_names.append(a["data-component"])
        if tag == "label":
            self.label_depth += 1
            if a.get("for"):
                self.label_for.add(a["for"])
        if tag == "form":
            self.form_depth += 1
        if tag in {"input", "select", "textarea"}:
            self.controls.append((tag, a, self.label_depth > 0))
        if tag == "a":
            self.links.append(a)
            href = a.get("href", "")
            classes = a.get("class", "")
            if href.startswith("#") and ("skip" in classes.lower() or "main" in href.lower()):
                self.has_skip_link = True
        if tag == "img":
            self.images.append(a)
        if tag == "iframe":
            self.iframes.append(a)
        if tag == "button":
            item: dict[str, object] = {"attrs": a, "text": [], "in_form": self.form_depth > 0}
            self.button_stack.append(item)
        if tag == "dialog":
            self.dialogs.append(a)
        if tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self.headings[tag] += 1
        if tag == "main":
            self.has_main = True
        if tag == "nav":
            self.has_nav = True
        if tag == "meta" and a.get("name", "").lower() == "viewport":
            self.has_viewport = True
        if tag in {"div", "span", "p"} and ("onclick" in a or a.get("role") == "button"):
            self.nonsemantic_clickables.append(tag)
        if tag == "svg":
            item = {"attrs": a, "has_title": False}
            self.svg_stack.append(item)
        elif tag == "title" and self.svg_stack:
            self.svg_stack[-1]["has_title"] = True
            self.title_depth += 1

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.handle_starttag(tag, attrs)
        if tag.lower() == "label":
            self.label_depth = max(0, self.label_depth - 1)

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag == "label":
            self.label_depth = max(0, self.label_depth - 1)
        if tag == "form":
            self.form_depth = max(0, self.form_depth - 1)
        if tag == "button" and self.button_stack:
            self.buttons.append(self.button_stack.pop())
        if tag == "title" and self.title_depth:
            self.title_depth -= 1
        if tag == "svg" and self.svg_stack:
            self.svgs.append(self.svg_stack.pop())

    def handle_data(self, data: str) -> None:
        if self.button_stack:
            self.button_stack[-1]["text"].append(data)


def rel(path: Path, root: Path) -> str:
    return str(path.relative_to(root)).replace("\\", "/")


def add(findings: list[Finding], severity: str, code: str, message: str, file: str | None = None) -> None:
    findings.append(Finding(severity, code, message, file))


def has_accessible_name(attrs: dict[str, str], text: str = "") -> bool:
    return bool(text.strip() or attrs.get("aria-label", "").strip() or attrs.get("aria-labelledby", "").strip() or attrs.get("title", "").strip())


def audit_html(path: Path, root: Path, findings: list[Finding]) -> None:
    text = path.read_text(encoding="utf-8", errors="replace")
    location = rel(path, root)
    lower = text.lower()

    for term in PROHIBITED_TERMS:
        if term.lower() in lower:
            add(findings, "critical", "framework-reference", f"Prohibited framework reference: {term}", location)

    if "<!doctype html" not in lower:
        add(findings, "minor", "doctype", "Missing HTML doctype", location)

    html_match = HTML_TAG_RE.search(text)
    if not html_match:
        add(findings, "critical", "html-root", "Missing <html> element", location)
    else:
        attrs = html_match.group(1).lower()
        if "lang=" not in attrs:
            add(findings, "major", "html-lang", "Missing lang attribute", location)
        if "dir=" not in attrs:
            add(findings, "minor", "html-dir", "Missing dir attribute", location)

    parser = PageParser()
    try:
        parser.feed(text)
    except Exception as exc:  # HTMLParser is forgiving; keep a guarded fallback.
        add(findings, "major", "html-parse", f"Could not fully parse HTML: {exc}", location)

    if not parser.has_viewport:
        add(findings, "major", "viewport", "Missing responsive viewport meta tag", location)
    if not parser.has_main:
        add(findings, "major", "main-landmark", "Missing <main> landmark", location)
    if parser.has_nav and not parser.has_skip_link:
        add(findings, "minor", "skip-link", "Navigation exists but no clear skip-to-content link was found", location)
    if parser.headings["h1"] == 0:
        add(findings, "major", "h1", "No <h1> found", location)
    elif parser.headings["h1"] > 1:
        add(findings, "minor", "multiple-h1", f"Multiple <h1> elements found ({parser.headings['h1']})", location)

    duplicate_ids = sorted(key for key, count in Counter(parser.ids).items() if count > 1)
    for identifier in duplicate_ids:
        add(findings, "critical", "duplicate-id", f"Duplicate id: {identifier}", location)

    for image in parser.images:
        if "alt" not in image:
            add(findings, "critical", "img-alt", "Image missing alt attribute", location)

    for frame in parser.iframes:
        if not frame.get("title", "").strip():
            add(findings, "critical", "iframe-title", "Iframe missing title", location)

    for tag, attrs, nested_in_label in parser.controls:
        if tag == "input" and attrs.get("type", "text").lower() == "hidden":
            continue
        identifier = attrs.get("id", "")
        named = nested_in_label or (identifier and identifier in parser.label_for) or has_accessible_name(attrs)
        if not named:
            control_type = attrs.get("type", tag)
            add(findings, "critical", "form-label", f"Unlabelled form control: {control_type}", location)

    for button in parser.buttons:
        attrs = button["attrs"]  # type: ignore[assignment]
        text_content = "".join(button["text"])  # type: ignore[arg-type]
        if not has_accessible_name(attrs, text_content):
            add(findings, "critical", "button-name", "Button has no accessible name", location)
        if button["in_form"] and not attrs.get("type"):
            add(findings, "minor", "button-type", "Button inside form has no explicit type", location)

    for link in parser.links:
        href = link.get("href", "").strip()
        if href in {"#", "javascript:void(0)", "javascript:;", ""}:
            add(findings, "major", "placeholder-link", f"Placeholder or empty link: {href or '[empty]'}", location)
            continue
        if link.get("target") == "_blank":
            rel_tokens = set(link.get("rel", "").lower().split())
            if "noopener" not in rel_tokens:
                add(findings, "major", "blank-rel", "target=_blank link missing rel=noopener", location)
        if href.startswith(("http://", "https://", "mailto:", "tel:", "#", "data:")):
            continue
        target = href.split("#", 1)[0].split("?", 1)[0]
        if not target:
            continue
        resolved = (path.parent / target).resolve()
        try:
            resolved.relative_to(root.resolve())
        except ValueError:
            add(findings, "minor", "link-root", f"Link escapes project root: {href}", location)
            continue
        if not resolved.exists():
            add(findings, "critical", "broken-link", f"Broken relative link: {href}", location)

    for attrs in parser.dialogs:
        if not attrs.get("aria-label") and not attrs.get("aria-labelledby"):
            add(findings, "major", "dialog-name", "Dialog has no accessible name", location)

    for svg in parser.svgs:
        attrs = svg["attrs"]  # type: ignore[assignment]
        decorative = attrs.get("aria-hidden", "").lower() == "true"
        named = svg["has_title"] or attrs.get("aria-label") or attrs.get("aria-labelledby")
        if not decorative and not named:
            add(findings, "minor", "svg-name", "SVG is neither named nor marked aria-hidden", location)

    for tag in parser.nonsemantic_clickables:
        add(findings, "major", "nonsemantic-control", f"Interactive {tag} detected; prefer button or link", location)

    for match in re.finditer(r'tabindex=["\']([1-9]\d*)["\']', text, re.IGNORECASE):
        add(findings, "major", "positive-tabindex", f"Positive tabindex found: {match.group(1)}", location)

    if INLINE_EVENT_RE.search(text):
        add(findings, "major", "inline-event", "Inline JavaScript event attribute found; use a focused module and data-action hook", location)

    if len(text) > 3500 and not parser.component_names:
        add(findings, "minor", "component-boundaries", "Substantial page has no data-component boundaries for reusable units", location)

    for component_name in parser.component_names:
        if not re.fullmatch(r"[A-Z][A-Za-z0-9]*", component_name):
            add(findings, "minor", "component-name", f"data-component should use a stable PascalCase name: {component_name}", location)

    for style_match in CLASS_OR_STYLE_RE.finditer(text):
        fragment = style_match.group(0)
        if RAW_COLOR_RE.search(fragment):
            add(findings, "minor", "raw-color", f"Raw color in HTML attributes: {fragment[:110]}", location)



def audit_javascript(path: Path, root: Path, findings: list[Finding]) -> None:
    text = path.read_text(encoding="utf-8", errors="replace")
    location = rel(path, root)
    lower = text.lower()

    for term in PROHIBITED_TERMS:
        if term.lower() in lower:
            add(findings, "critical", "framework-reference", f"Prohibited framework reference: {term}", location)

    if CLASS_QUERY_RE.search(text):
        add(findings, "major", "class-selector-hook", "Behavior selects elements by CSS class; use stable data-action/data-controller hooks", location)
    if INNER_HTML_RE.search(text):
        add(findings, "major", "innerhtml-render", "innerHTML assignment found; avoid injecting complete components or business markup", location)
    if CLASS_LIST_STATE_RE.search(text):
        add(findings, "minor", "class-state-mutation", "State appears to be expressed through classList; prefer data-state plus accurate aria state", location)
    if len(text.splitlines()) > 500:
        add(findings, "minor", "large-js-module", "Large JavaScript module; split DOM controllers, services, and mock state", location)


def audit(root: Path) -> list[Finding]:
    findings: list[Finding] = []
    html_files = sorted(root.rglob("*.html"))
    js_files = sorted(root.rglob("*.js"))

    if not html_files:
        add(findings, "blocker", "no-html", "No HTML files found")

    for path in root.rglob("*"):
        if path.is_file() and path.suffix.lower() in PROHIBITED_EXTENSIONS:
            add(findings, "critical", "framework-file", f"Prohibited framework file: {rel(path, root)}")

    for path in html_files:
        audit_html(path, root, findings)

    for path in js_files:
        audit_javascript(path, root, findings)

    required_handoff = (
        "design-system/component-map.json",
        "docs/component-inventory.md",
        "docs/route-map.md",
        "docs/react-handoff.md",
    )
    for relative in required_handoff:
        if not (root / relative).exists():
            add(findings, "major", "react-handoff", f"React-readiness handoff artifact missing: {relative}")

    theme_candidates = list(root.rglob("theme.css"))
    if not theme_candidates:
        add(findings, "critical", "theme-file", "theme.css not found")
    else:
        theme_text = "\n".join(p.read_text(encoding="utf-8", errors="replace") for p in theme_candidates)
        for token in ("--primary", "--background", "--foreground", "--border", "--focus"):
            if token not in theme_text:
                add(findings, "major", "theme-token", f"Semantic token missing from theme CSS: {token}")
        if "prefers-reduced-motion" not in theme_text:
            add(findings, "critical", "reduced-motion", "Reduced-motion handling missing from theme CSS")
        if ":focus-visible" not in theme_text:
            add(findings, "critical", "focus-visible", "Global visible focus handling missing from theme CSS")

    return sorted(findings, key=lambda item: (SEVERITY_ORDER[item.severity], item.file or "", item.code))


def counts(findings: Iterable[Finding]) -> dict[str, int]:
    result = {key: 0 for key in SEVERITY_ORDER}
    for item in findings:
        result[item.severity] += 1
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("project", type=Path)
    parser.add_argument("--format", choices=("text", "json"), default="text")
    parser.add_argument("--output", type=Path, help="Optional report file")
    args = parser.parse_args()
    root = args.project.resolve()

    if not root.exists() or not root.is_dir():
        print(f"Project directory not found: {root}", file=sys.stderr)
        return 2

    findings = audit(root)
    summary = counts(findings)

    if args.format == "json":
        rendered = json.dumps(
            {"project": str(root), "summary": summary, "findings": [asdict(item) for item in findings]},
            ensure_ascii=False,
            indent=2,
        ) + "\n"
    else:
        lines = []
        for item in findings:
            location = f" [{item.file}]" if item.file else ""
            lines.append(f"{item.severity.upper():8} {item.code}{location}: {item.message}")
        lines.append("")
        lines.append("Audit complete: " + ", ".join(f"{value} {key}" for key, value in summary.items()))
        lines.append("Static preflight only; manual browser and assistive-technology checks are still required.")
        rendered = "\n".join(lines) + "\n"

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")

    return 1 if summary["blocker"] or summary["critical"] else 0


if __name__ == "__main__":
    sys.exit(main())
