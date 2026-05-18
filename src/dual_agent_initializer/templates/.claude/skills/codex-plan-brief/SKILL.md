---
name: codex-plan-brief
description: Codex planner flow that converts a user request or Change Request into an Implementation Brief for Claude Code.
---

# Codex Plan Brief

Use this when Codex is the current owner and phase is `CODEX_PLANNING`, `CHANGE_REQUEST_REVIEW`, or `ARCHITECTURE_REVIEW`.

Do not implement code.

Read:

- `AGENTS.md`
- `docs/agent/02_LOCKED_REQUIREMENTS.md`
- `docs/agent/03_ROADMAP.md`
- `docs/agent/05_PROGRESS.md`
- `docs/agent/11_AGENT_STATE.md`
- `docs/agent/12_AGENT_BOARD.md`
- `docs/agent/13_CHANGE_CONTROL.md`
- active Change Request if any

Write or update:

- `docs/agent/08_IMPLEMENTATION_BRIEF.md`
- `docs/agent/12_AGENT_BOARD.md`

Then update:

- `docs/agent/11_AGENT_STATE.md`
- `docs/agent/04_TASK_HANDOFF.md`
- `docs/agent/05_PROGRESS.md`
- `docs/agent/06_DECISION_LOG.md` if needed

Next state after the brief is ready:

- Phase: `WAITING_USER_APPROVAL` or `CLAUDE_IMPLEMENTING`
- Owner: `USER` or `CLAUDE_CODE`
