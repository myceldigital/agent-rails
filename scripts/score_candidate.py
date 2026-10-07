#!/usr/bin/env python3
"""Score an Agent Rails candidate from a JSON file."""

import json
import sys
from pathlib import Path

WEIGHTS = {
    "decisions_removed": 25,
    "bad_paths_eliminated": 20,
    "simplicity": 15,
    "discoverability": 10,
    "enforcement_strength": 10,
    "verification_quality": 10,
    "migration_safety": 5,
    "escape_hatch_quality": 5,
}


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(2)


def main() -> None:
    if len(sys.argv) != 2:
        fail("usage: score_candidate.py <candidate.json>")

    path = Path(sys.argv[1])
    try:
        data = json.loads(path.read_text())
    except Exception as exc:
        fail(f"cannot read candidate JSON: {exc}")

    scores = data.get("scores")
    if not isinstance(scores, dict):
        fail("candidate JSON must contain an object named 'scores'")

    missing = [key for key in WEIGHTS if key not in scores]
    extra = [key for key in scores if key not in WEIGHTS]
    if missing:
        fail("missing score(s): " + ", ".join(missing))
    if extra:
        fail("unknown score(s): " + ", ".join(extra))

    total = 0.0
    for key, weight in WEIGHTS.items():
        value = scores[key]
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            fail(f"{key} must be numeric")
        if value < 0 or value > 5:
            fail(f"{key} must be between 0 and 5")
        total += (value / 5.0) * weight

    result = {
        "name": data.get("name", path.stem),
        "score": round(total, 1),
        "out_of": 100,
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
