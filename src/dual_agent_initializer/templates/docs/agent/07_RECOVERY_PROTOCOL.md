# Recovery Protocol

Use this file when:

- a session was interrupted,
- terminal closed,
- network failed,
- user forgot which agent was working,
- Claude Code completed several rounds before Codex review,
- Codex review was delayed,
- the dual-agent sequence was broken.

## Recovery Steps

1. Do not modify code immediately.
2. Read:
   - `docs/agent/11_AGENT_STATE.md`
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
   git diff --name-only HEAD
   git diff HEAD
   git log --oneline -5
   ```
4. Determine:
   - Current Task ID
   - Current Phase
   - Current Owner
   - Whether code has unreviewed changes
   - Whether review has Required Fixes
   - Whether local git finalization has happened
   - Whether a Change Request or Architecture Change is active
5. Output a recovery summary.
6. Wait for user confirmation before editing code or pushing.

## Recovery Decision Table

| Observed State | Next Owner | Next Action |
|---|---|---|
| No brief exists | CODEX | Create Implementation Brief or Change Request |
| Brief exists, no implementation | CLAUDE_CODE | Implement from brief |
| Implementation exists, no review | CODEX | Review diff and write Review Report |
| Review has Required Fixes | CLAUDE_CODE | Fix only Required Fixes |
| Review passes, no local commit | CODEX | Final checks, local commit, prepare next brief/board; do not push by default |
| Local commit and next board complete | CLAUDE_CODE | Execute next Agent Board |
| New idea arrives mid-task | CODEX | Record Change Request without disturbing current task unless blocker |
| Architecture change requested | CODEX + USER | Enter Architecture Change Mode before any implementation |

## Rule

If unsure, prefer returning control to Codex for planning/review rather than allowing Claude Code to continue implementation freely.
