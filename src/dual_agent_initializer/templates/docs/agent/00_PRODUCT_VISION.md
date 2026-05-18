# Product Vision

Project name: {{PROJECT_NAME}}

## Long-Term Vision

TODO: Describe the long-term goal of this project.

## What This Project Is

TODO: Describe the system/product/research project.

## What This Project Is Not

TODO: Describe boundaries and non-goals.

## Target Users / Operators

TODO: Describe who will use or maintain this project.

## Core Principles

- Preserve working behavior.
- Prefer incremental changes.
- Keep architecture understandable.
- Make important decisions explicit.
- Keep implementation and review separated when using dual agents.
- Do not rely on chat history as the only source of truth.

## Dual-Agent Development Philosophy

This project uses Codex and Claude Code together:

- Codex brainstorms with the user and converts ideas into structured change requests or implementation briefs.
- Claude Code implements the approved brief.
- Codex reviews the implementation and performs local git checkpoints after review passes.
- User remains the final product owner and acceptance authority.
