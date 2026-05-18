# Contributing

Thank you for your interest in Dual Agent Project Initializer.

## Development setup

```bash
python -m pip install -e .[dev]
ruff check .
pytest -q
python scripts/compile_release.py
```

## Template editing

Edit real template files under:

```text
src/dual_agent_initializer/templates/
```

Do not edit generated `dist/init-agent-project.py` directly. It is produced by:

```bash
python scripts/compile_release.py
```

## Pull request checklist

- Keep short-term `12_AGENT_BOARD.md` content separate from long-term workflow rules.
- If changing workflow rules, check whether `AGENTS.md`, `CLAUDE.md`, `02_LOCKED_REQUIREMENTS.md`, `11_AGENT_STATE.md`, and `13_CHANGE_CONTROL.md` need synchronized changes.
- Run tests and compile the release script.
- Do not commit `.env`, tokens, credentials, or private project data.

## Suggested contributions

- more project templates;
- better Change Request workflows;
- stronger validation scripts;
- more examples;
- additional agent integrations;
- documentation translations.
