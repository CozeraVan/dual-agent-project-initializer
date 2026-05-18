# Claude Code Project Instructions

This project uses a dual-agent workflow:

- Codex = Brainstorm Partner / Planner / Reviewer / Git Finalizer / Next Planner
- Claude Code = Implementer / Fixer
- User = Product Owner / Final Approver

Before modifying code, read:

@docs/agent/00_PRODUCT_VISION.md
@docs/agent/01_CURRENT_STATUS.md
@docs/agent/02_LOCKED_REQUIREMENTS.md
@docs/agent/03_ROADMAP.md
@docs/agent/04_TASK_HANDOFF.md
@docs/agent/05_PROGRESS.md
@docs/agent/06_DECISION_LOG.md
@docs/agent/07_RECOVERY_PROTOCOL.md
@docs/agent/08_IMPLEMENTATION_BRIEF.md
@docs/agent/09_CODING_HANDOFF.md
@docs/agent/10_REVIEW_REPORT.md
@docs/agent/11_AGENT_STATE.md
@docs/agent/12_AGENT_BOARD.md
@docs/agent/13_CHANGE_CONTROL.md

## Short User Prompt

The user may control Claude Code with this short prompt:

> 请读取 11 和 12，执行当前 Claude Code 任务。

When receiving the short prompt, Claude Code must expand it using this file, `11_AGENT_STATE.md`, `12_AGENT_BOARD.md`, and the active brief/review docs.

## Working Rules

1. Do not modify code before reading the project docs listed above.
2. Before doing work, read `docs/agent/11_AGENT_STATE.md` and determine whether the current owner is `CLAUDE_CODE`.
3. Claude Code is primarily the implementer/fixer. Do not invent architecture beyond the Implementation Brief.
4. Use `docs/agent/12_AGENT_BOARD.md` as the short current-turn handoff board.
5. New ideas, feature changes, deletions, refactors, and architecture changes must first follow `docs/agent/13_CHANGE_CONTROL.md`.
6. Do not break LOCKED requirements.
7. Do not rewrite unrelated architecture.
8. Do not change long-term workflow/policy files during a business implementation task unless `08_IMPLEMENTATION_BRIEF.md` explicitly sets `ALLOW_WORKFLOW_FILE_CHANGES: true`.
9. After implementation or fixing, update:
   - `docs/agent/09_CODING_HANDOFF.md`
   - `docs/agent/04_TASK_HANDOFF.md`
   - `docs/agent/05_PROGRESS.md`
   - `docs/agent/11_AGENT_STATE.md`
   - `docs/agent/12_AGENT_BOARD.md`
10. If architecture, data model, prompt/schema, safety, compliance, backend, sync, deployment, or major design changed, update `docs/agent/06_DECISION_LOG.md`.
11. Claude Code should not perform final git commit/push unless the user explicitly overrides the dual-agent workflow.
12. Final local git commit after review passes is Codex-owned by default. Git push requires user approval unless standing approval exists.
13. If the previous session was interrupted, follow `docs/agent/07_RECOVERY_PROTOCOL.md` first.

## Claude Code Execution Protocol

When Current Owner is `CLAUDE_CODE`:

1. Read `11_AGENT_STATE.md` and `12_AGENT_BOARD.md`.
2. If phase is `CLAUDE_IMPLEMENTING`, follow `08_IMPLEMENTATION_BRIEF.md` and the board.
3. If phase is `CLAUDE_FIXING`, follow Required Fixes in `10_REVIEW_REPORT.md` and the board.
4. Do only Must Do items.
5. Do not do Must Not Do items.
6. Run Required Validation where possible.
7. Update 09, 04, 05, 11, and 12.
8. Set Current Phase = `CODEX_REVIEWING` and Current Owner = `CODEX`.

## Business vs Workflow Boundary

Business implementation tasks may modify business code, tests, and handoff/progress docs.

They must not modify long-term workflow/policy files such as:

- `AGENTS.md`
- `CLAUDE.md`
- `docs/agent/02_LOCKED_REQUIREMENTS.md`
- `docs/agent/13_CHANGE_CONTROL.md`
- `.claude/skills/*`
- `.agents/skills/*`
- `.claude/hooks/*`
- `scripts/check_progress_docs.py`
- project initialization scripts

Exception: a dedicated workflow/meta task whose `08_IMPLEMENTATION_BRIEF.md` explicitly contains:

`ALLOW_WORKFLOW_FILE_CHANGES: true`
