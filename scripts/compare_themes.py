#!/usr/bin/env python3
"""Compare two Theme Fingerprints for suspicious similarity.

This does not measure visual quality. It only flags matching theme dimensions
that may indicate a new project reused a previous visual system without
product-specific rationale.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

DIMENSIONS = [
    "designArchetype",
    "paletteModel",
    "typographyModel",
    "geometryModel",
    "spacingModel",
    "surfaceModel",
    "borderModel",
    "elevationModel",
    "layoutModel",
    "navigationModel",
    "imageryModel",
    "iconographyModel",
    "motionModel",
    "densityModel",
    "signatureElement",
]


def normalize(value: Any) -> str:
    return " ".join(str(value or "").lower().strip().split())


def load_profile(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"Profile is not a JSON object: {path}")
    return data


def fingerprint(profile: dict[str, Any]) -> dict[str, Any]:
    visual_system = profile.get("visualSystem")
    if not isinstance(visual_system, dict):
        return {}
    fp = visual_system.get("themeFingerprint")
    return fp if isinstance(fp, dict) else {}


def similarity_intent(profile: dict[str, Any]) -> bool:
    visual_system = profile.get("visualSystem")
    if not isinstance(visual_system, dict):
        return False
    intent = visual_system.get("similarityIntent")
    return isinstance(intent, dict) and intent.get("intentional") is True


def compare(previous: dict[str, Any], current: dict[str, Any]) -> tuple[list[str], list[str]]:
    previous_fp = fingerprint(previous)
    current_fp = fingerprint(current)
    matching: list[str] = []
    missing: list[str] = []

    for dimension in DIMENSIONS:
        previous_value = normalize(previous_fp.get(dimension))
        current_value = normalize(current_fp.get(dimension))
        if not previous_value or not current_value:
            missing.append(dimension)
        elif previous_value == current_value:
            matching.append(dimension)

    return matching, missing


def render(previous_path: Path, current_path: Path, matching: list[str], missing: list[str], intentional: bool) -> str:
    lines = [
        f"Compared Theme Fingerprints:",
        f"- Previous: {previous_path}",
        f"- Current: {current_path}",
        "",
        "This tool does not measure visual quality. It only identifies suspicious similarity.",
        "",
    ]

    if intentional:
        lines.append("Intentional similarity is documented in the current profile.")
    elif len(matching) >= 9:
        lines.append(f"Similarity warning: {len(matching)} of {len(DIMENSIONS)} theme dimensions match the previous project.")
        lines.append("Review whether the new direction is sufficiently product-specific.")
    else:
        lines.append(f"No high-similarity warning: {len(matching)} of {len(DIMENSIONS)} theme dimensions match.")

    if matching:
        lines.append("")
        lines.append("Matching dimensions:")
        lines.extend(f"- {item}" for item in matching)

    if missing:
        lines.append("")
        lines.append("Missing or incomplete dimensions:")
        lines.extend(f"- {item}" for item in missing)

    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("previous_profile", type=Path)
    parser.add_argument("current_profile", type=Path)
    parser.add_argument("--format", choices=("text", "json"), default="text")
    args = parser.parse_args()

    try:
        previous = load_profile(args.previous_profile)
        current = load_profile(args.current_profile)
    except Exception as exc:
        print(f"Could not read profiles: {exc}", file=sys.stderr)
        return 2

    matching, missing = compare(previous, current)
    intentional = similarity_intent(current)

    if args.format == "json":
        print(
            json.dumps(
                {
                    "previous": str(args.previous_profile),
                    "current": str(args.current_profile),
                    "matchingDimensions": matching,
                    "missingDimensions": missing,
                    "matchingCount": len(matching),
                    "dimensionCount": len(DIMENSIONS),
                    "intentionalSimilarity": intentional,
                    "warning": (len(matching) >= 9 and not intentional),
                    "qualityClaim": "none",
                },
                indent=2,
            )
        )
    else:
        print(render(args.previous_profile, args.current_profile, matching, missing, intentional), end="")

    return 1 if len(matching) >= 9 and not intentional else 0


if __name__ == "__main__":
    sys.exit(main())

