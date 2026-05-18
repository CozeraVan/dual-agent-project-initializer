#!/usr/bin/env sh
PROJECT_DIR="${CLAUDE_PROJECT_DIR:-$(pwd)}"
cd "$PROJECT_DIR" 2>/dev/null || exit 0

if [ -f scripts/check_progress_docs.py ]; then
  (python3 scripts/check_progress_docs.py 2>/dev/null || python scripts/check_progress_docs.py) || {
    cat >&2 <<'ERR'
Progress or handoff documentation is missing or scope boundaries were violated.

Before stopping, update the appropriate docs:
- docs/agent/04_TASK_HANDOFF.md
- docs/agent/05_PROGRESS.md
- docs/agent/08_IMPLEMENTATION_BRIEF.md
- docs/agent/09_CODING_HANDOFF.md
- docs/agent/10_REVIEW_REPORT.md
- docs/agent/11_AGENT_STATE.md
- docs/agent/12_AGENT_BOARD.md
- docs/agent/13_CHANGE_CONTROL.md if needed
- docs/agent/06_DECISION_LOG.md if needed
ERR
    exit 2
  }
fi

exit 0
