# {{PROJECT_NAME}}

TODO: Describe this project.

## Agent Workflow

This repository was initialized with Dual Agent Project Initializer.


This project uses a dual-agent workflow:

1. Codex brainstorms with the user and initializes project goals, architecture, todo list, and first implementation brief.
2. Claude Code implements the active brief and writes `docs/agent/09_CODING_HANDOFF.md`.
3. Codex reviews and writes `docs/agent/10_REVIEW_REPORT.md`.
4. If review fails, Codex writes Required Fixes to `10` and `12`, then returns work to Claude Code without committing.
5. If review passes, Codex creates a local git checkpoint, does not push by default, prepares the next `08` and `12`, and hands work back to Claude Code.
6. New ideas and architecture changes follow `docs/agent/13_CHANGE_CONTROL.md`.

Short commands:

- Claude Code: `请读取 11 和 12，执行当前 Claude Code 任务。`
- Codex: `请读取 11 和 12，执行 One-Shot Review-Finalize-Next。`
- New idea: `请读取 11 和 12，把以下新 idea 作为 Change Request 分析，不改代码。`
- Architecture change: `请进入 Architecture Change Mode，读取 11、12、13，对以下架构变更做影响分析，不改业务代码。`
