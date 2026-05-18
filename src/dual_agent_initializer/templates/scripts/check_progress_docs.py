#!/usr/bin/env python3
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path.cwd()

CODE_PATTERNS = re.compile(
    r"^(src/|app/|components/|screens/|services/|lib/|api/|server/|backend/|packages/|tests/|__tests__/|ios/|android/|"
    r"package\.json|package-lock\.json|pnpm-lock\.yaml|yarn\.lock|tsconfig\.json|babel\.config\.js|metro\.config\.js|app\.json|"
    r"pyproject\.toml|requirements\.txt|poetry\.lock|Cargo\.toml|go\.mod|Dockerfile|docker-compose\.ya?ml)"
)

PROGRESS_DOC_PATTERNS = re.compile(
    r"^docs/agent/(03_ROADMAP|04_TASK_HANDOFF|05_PROGRESS|06_DECISION_LOG|08_IMPLEMENTATION_BRIEF|09_CODING_HANDOFF|10_REVIEW_REPORT|11_AGENT_STATE|12_AGENT_BOARD|13_CHANGE_CONTROL)\.md$"
)

PROTECTED_WORKFLOW_PATTERNS = re.compile(
    r"^(AGENTS\.md|CLAUDE\.md|docs/agent/02_LOCKED_REQUIREMENTS\.md|docs/agent/13_CHANGE_CONTROL\.md|"
    r"\.claude/skills/|\.agents/skills/|\.claude/hooks/|scripts/check_progress_docs\.py|scripts/git_finalize_check\.py|scripts/agent_status\.py|"
    r"init-agent-project.*|init_agent_project.*)"
)


def run(cmd: list[str], check: bool = False) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, text=True, capture_output=True, check=check)


def inside_git() -> bool:
    return run(["git", "rev-parse", "--is-inside-work-tree"]).returncode == 0


def has_head() -> bool:
    return run(["git", "rev-parse", "--verify", "HEAD"]).returncode == 0


def changed_files() -> list[str]:
    if has_head():
        cp = run(["git", "diff", "--name-only", "HEAD"])
        names = cp.stdout.splitlines()
        cp2 = run(["git", "ls-files", "--others", "--exclude-standard"])
        names += cp2.stdout.splitlines()
        return sorted(set(n for n in names if n))
    cp = run(["git", "ls-files", "--others", "--exclude-standard"])
    return sorted(set(n for n in cp.stdout.splitlines() if n))


def diff_summary() -> str:
    if not has_head():
        return ""
    return run(["git", "diff", "--summary", "HEAD"]).stdout


def allow_workflow_file_changes() -> bool:
    p = Path("docs/agent/08_IMPLEMENTATION_BRIEF.md")
    if not p.exists():
        return False
    text = p.read_text(encoding="utf-8", errors="replace")
    return re.search(r"^ALLOW_WORKFLOW_FILE_CHANGES:\s*true\s*$", text, re.MULTILINE) is not None


def main() -> int:
    if not inside_git():
        return 0

    files = changed_files()
    if not files:
        print("No uncommitted changes.")
        return 0

    code_changed = [f for f in files if CODE_PATTERNS.search(f)]
    progress_changed = [f for f in files if PROGRESS_DOC_PATTERNS.search(f)]
    protected_changed = [f for f in files if PROTECTED_WORKFLOW_PATTERNS.search(f)]

    errors: list[str] = []

    if code_changed and not progress_changed:
        errors.append(
            "Code/config changed, but progress or handoff docs were not updated. "
            "Update at least one of docs/agent/04,05,08,09,10,11,12,13 as appropriate."
        )

    if code_changed and protected_changed and not allow_workflow_file_changes():
        errors.append(
            "Business code/config changes are mixed with protected workflow/policy file changes. "
            "Use a dedicated workflow/meta task with ALLOW_WORKFLOW_FILE_CHANGES: true, or separate the commits.\n"
            + "Protected changed files:\n- " + "\n- ".join(protected_changed)
        )

    summary = diff_summary()
    bad_modes = []
    for line in summary.splitlines():
        if "mode change" in line and ".md" in line and "100755" in line:
            bad_modes.append(line.strip())
    if bad_modes:
        errors.append("Markdown files should not become executable:\n- " + "\n- ".join(bad_modes))

    if errors:
        print("ERROR: Agent workflow checks failed.\n", file=sys.stderr)
        for err in errors:
            print(err, file=sys.stderr)
            print(file=sys.stderr)
        return 1

    print("Progress docs check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
