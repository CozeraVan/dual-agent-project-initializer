# Change Control Protocol

This file defines how new ideas, scope changes, architecture changes, and workflow/meta changes enter the project after the initial brainstorm.

## Purpose

Normal coding uses the daily loop:

Codex Review-Finalize-Next -> Claude Code implementation -> Codex Review-Finalize-Next

New ideas and architecture changes must not be mixed into an active implementation diff.

## Short User Prompts

### New Idea

```text
请读取 11 和 12，把以下新 idea 作为 Change Request 分析，不改代码。
```

### Architecture Change

```text
请进入 Architecture Change Mode，读取 11、12、13，对以下架构变更做影响分析，不改业务代码。
```

## Change Levels

### Level 1: Small Idea

Examples:

- small CLI option
- one focused test
- minor output formatting
- small non-breaking behavior improvement

Process:

1. Codex may add it to backlog or next `08_IMPLEMENTATION_BRIEF.md`.
2. No architecture change is required.
3. Claude Code implements only after Codex writes/updates the brief and board.

### Level 2: Medium Change Request

Examples:

- changes to module responsibilities
- new report artifact
- new interface behavior
- roadmap-level feature

Process:

1. Codex creates `docs/agent/change_requests/CR-xxxx-short-name.md`.
2. Codex updates `03_ROADMAP.md`, `05_PROGRESS.md`, and possibly `06_DECISION_LOG.md`.
3. User approves or rejects the change.
4. Codex writes or updates `08_IMPLEMENTATION_BRIEF.md` and `12_AGENT_BOARD.md`.
5. Claude Code implements.

### Level 3: Architecture Change

Examples:

- changing project long-term goal
- changing data layer / service boundaries
- changing locked requirements
- changing storage model
- changing security/compliance/safety model

Process:

1. Codex enters `ARCHITECTURE_REVIEW`.
2. Codex creates a Change Request.
3. Codex performs impact analysis.
4. Codex proposes updates to:
   - `00_PRODUCT_VISION.md`
   - `02_LOCKED_REQUIREMENTS.md`
   - `03_ROADMAP.md`
   - `06_DECISION_LOG.md`
   - `11_AGENT_STATE.md`
   - `12_AGENT_BOARD.md`
5. User confirms before implementation.
6. Codex writes a new `08_IMPLEMENTATION_BRIEF.md`.
7. Claude Code implements.

### Level 4: Workflow / Meta Change

Examples:

- changing dual-agent rules
- changing `AGENTS.md` / `CLAUDE.md`
- changing locked workflow policy
- changing skills/hooks/scripts
- changing initialization templates

Process:

1. Must be a dedicated workflow/meta task.
2. Must not be mixed with business code.
3. Active `08_IMPLEMENTATION_BRIEF.md` must contain:

   `ALLOW_WORKFLOW_FILE_CHANGES: true`

4. Codex reviews scope boundary carefully.
5. Codex may commit only after the workflow/meta review passes.

## Mid-Task New Ideas

If the user has a new idea while Claude Code is implementing:

- Do not interrupt Claude Code unless the idea invalidates the current task.
- Codex should record the idea as a Change Request or backlog item.
- The current task should finish and be reviewed first.
- The idea may become the next brief after review passes.

## Blocking Architecture Change

If a new idea invalidates the current task:

1. Codex enters `ARCHITECTURE_REVIEW` or `BLOCKED`.
2. Codex explains whether current Claude Code implementation should stop.
3. No business code should be committed until the conflict is resolved.

## Change Request Template

Use:

`docs/agent/change_requests/CR-0000-template.md`

## Rule

New idea -> Change Request.
Architecture change -> Decision.
Approved decision -> Implementation Brief.
Claude Code executes only approved briefs.
