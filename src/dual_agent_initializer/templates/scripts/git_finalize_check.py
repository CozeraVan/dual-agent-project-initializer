#!/usr/bin/env python3
from __future__ import annotations

import re
import subprocess
import sys

SECRET_RE = re.compile(r"api[_-]?key|secret|token|password|passwd|BEGIN (RSA|OPENSSH|PRIVATE) KEY", re.I)


def run(cmd: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, text=True, capture_output=True)


def main() -> int:
    print("== Git Finalize Check ==")

    if run(["git", "rev-parse", "--is-inside-work-tree"]).returncode != 0:
        print("ERROR: Not inside a git repository.", file=sys.stderr)
        return 1

    print("\n== Current branch ==")
    print(run(["git", "branch", "--show-current"]).stdout.strip())

    print("\n== Git status ==")
    print(run(["git", "status", "--short"]).stdout, end="")

    print("\n== Changed files ==")
    print(run(["git", "diff", "--name-only", "HEAD"]).stdout, end="")

    print("\n== Progress docs check ==")
    cp = run([sys.executable, "scripts/check_progress_docs.py"])
    print(cp.stdout, end="")
    if cp.returncode != 0:
        print(cp.stderr, file=sys.stderr)
        return cp.returncode

    print("\n== Secret scan ==")
    diff = run(["git", "diff", "HEAD"]).stdout
    matches = [line for line in diff.splitlines() if SECRET_RE.search(line)]
    if matches:
        print("ERROR: Potential secret-like text found in git diff.", file=sys.stderr)
        for line in matches[:50]:
            print(line, file=sys.stderr)
        return 1
    print("No obvious secret-like text found in git diff.")

    print("\n== Remote ==")
    print(run(["git", "remote", "-v"]).stdout, end="")

    print("\nGit finalize check completed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
