---
name: intake-change
description: Turn a new idea, feature, refactor, architecture change, or deletion request into a formal Change Request.
---

# Intake Change Request

Do not modify business code.

Read:

- `docs/agent/11_AGENT_STATE.md`
- `docs/agent/12_AGENT_BOARD.md`
- `docs/agent/13_CHANGE_CONTROL.md`

Create a new file under:

`docs/agent/change_requests/`

Use the next available ID:

`CR-0001-short-name.md`

Include:

1. Background
2. Goal
3. User scenario
4. Change level
5. In Scope
6. Out of Scope
7. Affected requirements
8. Protected requirements
9. Suggested tasks
10. Acceptance criteria
11. Risks
12. Impact analysis
13. Proposed agent state transition

Update `docs/agent/11_AGENT_STATE.md` based on the change level:

- Small/medium change: `CHANGE_REQUEST_REVIEW` / `CODEX`
- Architecture change: `ARCHITECTURE_REVIEW` / `CODEX`
- Workflow/meta change: `ARCHITECTURE_REVIEW` / `CODEX`

Then summarize and wait for confirmation.
