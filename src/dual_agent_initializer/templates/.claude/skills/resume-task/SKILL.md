---
name: resume-task
description: Recover project context after an interrupted session.
---

# Resume Interrupted Task

Do not modify code immediately.

Read:

- `CLAUDE.md` if available
- `AGENTS.md` if available
- `docs/agent/11_AGENT_STATE.md`
- `docs/agent/12_AGENT_BOARD.md`
- `docs/agent/04_TASK_HANDOFF.md`
- `docs/agent/05_PROGRESS.md`
- `docs/agent/07_RECOVERY_PROTOCOL.md`
- `docs/agent/08_IMPLEMENTATION_BRIEF.md`
- `docs/agent/09_CODING_HANDOFF.md`
- `docs/agent/10_REVIEW_REPORT.md`
- `docs/agent/13_CHANGE_CONTROL.md`

Inspect:

```bash
git status
git diff --name-only HEAD
git diff HEAD
git log --oneline -5
```

Output:

1. Current project phase
2. Current task ID
3. Current owner
4. Completed work
5. In-progress work
6. Uncommitted changes
7. Half-finished files
8. Next minimal safe step

Wait for user confirmation.
