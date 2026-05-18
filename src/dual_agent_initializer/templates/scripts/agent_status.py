#!/usr/bin/env python3
from __future__ import annotations

import subprocess
from pathlib import Path


def run(cmd: list[str]) -> str:
    return subprocess.run(cmd, text=True, capture_output=True).stdout


print("== Agent State ==")
p = Path("docs/agent/11_AGENT_STATE.md")
if p.exists():
    lines = p.read_text(encoding="utf-8", errors="replace").splitlines()
    print("\n".join(lines[:160]))
else:
    print("docs/agent/11_AGENT_STATE.md not found.")

print("\n== Agent Board ==")
p = Path("docs/agent/12_AGENT_BOARD.md")
if p.exists():
    lines = p.read_text(encoding="utf-8", errors="replace").splitlines()
    print("\n".join(lines[:120]))
else:
    print("docs/agent/12_AGENT_BOARD.md not found.")

print("\n== Git Status ==")
if subprocess.run(["git", "rev-parse", "--is-inside-work-tree"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0:
    print(run(["git", "status", "--short"]), end="")
    print("\n== Last commits ==")
    print(run(["git", "log", "--oneline", "-5"]), end="")
else:
    print("Not a git repository.")
