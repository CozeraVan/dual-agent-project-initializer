# Implementation Brief

## Task ID

TBD

## Created By

CODEX

## Intended Implementer

CLAUDE_CODE

## Workflow File Changes Allowed

ALLOW_WORKFLOW_FILE_CHANGES: false

Set to `true` only for a dedicated workflow/meta task. Business implementation tasks must keep this as `false`.

## Background

TODO

## Goal

TODO

## Non-Goals

TODO

## Affected Modules

- TBD

## Files Likely to Change

- TBD

## Forbidden Files

- TBD

## Locked Requirements

Read:

- `docs/agent/02_LOCKED_REQUIREMENTS.md`

Task-specific locked requirements:

- TBD

## Implementation Steps

1. TODO

## Data / Schema Changes

None yet.

## API / Interface Changes

None yet.

## Validation Plan

TODO

Examples:

```bash
python -m pytest
npm test
```

## Acceptance Criteria

- [ ] TODO

## Risks

TODO

## Instructions for Claude Code

Claude Code must:

1. Follow this brief strictly.
2. Avoid unrelated refactors.
3. Avoid modifying forbidden files.
4. Avoid modifying workflow/policy files unless `ALLOW_WORKFLOW_FILE_CHANGES: true`.
5. Stop and ask if the brief conflicts with existing code.
6. Run validation commands where possible.
7. Update:
   - `docs/agent/09_CODING_HANDOFF.md`
   - `docs/agent/04_TASK_HANDOFF.md`
   - `docs/agent/05_PROGRESS.md`
   - `docs/agent/11_AGENT_STATE.md`
   - `docs/agent/12_AGENT_BOARD.md`
8. If architecture changes, also update `docs/agent/06_DECISION_LOG.md`.

## Next Agent State After Brief Is Approved

- Phase: `CLAUDE_IMPLEMENTING`
- Owner: `CLAUDE_CODE`
