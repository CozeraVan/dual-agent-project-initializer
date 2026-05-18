#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
import stat
import subprocess
import sys
from datetime import datetime
from pathlib import Path

TEMPLATE_DIR = Path(__file__).resolve().parent / "templates"

EXECUTABLE_PATHS = {
    "scripts/check_progress_docs.py",
    "scripts/git_finalize_check.py",
    "scripts/agent_status.py",
    "scripts/check-progress-docs.sh",
    "scripts/git-finalize-check.sh",
    "scripts/agent-status.sh",
    ".claude/hooks/progress-gate.sh",
    "_git/hooks/pre-commit",
    ".git/hooks/pre-commit",
}

CORE_DOCS = [
    "CLAUDE.md",
    "AGENTS.md",
    "docs/agent/00_PRODUCT_VISION.md",
    "docs/agent/01_CURRENT_STATUS.md",
    "docs/agent/02_LOCKED_REQUIREMENTS.md",
    "docs/agent/03_ROADMAP.md",
    "docs/agent/04_TASK_HANDOFF.md",
    "docs/agent/05_PROGRESS.md",
    "docs/agent/06_DECISION_LOG.md",
    "docs/agent/07_RECOVERY_PROTOCOL.md",
    "docs/agent/08_IMPLEMENTATION_BRIEF.md",
    "docs/agent/09_CODING_HANDOFF.md",
    "docs/agent/10_REVIEW_REPORT.md",
    "docs/agent/11_AGENT_STATE.md",
    "docs/agent/12_AGENT_BOARD.md",
    "docs/agent/13_CHANGE_CONTROL.md",
]

GIT_HOOK_TEMPLATE = "_git/hooks/pre-commit"
GIT_HOOK_TARGET = ".git/hooks/pre-commit"


def configure_stdio() -> None:
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")


def run(cmd: list[str], cwd: Path, check: bool = False) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, cwd=str(cwd), text=True, capture_output=True, check=check)


def git_available() -> bool:
    return shutil.which("git") is not None


def is_git_repository(project: Path) -> bool:
    if not git_available():
        return False
    return run(["git", "rev-parse", "--is-inside-work-tree"], project).returncode == 0


def backup_if_exists(project: Path, rel: str, backup_root: Path) -> None:
    target = project / rel
    if target.exists() or target.is_symlink():
        dst = backup_root / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        if target.is_dir() and not target.is_symlink():
            if dst.exists():
                shutil.rmtree(dst)
            shutil.copytree(target, dst)
        else:
            shutil.copy2(target, dst)


def render(content: str, project: Path) -> str:
    return content.replace("{{PROJECT_NAME}}", project.name).replace("{PROJECT_NAME}", project.name)


def set_executable_if_needed(target: Path, rel: str) -> None:
    if rel in EXECUTABLE_PATHS:
        try:
            mode = target.stat().st_mode
            target.chmod(mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
        except OSError:
            pass


def write_file(project: Path, rel: str, content: str, backup_root: Path, overwrite_readme: bool = False) -> None:
    target = project / rel
    if rel == "README.md" and target.exists() and not overwrite_readme:
        return
    backup_if_exists(project, rel, backup_root)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(render(content, project), encoding="utf-8", newline="\n")
    set_executable_if_needed(target, rel)


def iter_templates() -> list[tuple[str, str]]:
    if not TEMPLATE_DIR.exists():
        raise FileNotFoundError(f"Template directory not found: {TEMPLATE_DIR}")
    items: list[tuple[str, str]] = []
    for p in sorted(TEMPLATE_DIR.rglob("*")):
        if p.is_file():
            rel = p.relative_to(TEMPLATE_DIR).as_posix()
            items.append((rel, p.read_text(encoding="utf-8")))
    return items


def ensure_git(project: Path, backup_root: Path, hook_content: str | None, no_commit: bool) -> None:
    if not git_available():
        print("WARNING: git not found. Files were created, but git initialization was skipped.")
        return

    if not is_git_repository(project):
        cp = run(["git", "init"], project)
        if cp.returncode != 0:
            print("WARNING: git init failed. Git hook and initial commit were skipped.")
            if cp.stderr.strip():
                print(cp.stderr.strip())
            return

    if hook_content is not None:
        write_file(project, GIT_HOOK_TARGET, hook_content, backup_root, overwrite_readme=True)

    # Git hooks are intentionally not added; .git is not versioned.
    add_targets = [
        ".editorconfig",
        ".gitattributes",
        ".gitignore",
        "CLAUDE.md",
        "AGENTS.md",
        "README.md",
        "docs/agent",
        ".claude",
        ".agents",
        ".codex",
        "scripts",
    ]
    run(["git", "add", *add_targets], project)

    if no_commit:
        return

    cp = run(["git", "commit", "-m", "chore: initialize dual-agent workflow"], project)
    if cp.returncode != 0:
        print("Initial commit skipped or failed. This is usually fine if user.name/user.email is not configured or there are no changes.")
        if cp.stderr.strip():
            print(cp.stderr.strip())


def initialize(project: Path, no_git_commit: bool = False, overwrite_readme: bool = False) -> Path:
    project = project.expanduser().resolve()
    project.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    backup_root = project / ".agent-backups" / timestamp

    print(f"Initializing dual-agent workflow for: {project.name}")
    print(f"Project directory: {project}")

    hook_content: str | None = None
    for rel, content in iter_templates():
        if rel == GIT_HOOK_TEMPLATE:
            hook_content = content
            continue
        write_file(project, rel, content, backup_root, overwrite_readme=overwrite_readme)

    for rel in [
        "docs/agent/change_requests",
        ".claude/skills",
        ".agents/skills",
        ".claude/hooks",
        ".codex",
        "scripts",
    ]:
        (project / rel).mkdir(parents=True, exist_ok=True)

    ensure_git(project, backup_root, hook_content, no_git_commit)

    print("\nDual-agent workflow initialized.")
    print("\nCreated/updated core files:")
    for rel in CORE_DOCS:
        print(f"- {rel}")

    print("\nShort prompts:")
    print("Claude Code: 请读取 11 和 12，执行当前 Claude Code 任务。")
    print("Codex: 请读取 11 和 12，执行 One-Shot Review-Finalize-Next。")
    print("New idea: 请读取 11 和 12，把以下新 idea 作为 Change Request 分析，不改代码。")
    print("Architecture change: 请进入 Architecture Change Mode，读取 11、12、13，对以下架构变更做影响分析，不改业务代码。")

    print("\nNext recommended prompt for Codex:")
    print("请先不要修改业务代码。请读取 AGENTS.md、11、12、13，和我进行项目 brainstorm，初始化项目目标、架构、todo list，并准备第一份 Implementation Brief。")

    print("\nBackups for overwritten files, if any:")
    print(backup_root)
    return project


def main(argv: list[str] | None = None) -> int:
    configure_stdio()

    parser = argparse.ArgumentParser(description="Initialize a reusable dual-agent project workflow.")
    parser.add_argument("project_dir", nargs="?", default=".", help="Project directory. Defaults to current directory.")
    parser.add_argument("--no-git-commit", action="store_true", help="Initialize files and git hook, but do not create initial commit.")
    parser.add_argument("--overwrite-readme", action="store_true", help="Overwrite README.md if it already exists. Default preserves it.")
    args = parser.parse_args(argv)

    try:
        initialize(Path(args.project_dir), no_git_commit=args.no_git_commit, overwrite_readme=args.overwrite_readme)
        return 0
    except Exception as exc:  # pragma: no cover - defensive CLI reporting
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
