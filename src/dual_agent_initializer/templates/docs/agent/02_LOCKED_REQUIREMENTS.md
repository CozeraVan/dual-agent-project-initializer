# Locked Requirements

Locked requirements must not be removed, weakened, or silently changed.

## R-CORE-001: Preserve existing working behavior

Status: LOCKED

Do not remove working features unless explicitly requested.

## R-CORE-002: No unrelated rewrites

Status: LOCKED

Do not rewrite unrelated modules while implementing a focused task.

## R-CORE-003: Changes must be verifiable

Status: LOCKED

Every meaningful code change should have a validation path:

- tests
- lint
- typecheck
- manual verification
- documented reason why validation is unavailable

## R-CORE-004: Protect user secrets

Status: LOCKED

Do not read, print, commit, or push secrets.

Protected examples:

- `.env`
- `.env.*`
- API keys
- database credentials
- SSH keys
- cloud credentials
- personal tokens

## R-CORE-005: Preserve project memory files

Status: LOCKED

Do not delete the agent workflow files unless explicitly requested:

- `CLAUDE.md`
- `AGENTS.md`
- `docs/agent/*`

## R-DUAL-001: Codex owns planning and review

Status: LOCKED

Codex should produce:

- `08_IMPLEMENTATION_BRIEF.md`
- `10_REVIEW_REPORT.md`

Codex should not do large implementation work unless explicitly requested.

## R-DUAL-002: Claude Code owns implementation

Status: LOCKED

Claude Code should implement from:

- `08_IMPLEMENTATION_BRIEF.md`
- `12_AGENT_BOARD.md`

Claude Code should not invent architecture beyond the brief unless it first writes a question or blocker.

## R-DUAL-003: Agent state is the source of truth

Status: LOCKED

If chat history and docs disagree, prefer:

1. `11_AGENT_STATE.md`
2. `12_AGENT_BOARD.md`
3. `04_TASK_HANDOFF.md`
4. `08_IMPLEMENTATION_BRIEF.md`
5. `09_CODING_HANDOFF.md`
6. `10_REVIEW_REPORT.md`
7. `git status` / `git log`

## R-DUAL-004: One-Shot review routing is mandatory

Status: LOCKED

When Codex is asked to execute One-Shot Review-Finalize-Next, Codex must choose exactly one route:

### Fail Path

If review fails:

- Do not commit.
- Do not push.
- Update `10_REVIEW_REPORT.md` with `Review Outcome = FAIL`.
- Write Required Fixes.
- Update `11_AGENT_STATE.md` to `CLAUDE_FIXING` / `CLAUDE_CODE`.
- Update `12_AGENT_BOARD.md` with concise fix instructions.

### Pass Path

If review passes:

- Update `10_REVIEW_REPORT.md` with `Review Outcome = PASS`.
- Update progress/handoff/state docs.
- Create a local git commit for accepted implementation.
- Do not push unless explicit approval or standing approval exists.
- Prepare the next `08_IMPLEMENTATION_BRIEF.md` and `12_AGENT_BOARD.md`.
- Commit the next planning/handoff docs.
- Set `11_AGENT_STATE.md` to `CLAUDE_IMPLEMENTING` / `CLAUDE_CODE`.

## R-DUAL-005: Business tasks must not modify workflow/policy files

Status: LOCKED

Business implementation tasks must not modify long-term workflow/policy files unless the active `08_IMPLEMENTATION_BRIEF.md` explicitly contains:

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

If business code and protected workflow/policy files are changed together without explicit allowance, review must fail.

## R-CHANGE-001: New ideas enter through Change Control

Status: LOCKED

New ideas, mid-project scope changes, architecture changes, and workflow/meta changes must follow `docs/agent/13_CHANGE_CONTROL.md`.

Claude Code must not implement a new idea until Codex has classified it and produced or updated an approved Implementation Brief.

## R-GIT-001: Codex owns final local git commit

Status: LOCKED

By default, final local commit should be performed by Codex after review passes.

Default policy:

- Claude Code may implement code.
- Codex reviews.
- If review fails, no commit.
- If review passes, Codex creates a local checkpoint commit.
- Git push requires explicit approval or standing approval.

## R-GIT-002: No push before review passes

Status: LOCKED

Do not push code until:

- implementation is complete,
- required tests/checks have run or unavailable checks are documented,
- `10_REVIEW_REPORT.md` has no Required Fixes,
- user approval or standing approval exists.

## R-GIT-003: Failed review must not be committed

Status: LOCKED

If `Review Outcome = FAIL`, Codex must not create a commit containing the failed implementation. It must return the task to Claude Code through `11_AGENT_STATE.md` and `12_AGENT_BOARD.md`.
