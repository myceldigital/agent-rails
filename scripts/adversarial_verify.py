#!/usr/bin/env python3
"""Verify that one command passes and an intentional bypass command fails."""

import argparse
import subprocess
import sys


def run(label: str, command: str) -> int:
    print(f"[{label}] {command}")
    completed = subprocess.run(command, shell=True)
    print(f"[{label}] exit={completed.returncode}")
    return completed.returncode


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pass-cmd", required=True, help="command expected to exit 0")
    parser.add_argument("--fail-cmd", required=True, help="intentional bypass command expected to exit non-zero")
    args = parser.parse_args()

    pass_code = run("positive", args.pass_cmd)
    fail_code = run("adversarial", args.fail_cmd)

    problems = []
    if pass_code != 0:
        problems.append("positive command did not pass")
    if fail_code == 0:
        problems.append("adversarial command did not fail")

    if problems:
        for problem in problems:
            print(f"ERROR: {problem}", file=sys.stderr)
        raise SystemExit(1)

    print("OK: approved path passed and bypass failed")


if __name__ == "__main__":
    main()
