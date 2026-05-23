# Agent Guidance

This repository is a Gauge + Python automation project.

## Current conventions

- Specs live in `specs/`
- Step implementations live in `step_impl/`
- The Gauge manifest is `manifest.json`
- Use the project virtual environment in `.venv/`
- The step decorator comes from `getgauge.python`

## How to run tests

From the project root, make sure the venv is active or on `PATH`, then run:

```bash
cd specs
gauge run example.spec
```

You can also use the Makefile from the project root:

```bash
make test
make install-skill
```

## When working with the AI agent

- Prefer changes in the repo over ad hoc shell-only fixes.
- If Gauge fails, inspect `logs/gauge.log` first.
- Keep shared automation helpers outside the specs.
- Use the repo-local skill source in `skills/gauge-python-automation/` as the canonical agent guidance.
