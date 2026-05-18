# Decision Log

Use this file for decisions that affect architecture, data, safety, compliance, prompts, schema, deployment, or dual-agent workflow.

## Format

### YYYY-MM-DD: Decision title

- Decision:
- Reason:
- Alternatives:
- Impact:
- Owner:

---

### Initial: Use dual-agent workflow

- Decision: This project uses Codex as Brainstorm Partner/Planner/Reviewer/Git Finalizer/Next Planner and Claude Code as Implementer/Fixer.
- Reason: This separates planning, implementation, review, and final git operations.
- Alternatives: Single-agent coding; manual-only workflow.
- Impact: Normal tasks should pass through `08_IMPLEMENTATION_BRIEF.md`, `09_CODING_HANDOFF.md`, `10_REVIEW_REPORT.md`, `11_AGENT_STATE.md`, and `12_AGENT_BOARD.md`; new ideas and architecture changes should follow `13_CHANGE_CONTROL.md`.
- Owner: USER
