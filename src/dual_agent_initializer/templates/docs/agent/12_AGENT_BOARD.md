# Agent Board

This file is the current short handoff board between Codex and Claude Code.

It is short-term and may be overwritten at each agent handoff.

Long-term workflow rules live in:

- `AGENTS.md`
- `CLAUDE.md`
- `docs/agent/02_LOCKED_REQUIREMENTS.md`
- `docs/agent/11_AGENT_STATE.md`
- `docs/agent/13_CHANGE_CONTROL.md`

## Protocol Reference

- For Codex review routing, follow `AGENTS.md` -> `One-Shot Review-Finalize-Next Rule`.
- For new ideas and architecture changes, follow `docs/agent/13_CHANGE_CONTROL.md`.

## Current Task ID

NONE

## Current Recipient

Allowed values:

- CODEX
- CLAUDE_CODE
- USER

Current:

USER

## Message Type

Allowed values:

- PLAN_TO_CLAUDE
- FIX_REQUEST_TO_CLAUDE
- REVIEW_REQUEST_TO_CODEX
- CHANGE_REQUEST_TO_CODEX
- ARCHITECTURE_CHANGE_TO_CODEX
- REVIEW_TO_USER
- FINALIZE_AND_NEXT_PLAN
- BLOCKED

Current:

BLOCKED

## Sender

SYSTEM

## Short Message

Project workflow initialized. User should discuss project goals and the first task with Codex.

## Must Read

- `docs/agent/11_AGENT_STATE.md`
- `docs/agent/08_IMPLEMENTATION_BRIEF.md`
- `docs/agent/09_CODING_HANDOFF.md`
- `docs/agent/10_REVIEW_REPORT.md`
- `docs/agent/02_LOCKED_REQUIREMENTS.md`
- `docs/agent/13_CHANGE_CONTROL.md`

## Must Do

1. Wait for the user to provide the first project-specific goal.
2. Codex should create the first Implementation Brief before Claude Code starts implementation.

## Must Not Do

1. Do not make unrelated changes.
2. Do not change architecture unless the brief explicitly allows it.
3. Do not commit or push unless the workflow explicitly allows it.
4. Do not start implementation when Current Owner is not `CLAUDE_CODE`.

## Allowed Files

- `docs/agent/*`

## Forbidden Files

- `src/*`
- `tests/*`
- `configs/*`
- `pyproject.toml`
- `uv.lock`
- `package.json`
- `package-lock.json`
- `pnpm-lock.yaml`

## Required Validation

```bash
python scripts/check_progress_docs.py
git diff --check
```

## Completion Rule

When Claude Code completes implementation or fixing, it must update:

- `docs/agent/09_CODING_HANDOFF.md`
- `docs/agent/04_TASK_HANDOFF.md`
- `docs/agent/05_PROGRESS.md`
- `docs/agent/11_AGENT_STATE.md`
- `docs/agent/12_AGENT_BOARD.md`

Then it should set:

- Current Phase = `CODEX_REVIEWING`
- Current Owner = `CODEX`
