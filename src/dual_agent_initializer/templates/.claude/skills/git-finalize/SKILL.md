---
name: git-finalize
description: Final git verification and local commit flow. Push is optional and user-approved by default.
---

# Git Finalize

This flow is Codex-owned by default. It creates local checkpoints. Push requires explicit approval by default.

Use only when:

- Codex is the current owner
- Review has passed
- No Required Fixes remain
- User has approved finalization or One-Shot Review-Finalize-Next requires a local checkpoint

Required checks:

```bash
git status
git diff --name-only HEAD
python scripts/check_progress_docs.py
python scripts/git_finalize_check.py
```

Then:

1. Confirm no secrets are included.
2. Commit locally:
   ```bash
   git add -A
   git commit -m "..."
   ```
3. Do not push unless the user explicitly approves or standing approval exists.
4. If push is approved:
   ```bash
   git push
   ```
5. Update:
   - `docs/agent/11_AGENT_STATE.md`
   - `docs/agent/04_TASK_HANDOFF.md`
   - `docs/agent/05_PROGRESS.md`

Final state:

- Phase: `DONE` or next planned phase
- Owner: `USER` or next owner
