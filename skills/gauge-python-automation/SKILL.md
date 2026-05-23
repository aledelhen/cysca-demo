---
name: gauge-python-automation
description: Use when working in the Gauge + Python automation repo to understand project layout, execution conventions, step implementation patterns, and environment setup.
metadata:
  short-description: Gauge Python automation project guide
---

# Gauge Python Automation

Use this skill when working in the `~/Apps/demo` Gauge/Python project.

## Scope

This project is a Gauge test automation repo. Prefer the existing project structure and conventions over inventing new ones.

## Current project conventions

- Specs live in `specs/`
- Step implementations live in `step_impl/`
- The Gauge manifest is `manifest.json`
- Python dependencies are installed in `.venv`
- Run Gauge from a shell where `.venv/bin` is on `PATH`
- The step decorator comes from `getgauge.python`

## Execution rules

- Do not assume system `python` exists.
- Prefer the project venv over system Python.
- When a Gauge run fails, inspect `logs/gauge.log` first.
- Run specs from the `specs/` directory with `gauge run <spec_name>` when verifying a single spec.
- If the sandbox blocks Gauge from starting its local API server, rerun the command outside the sandbox rather than changing the spec first.
- If a runner import fails, fix the project import path or dependency, not the spec first.

## Step implementation pattern

- Keep steps small and explicit.
- Put shared browser/UI helpers in future `pages/` or helper modules, not in specs.
- Keep example/demo steps minimal unless the user asks for a fuller framework scaffold.

## Environment assumptions

- The repo uses `direnv` for local activation when available.
- If a terminal session is not already in the venv, activate it before running Gauge.
- Prefer repo-local, repeatable config over shell-only one-offs.

## When to read references

- Read `references/project-map.md` when you need the exact repo layout or workflow reminders.
