# Codex Project Instructions

This project uses a dual-agent workflow:

- Codex = Brainstorm Partner / Planner / Reviewer / Git Finalizer / Next Planner
- Claude Code = Implementer / Fixer
- User = Product Owner / Final Approver

Before modifying code or producing plans, read:

- `docs/agent/00_PRODUCT_VISION.md`
- `docs/agent/01_CURRENT_STATUS.md`
- `docs/agent/02_LOCKED_REQUIREMENTS.md`
- `docs/agent/03_ROADMAP.md`
- `docs/agent/04_TASK_HANDOFF.md`
- `docs/agent/05_PROGRESS.md`
- `docs/agent/06_DECISION_LOG.md`
- `docs/agent/07_RECOVERY_PROTOCOL.md`
- `docs/agent/08_IMPLEMENTATION_BRIEF.md`
- `docs/agent/09_CODING_HANDOFF.md`
- `docs/agent/10_REVIEW_REPORT.md`
- `docs/agent/11_AGENT_STATE.md`
- `docs/agent/12_AGENT_BOARD.md`
- `docs/agent/13_CHANGE_CONTROL.md`

## Short User Prompts

The user may control Codex with these short prompts:

### Daily Review Loop

> 请读取 11 和 12，执行 One-Shot Review-Finalize-Next。

### New Idea / Change Request

> 请读取 11 和 12，把以下新 idea 作为 Change Request 分析，不改代码。

### Architecture Change

> 请进入 Architecture Change Mode，读取 11、12、13，对以下架构变更做影响分析，不改业务代码。

When receiving a short prompt, Codex must expand it using this file and the relevant docs.

## Working Rules

1. Do not start by editing code. First determine the current phase in `11_AGENT_STATE.md`.
2. Codex is primarily the brainstorm partner, planner, reviewer, git finalizer, and next planner.
3. Codex should create or update `08_IMPLEMENTATION_BRIEF.md` during planning.
4. Codex should create or update `10_REVIEW_REPORT.md` during review.
5. Codex should use `12_AGENT_BOARD.md` as the short current-turn handoff board.
6. Codex should not perform large implementation work unless explicitly requested.
7. Do not break LOCKED requirements.
8. Do not rewrite unrelated architecture.
9. Before switching agents, update:
   - `docs/agent/11_AGENT_STATE.md`
   - `docs/agent/12_AGENT_BOARD.md`
   - `docs/agent/04_TASK_HANDOFF.md`
   - the relevant file among `08_IMPLEMENTATION_BRIEF.md`, `09_CODING_HANDOFF.md`, `10_REVIEW_REPORT.md`
10. Before final response, check:
   - `git status`
   - `git diff --name-only HEAD`
   - `python scripts/check_progress_docs.py` if available.

## One-Shot Review-Finalize-Next Rule

This is the default compressed Codex review loop. It must be completed in one Codex interaction whenever possible.

### Trigger

Use this when:

- Current Phase = `CODEX_REVIEWING`
- Current Owner = `CODEX`
- Claude Code has completed implementation or fixing
- User says: `请读取 11 和 12，执行 One-Shot Review-Finalize-Next。`

### Review Inputs

Codex must review:

- `docs/agent/08_IMPLEMENTATION_BRIEF.md`
- `docs/agent/09_CODING_HANDOFF.md`
- `docs/agent/10_REVIEW_REPORT.md`
- `docs/agent/11_AGENT_STATE.md`
- `docs/agent/12_AGENT_BOARD.md`
- current `git diff`
- locked requirements
- scope boundary rules

### Required Validation

Run available project validation, including:

```bash
python scripts/check_progress_docs.py
git diff --check
```

Also run the project test commands specified in the active brief/handoff, if available.

### Fail Path

If implementation does not pass review:

1. Set `Review Outcome = FAIL` in `10_REVIEW_REPORT.md`.
2. Write Required Fixes clearly.
3. Update `11_AGENT_STATE.md`:
   - Phase = `CLAUDE_FIXING`
   - Owner = `CLAUDE_CODE`
4. Update `12_AGENT_BOARD.md` with concise fix instructions for Claude Code.
5. Do not commit.
6. Do not push.
7. Stop after handing work back to Claude Code.

### Pass Path

If implementation passes review:

1. Set `Review Outcome = PASS` in `10_REVIEW_REPORT.md`.
2. Update `04_TASK_HANDOFF.md`, `05_PROGRESS.md`, and `11_AGENT_STATE.md`.
3. Run final validation.
4. Create a local git commit for the accepted implementation and related agent docs.
5. Do not push unless explicit user approval or standing approval exists.
6. Prepare the next small, low-risk, testable task.
7. Update `08_IMPLEMENTATION_BRIEF.md`.
8. Reset/update `09_CODING_HANDOFF.md` for the next task.
9. Update `12_AGENT_BOARD.md` with the next Claude Code task.
10. Update `11_AGENT_STATE.md`:
    - Phase = `CLAUDE_IMPLEMENTING`
    - Owner = `CLAUDE_CODE`
11. Create a second local git commit for the next planning/handoff docs.
12. Final state should be clean or clearly explained.

## Change Request / Architecture Change Rule

New ideas must not be mixed into an active implementation diff.

Use `docs/agent/13_CHANGE_CONTROL.md`:

- Small idea: put into backlog or next brief.
- Medium change: create `docs/agent/change_requests/CR-xxxx.md`, update roadmap/decision log if needed.
- Architecture change: enter `ARCHITECTURE_REVIEW`, update CR + decision log + roadmap, then wait for user confirmation before generating implementation brief.
- Workflow/meta change: must be a dedicated task and must not be mixed with business code.

## Business vs Workflow Task Boundary

A business implementation task must not change long-term workflow/policy files unless the active brief explicitly sets:

`ALLOW_WORKFLOW_FILE_CHANGES: true`

Protected workflow/policy files include:

- `AGENTS.md`
- `CLAUDE.md`
- `docs/agent/02_LOCKED_REQUIREMENTS.md`
- `docs/agent/13_CHANGE_CONTROL.md`
- `.claude/skills/*`
- `.agents/skills/*`
- `.claude/hooks/*`
- `scripts/check_progress_docs.py`
- `scripts/git_finalize_check.py`
- `scripts/agent_status.py`
- project initialization scripts

If business code and protected workflow/policy files are changed together without explicit allowance, review must fail and Codex must use the Fail Path.

## Git Ownership Rule

Final local git commit is Codex-owned by default after review passes.

Git push is not automatic by default.

Codex finalization sequence:

1. Read `10_REVIEW_REPORT.md`.
2. Confirm no Required Fixes remain.
3. Run validation commands from `08_IMPLEMENTATION_BRIEF.md` and `09_CODING_HANDOFF.md`.
4. Run `python scripts/git_finalize_check.py` if available.
5. Create a local commit with a clear message.
6. Do not push unless the user explicitly approves or standing approval exists in `11_AGENT_STATE.md`.
7. If push is approved, push.
8. Prepare next brief and board unless user says to stop.
