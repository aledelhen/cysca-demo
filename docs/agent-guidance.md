# Agent Guidance

This repository is a Gauge + Python automation project for Cysca-style QA demos.

## Current conventions

- Specs live in `specs/`
- Step implementations live in `step_impl/`
- The Gauge manifest is `manifest.json`
- Use the project virtual environment in `.venv/`
- The step decorator comes from `getgauge.python`

## How to run tests

From the project root, make sure the venv is active or on `PATH`, then run:

```bash
gauge run specs
```

To run a single scenario file:

```bash
cd specs
gauge run config_reload.spec
```

## When working with the AI agent

- Prefer changes in the repo over ad hoc shell-only fixes.
- If Gauge fails, inspect `logs/gauge.log` first.
- Keep shared automation helpers outside the specs.
- Use the repo-local skill source in `skills/gauge-python-automation/` as the canonical agent guidance.
- Keep the repo focused on test automation and handoff documentation, not agent-specific noise.

## GoCD material note

- The GoCD pipeline polls `file:///tmp/gocd-repos/demo.git` as a bare mirror, not the working tree in `/home/alaa/Apps/demo`.
- The repo scripts and post-commit hook bootstrap that mirror automatically so local commits can be pushed into the material GoCD watches.
- If you are reviewing pipeline behavior, remember that material polling happens before the job scripts run.
