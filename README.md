# Cysca Demo

This repository is a Gauge + Python automation demo tailored to Cysca-style complex systems QA work.

It is intended to show:

- how we structure executable specs around system behavior
- how we keep step logic small and testable
- how we document setup and execution for local, Docker, and pipeline use
- how we connect test automation to risk-based QA thinking

## Repository Map

- `specs/`: Gauge specifications
- `step_impl/`: Python step definitions and supporting domain helpers
- `docs/`: handoff documentation for reviewers and interviewers
- `diagrams/`: Mermaid flows that mirror the specs
- `scripts/`: shell helpers for runtime and skill installation
- `env/`: Gauge environment config
- `skills/`: repo-local Codex skill sources and references

## Script Guide

- Required runtime entrypoint: `scripts/entrypoint.sh`
- Optional pipeline helper: `scripts/run-gocd.sh`
- Developer convenience: `scripts/install-codex-skill.sh`
- Developer convenience: `scripts/install-cysca-qa-skill.sh`

## Prerequisites

- Python 3.12
- `pip`
- Gauge CLI
- Docker and Docker Compose for containerized runs
- `direnv` if you want automatic local venv activation

## Local Setup

1. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

1. Install Python dependencies:

```bash
pip install -r requirements.txt
```

1. Install Gauge if it is not already available on your PATH.
1. Run the specs from the project root:

```bash
gauge run specs
```

To run a single spec:

```bash
cd specs
gauge run config_reload.spec
```

If a Gauge run fails, inspect `logs/gauge.log` first.

## Validation Coverage

Current specs cover the main reference flows:

- `device_handshake.spec`
- `system_boot.spec`
- `config_reload.spec`
- `fault_recovery.spec`
- `telemetry_trace.spec`

The matching Mermaid diagrams live in `diagrams/`.

## GoCD Pipeline

This repository is designed to run in GoCD as well as locally. The pipeline uses the same test entrypoint as the manual run, so the behavior stays aligned between developer machines and the CI agent.

GoCD should watch the GitHub repository directly rather than a local bare mirror. That keeps the pipeline source aligned with the real upstream repo and avoids a separate mirror bootstrap step.

Run the pipeline entrypoint directly:

```bash
./scripts/run-gocd.sh
```

That script starts the stack, runs the specs, and tears the containers down afterward.

GoCD prerequisites:

- the pipeline workspace at `/var/lib/go-agent/pipelines/demo_suite` must be owned by the `go` user
- the checkout must be clean before the job starts
- Docker must be available to the agent

If you are reviewing the project from the pipeline side, this is the execution path to follow first.

## Framework Choice

If you need the rationale for using Gauge instead of Robot Framework in this repository, see [docs/gauge-vs-robot-framework.md](/home/alaa/Apps/demo/docs/gauge-vs-robot-framework.md).

## Docker

Build the image:

```bash
docker build -t cysca-mock .
```

Run the full suite:

```bash
docker run --rm cysca-mock
```

Run a specific spec:

```bash
docker run --rm cysca-mock gauge run specs/config_reload.spec
```

## Docker Compose

Build and run the full suite:

```bash
docker compose up --build
```

Run a specific spec:

```bash
docker compose run --rm cysca-mock gauge run specs/config_reload.spec
```

## Git Sync

The repository uses the normal GitHub `origin` remote. Push changes with your standard Git workflow, for example `git push origin <branch>`.

## Codex Skills

Install the repo skill into your local Codex home:

```bash
./scripts/install-codex-skill.sh
```

Install the Cysca QA skill into your local Codex home:

```bash
./scripts/install-cysca-qa-skill.sh
```
