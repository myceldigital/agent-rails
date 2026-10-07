#!/usr/bin/env python3
"""Validate the minimal structure of .agent-rails/manifest.json."""

import json
import sys
from pathlib import Path

REQUIRED_RAIL = {
    "id",
    "scope",
    "invariant",
    "approved_path",
    "enforcement",
    "verification",
}


def error(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)


def main() -> None:
    if len(sys.argv) != 2:
        error("usage: check_manifest.py <manifest.json>")
        raise SystemExit(2)

    path = Path(sys.argv[1])
    try:
        data = json.loads(path.read_text())
    except Exception as exc:
        error(f"cannot read manifest JSON: {exc}")
        raise SystemExit(2)

    problems = []
    if data.get("version") != 1:
        problems.append("version must equal 1")

    rails = data.get("rails")
    if not isinstance(rails, list):
        problems.append("rails must be an array")
        rails = []

    seen = set()
    for index, rail in enumerate(rails):
        prefix = f"rails[{index}]"
        if not isinstance(rail, dict):
            problems.append(f"{prefix} must be an object")
            continue
        missing = sorted(REQUIRED_RAIL - set(rail))
        if missing:
            problems.append(f"{prefix} missing: {', '.join(missing)}")
        rail_id = rail.get("id")
        if not isinstance(rail_id, str) or not rail_id.strip():
            problems.append(f"{prefix}.id must be a non-empty string")
        elif rail_id in seen:
            problems.append(f"duplicate rail id: {rail_id}")
        else:
            seen.add(rail_id)
        scope = rail.get("scope")
        if scope is not None and (not isinstance(scope, list) or not all(isinstance(x, str) and x for x in scope)):
            problems.append(f"{prefix}.scope must be an array of non-empty strings")
        for key in ("enforcement", "verification"):
            value = rail.get(key)
            if value is not None and not isinstance(value, dict):
                problems.append(f"{prefix}.{key} must be an object")

    if problems:
        for problem in problems:
            error(problem)
        raise SystemExit(1)

    print(f"OK: {len(rails)} rail(s) validated")


if __name__ == "__main__":
    main()
