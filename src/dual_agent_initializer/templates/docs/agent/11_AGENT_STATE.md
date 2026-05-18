# Agent State

This file is the source of truth for dual-agent workflow recovery.

## Current Task ID

NONE

## Current Phase

Allowed values:

- IDEA_INTAKE
- CODEX_PLANNING
- CHANGE_REQUEST_REVIEW
- ARCHITECTURE_REVIEW
- WAITING_USER_APPROVAL
- CLAUDE_IMPLEMENTING
- CODEX_REVIEWING
- CLAUDE_FIXING
- USER_ACCEPTANCE
- CODEX_GIT_FINALIZING
- DONE
- BLOCKED

Current:

IDEA_INTAKE

## Current Owner

Allowed values:

- USER
- CODEX
- CLAUDE_CODE

Current:

USER

## Last Completed Step

Project workflow initialized.

## Next Required Step

User should discuss project goals and architecture with Codex.

## Active Change Request

None

## Active Implementation Brief

`docs/agent/08_IMPLEMENTATION_BRIEF.md`

## Active Coding Handoff

`docs/agent/09_CODING_HANDOFF.md`

## Active Review Report

`docs/agent/10_REVIEW_REPORT.md`

## Active Agent Board

`docs/agent/12_AGENT_BOARD.md`

## Active Change Control Protocol

`docs/agent/13_CHANGE_CONTROL.md`

## Git State

- Current branch: TODO
- Remote: TODO
- Last checkpoint commit: TODO
- Last implementation commit: TODO
- Last review/planning commit: TODO
- Last pushed commit: TODO

## Standing Approval

Default:

- Codex may create local commits after review passes.
- Codex must ask user before `git push`.

To allow Codex to push automatically for this project, user must explicitly write a standing approval here.

Standing approval:

NONE

## Recovery Instruction

If unsure where to continue:

1. Read this file first.
2. Read:
   - `docs/agent/12_AGENT_BOARD.md`
   - `docs/agent/04_TASK_HANDOFF.md`
   - `docs/agent/05_PROGRESS.md`
   - `docs/agent/08_IMPLEMENTATION_BRIEF.md`
   - `docs/agent/09_CODING_HANDOFF.md`
   - `docs/agent/10_REVIEW_REPORT.md`
   - `docs/agent/13_CHANGE_CONTROL.md`
3. Run:
   ```bash
   git status
   git diff
   git log --oneline -5
   ```
4. Determine current phase before modifying code.
5. If current owner is not the active agent, do not proceed.

## Short Prompt Commands

### For Claude Code

请读取 11 和 12，执行当前 Claude Code 任务。

### For Codex Daily Review

请读取 11 和 12，执行 One-Shot Review-Finalize-Next。

### For Codex New Idea

请读取 11 和 12，把以下新 idea 作为 Change Request 分析，不改代码。

### For Codex Architecture Change

请进入 Architecture Change Mode，读取 11、12、13，对以下架构变更做影响分析，不改业务代码。

## One-Shot Review Routing State Transitions

### CODEX_REVIEWING + FAIL

If Codex review fails:

- Do not commit.
- Do not push.
- Update `10_REVIEW_REPORT.md` with Review Outcome = FAIL.
- Update `12_AGENT_BOARD.md` with Required Fixes.
- Phase: `CLAUDE_FIXING`
- Owner: `CLAUDE_CODE`

### CODEX_REVIEWING + PASS

If Codex review passes and One-Shot Review-Finalize-Next is requested:

- Update `10_REVIEW_REPORT.md` with Review Outcome = PASS.
- Create local implementation commit.
- Do not push unless standing approval exists or user explicitly approves.
- Prepare next `08_IMPLEMENTATION_BRIEF.md`.
- Reset/update `09_CODING_HANDOFF.md`.
- Update `12_AGENT_BOARD.md` with next Claude Code task.
- Create planning docs commit.
- Phase: `CLAUDE_IMPLEMENTING`
- Owner: `CLAUDE_CODE`

## Change Control State Transitions

### New Idea -> Change Request Review

- Phase: `CHANGE_REQUEST_REVIEW`
- Owner: `CODEX`

### Architecture Change -> Architecture Review

- Phase: `ARCHITECTURE_REVIEW`
- Owner: `CODEX`

### Approved Change -> Codex Planning

- Phase: `CODEX_PLANNING`
- Owner: `CODEX`

### Approved Brief -> Claude Implementation

- Phase: `CLAUDE_IMPLEMENTING`
- Owner: `CLAUDE_CODE`

## Manual Phase Transition Rules

### User -> Codex Planning

When the user gives a new approved idea:

- Phase: `CODEX_PLANNING`
- Owner: `CODEX`

### Codex Planning -> User Approval

After Codex writes Implementation Brief and user approval is required:

- Phase: `WAITING_USER_APPROVAL`
- Owner: `USER`

### Claude Implementation -> Codex Review

After Claude Code finishes implementation:

- Phase: `CODEX_REVIEWING`
- Owner: `CODEX`

### Codex Review -> User Acceptance

If review passes but the user wants to stop before next planning:

- Phase: `USER_ACCEPTANCE`
- Owner: `USER`

### Codex Git Finalizing -> Done

After successful local commit and optional approved push:

- Phase: `DONE`
- Owner: `USER`
