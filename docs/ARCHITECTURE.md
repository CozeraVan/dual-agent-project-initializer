# Architecture

This repository intentionally keeps template content as normal files instead of embedding thousands of lines of Markdown into a giant Python dictionary.

## Source Layout

```text
dual-agent-project-initializer/
├── init-agent-project.py              # repo-friendly wrapper
├── init-agent-project.sh              # macOS/Linux wrapper
├── init-agent-project.ps1             # Windows PowerShell wrapper
├── src/dual_agent_initializer/cli.py   # initializer runtime
├── src/dual_agent_initializer/templates/
│   ├── AGENTS.md
│   ├── CLAUDE.md
│   ├── docs/agent/00-13...
│   ├── scripts/...
│   └── .claude / .agents / .codex ...
├── scripts/compile_release.py          # builds dist/init-agent-project.py
└── tests/test_initializer.py
```

## Why templates are real files

Real template files make the project easier to maintain:

- Markdown files get syntax highlighting and preview.
- Diffs are readable.
- Contributors can update one template without editing a huge Python string.
- The release compiler can still produce a single-file standalone script for users who want one file only.

## Runtime flow

1. The CLI loads all files under `src/dual_agent_initializer/templates/`.
2. Files are rendered with the target project name.
3. Existing files are backed up under `.agent-backups/<timestamp>/` before overwrite.
4. Git is initialized if needed.
5. A pre-commit hook is written after Git initialization.
6. The generated workflow files are staged and optionally committed.

## Release flow

Run:

```bash
python scripts/compile_release.py
```

This creates:

```text
dist/init-agent-project.py
```

The release script embeds the current templates, so it can be copied and run without the full repository.
