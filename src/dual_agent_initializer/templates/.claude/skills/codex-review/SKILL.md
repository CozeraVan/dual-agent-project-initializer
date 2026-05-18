---
name: codex-review
description: Codex review flow that checks implementation and routes through Fail Path or Pass Path.
---

# Codex Review

Use this when Codex is the current owner and phase is `CODEX_REVIEWING`.

Do not implement code unless explicitly requested.

Read:

- `AGENTS.md`
- `docs/agent/02_LOCKED_REQUIREMENTS.md`
- `docs/agent/08_IMPLEMENTATION_BRIEF.md`
- `docs/agent/09_CODING_HANDOFF.md`
- `docs/agent/10_REVIEW_REPORT.md`
- `docs/agent/11_AGENT_STATE.md`
- `docs/agent/12_AGENT_BOARD.md`
- `docs/agent/13_CHANGE_CONTROL.md`

Inspect:

```bash
git status
git diff --name-only HEAD
git diff HEAD
python scripts/check_progress_docs.py
git diff --check
```

Write:

- `docs/agent/10_REVIEW_REPORT.md`

## Fail Path

If Required Fixes exist:

- Set Review Outcome = FAIL.
- Update `10_REVIEW_REPORT.md`.
- Update `12_AGENT_BOARD.md` with a fix request.
- Phase: `CLAUDE_FIXING`.
- Owner: `CLAUDE_CODE`.
- Do not commit.
- Do not push.

## Pass Path

If review passes and One-Shot Review-Finalize-Next is requested:

- Set Review Outcome = PASS.
- Run final checks.
- Create a local implementation commit.
- Do not push by default.
- Prepare next `08_IMPLEMENTATION_BRIEF.md`.
- Reset/update `09_CODING_HANDOFF.md`.
- Update `12_AGENT_BOARD.md` for Claude Code.
- Create a local planning docs commit.
- Phase: `CLAUDE_IMPLEMENTING`.
- Owner: `CLAUDE_CODE`.

If review passes but user wants to stop:

- Phase: `USER_ACCEPTANCE`.
- Owner: `USER`.
