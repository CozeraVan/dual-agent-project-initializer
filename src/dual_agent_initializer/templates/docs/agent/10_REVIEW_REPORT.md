# Review Report

## Task ID

TBD

## Written By

CODEX

## Reviewed Implementation

TODO

## Review Outcome

Allowed values:

- TODO
- PASS
- FAIL

Current:

TODO

## Review Summary

TODO

## Compliance with Implementation Brief

TODO

## Scope Boundary Check

| Check | Status | Evidence |
|---|---|---|
| Business code changed only within allowed scope | TODO | - |
| Protected workflow/policy files unchanged, unless explicitly allowed | TODO | - |
| `ALLOW_WORKFLOW_FILE_CHANGES` respected | TODO | - |
| Markdown files are not accidentally executable | TODO | - |
| No unrelated project areas changed | TODO | - |

If business code and protected workflow/policy files are changed together without explicit allowance, review must fail.

## Locked Requirements Check

TODO

## Code Quality Issues

TODO

## Potential Bugs / Risks

TODO

## Missing Tests

TODO

## Required Fixes

None yet.

## Fail Path Required Fixes

Use this section only when Review Outcome = FAIL.

- TODO

## Recommended Improvements

TODO

## Follow-up Tasks

TODO

## Pass Path Finalization Summary

Use this section only when Review Outcome = PASS.

| Item | Status | Evidence |
|---|---|---|
| Validation passed | TODO | - |
| Local implementation commit created | TODO | - |
| Push skipped or approved | TODO | - |
| Next brief prepared | TODO | - |
| Next board prepared | TODO | - |
| Planning docs commit created | TODO | - |

## Git Finalization Readiness

| Check | Status | Evidence |
|---|---|---|
| Brief satisfied | TODO | - |
| Required Fixes cleared | TODO | - |
| Tests/checks run | TODO | - |
| Progress docs updated | TODO | - |
| Agent board updated | TODO | - |
| Secrets absent from diff | TODO | - |
| Local commit created | TODO | - |
| Push approved | TODO | Not required by default |

## Next Agent State After Review

If Review Outcome = FAIL:

- Phase: `CLAUDE_FIXING`
- Owner: `CLAUDE_CODE`

If Review Outcome = PASS and Codex executes One-Shot Review-Finalize-Next:

- Create local implementation commit.
- Prepare next 08 and 12.
- Create planning docs commit.
- Phase: `CLAUDE_IMPLEMENTING`
- Owner: `CLAUDE_CODE`

If Review Outcome = PASS but user wants to stop:

- Phase: `USER_ACCEPTANCE`
- Owner: `USER`
