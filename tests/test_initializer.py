from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INIT_SCRIPT = ROOT / "init-agent-project.py"

CORE_DOCS = [
    "AGENTS.md",
    "CLAUDE.md",
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


def run(cmd: list[str], cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, cwd=cwd, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def test_initializes_core_files(tmp_path: Path) -> None:
    project = tmp_path / "demo-project"
    cp = run([sys.executable, str(INIT_SCRIPT), str(project), "--no-git-commit"])
    assert cp.returncode == 0, cp.stderr

    for rel in CORE_DOCS:
        assert (project / rel).exists(), rel

    assert (project / "scripts" / "check_progress_docs.py").exists()
    assert (project / ".claude" / "hooks" / "progress-gate.sh").exists()
    assert (project / ".git" / "hooks" / "pre-commit").exists()

    check = run([sys.executable, "scripts/check_progress_docs.py"], cwd=project)
    assert check.returncode == 0, check.stderr


def test_check_progress_docs_rejects_business_and_workflow_mix(tmp_path: Path) -> None:
    project = tmp_path / "mixed-scope"
    project.mkdir()
    if run(["git", "--version"]).returncode != 0:
        return
    assert run(["git", "init"], cwd=project).returncode == 0
    run(["git", "config", "user.email", "test@example.com"], cwd=project)
    run(["git", "config", "user.name", "Test User"], cwd=project)

    cp = run([sys.executable, str(INIT_SCRIPT), str(project)])
    assert cp.returncode == 0, cp.stderr

    (project / "src").mkdir(exist_ok=True)
    (project / "src" / "demo.py").write_text("print('demo')\n", encoding="utf-8")
    (project / "AGENTS.md").write_text((project / "AGENTS.md").read_text(encoding="utf-8") + "\nextra\n", encoding="utf-8")

    check = run([sys.executable, "scripts/check_progress_docs.py"], cwd=project)
    assert check.returncode != 0
    assert "protected workflow/policy" in check.stderr


def test_compile_release_and_run_standalone(tmp_path: Path) -> None:
    cp = run([sys.executable, "scripts/compile_release.py"], cwd=ROOT)
    assert cp.returncode == 0, cp.stderr
    dist_script = ROOT / "dist" / "init-agent-project.py"
    assert dist_script.exists()

    project = tmp_path / "standalone-demo"
    cp = run([sys.executable, str(dist_script), str(project), "--no-git-commit"])
    assert cp.returncode == 0, cp.stderr
    assert (project / "docs" / "agent" / "13_CHANGE_CONTROL.md").exists()


def test_readme_uses_windows_safe_paths() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    readme_zh = (ROOT / "README.zh-CN.md").read_text(encoding="utf-8")
    assert "C:/path/to/your/project" in readme
    assert "C:/path/to/your/project" in readme_zh
    assert "Git Bash" in readme
    assert "Git Bash" in readme_zh
