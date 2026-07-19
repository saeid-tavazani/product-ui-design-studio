#!/usr/bin/env python3
"""Validate a Product UI Design Studio design profile against the bundled schema."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


DEFAULT_SCHEMA = Path(__file__).resolve().parents[1] / "assets" / "design-profile.schema.json"
DEFAULT_PROFILE = Path("design-system") / "design-profile.json"


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise SystemExit(f"File not found: {path}")
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON in {path}: line {exc.lineno}, column {exc.colno}: {exc.msg}")


def format_path(parts: tuple[Any, ...]) -> str:
    if not parts:
        return "$"
    rendered = "$"
    for part in parts:
        if isinstance(part, int):
            rendered += f"[{part}]"
        else:
            rendered += f".{part}"
    return rendered


class SimpleValidationError:
    def __init__(self, path: tuple[Any, ...], message: str, validator: str) -> None:
        self.path = path
        self.message = message
        self.validator = validator


def resolve_ref(schema: dict[str, Any], ref: str) -> dict[str, Any]:
    if not ref.startswith("#/"):
        raise ValueError(f"Only local refs are supported by fallback validator: {ref}")
    current: Any = schema
    for part in ref[2:].split("/"):
        current = current[part]
    return current


def json_type(value: Any) -> str:
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "boolean"
    if isinstance(value, int) and not isinstance(value, bool):
        return "integer"
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return "number"
    if isinstance(value, str):
        return "string"
    if isinstance(value, list):
        return "array"
    if isinstance(value, dict):
        return "object"
    return "unknown"


def fallback_iter_errors(value: Any, subschema: dict[str, Any], root: dict[str, Any], path: tuple[Any, ...] = ()) -> list[SimpleValidationError]:
    import re

    errors: list[SimpleValidationError] = []
    if "$ref" in subschema:
        return fallback_iter_errors(value, resolve_ref(root, subschema["$ref"]), root, path)

    if "const" in subschema and value != subschema["const"]:
        errors.append(SimpleValidationError(path, f"{value!r} does not equal {subschema['const']!r}", "const"))

    if "enum" in subschema and value not in subschema["enum"]:
        errors.append(SimpleValidationError(path, f"{value!r} is not one of {subschema['enum']}", "enum"))

    expected = subschema.get("type")
    if expected:
        expected_types = expected if isinstance(expected, list) else [expected]
        actual = json_type(value)
        if actual not in expected_types and not (actual == "integer" and "number" in expected_types):
            errors.append(SimpleValidationError(path, f"{actual!r} is not of type {expected!r}", "type"))
            return errors

    if isinstance(value, dict):
        required = subschema.get("required", [])
        for key in required:
            if key not in value:
                errors.append(SimpleValidationError(path, f"{key!r} is a required property", "required"))

        properties = subschema.get("properties", {})
        if subschema.get("additionalProperties") is False:
            for key in value:
                if key not in properties:
                    errors.append(SimpleValidationError(path + (key,), "Additional properties are not allowed", "additionalProperties"))

        for key, child_schema in properties.items():
            if key in value:
                errors.extend(fallback_iter_errors(value[key], child_schema, root, path + (key,)))

    if isinstance(value, list):
        if "minItems" in subschema and len(value) < subschema["minItems"]:
            errors.append(SimpleValidationError(path, f"{value!r} is too short", "minItems"))
        if subschema.get("uniqueItems"):
            seen = set()
            for item in value:
                marker = json.dumps(item, sort_keys=True, ensure_ascii=False)
                if marker in seen:
                    errors.append(SimpleValidationError(path, "Array items are not unique", "uniqueItems"))
                    break
                seen.add(marker)
        if "items" in subschema:
            for index, item in enumerate(value):
                errors.extend(fallback_iter_errors(item, subschema["items"], root, path + (index,)))

    if isinstance(value, str):
        if "minLength" in subschema and len(value) < subschema["minLength"]:
            errors.append(SimpleValidationError(path, f"{value!r} is too short", "minLength"))
        if "pattern" in subschema and not re.search(subschema["pattern"], value):
            errors.append(SimpleValidationError(path, f"{value!r} does not match {subschema['pattern']!r}", "pattern"))

    if isinstance(value, (int, float)) and not isinstance(value, bool):
        if "minimum" in subschema and value < subschema["minimum"]:
            errors.append(SimpleValidationError(path, f"{value!r} is less than the minimum of {subschema['minimum']}", "minimum"))
        if "maximum" in subschema and value > subschema["maximum"]:
            errors.append(SimpleValidationError(path, f"{value!r} is greater than the maximum of {subschema['maximum']}", "maximum"))

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "profile",
        nargs="?",
        type=Path,
        default=DEFAULT_PROFILE,
        help="Profile JSON file. Defaults to design-system/design-profile.json.",
    )
    parser.add_argument(
        "--schema",
        type=Path,
        default=DEFAULT_SCHEMA,
        help="Schema JSON file. Defaults to assets/design-profile.schema.json.",
    )
    parser.add_argument("--format", choices=("text", "json"), default="text")
    args = parser.parse_args()

    schema = load_json(args.schema)
    profile = load_json(args.profile)

    try:
        from jsonschema import Draft202012Validator

        validator = Draft202012Validator(schema)
        errors = sorted(validator.iter_errors(profile), key=lambda item: tuple(item.path))
    except ImportError:
        errors = sorted(fallback_iter_errors(profile, schema, schema), key=lambda item: tuple(item.path))

    if args.format == "json":
        print(
            json.dumps(
                {
                    "profile": str(args.profile),
                    "schema": str(args.schema),
                    "valid": not errors,
                    "errors": [
                        {
                            "path": format_path(tuple(error.path)),
                            "message": error.message,
                            "validator": error.validator,
                        }
                        for error in errors
                    ],
                },
                indent=2,
                ensure_ascii=False,
            )
        )
    elif errors:
        print(f"Design profile is invalid: {args.profile}")
        for error in errors:
            print(f"- {format_path(tuple(error.path))}: {error.message}")
    else:
        print(f"Design profile is valid: {args.profile}")

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
