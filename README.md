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
- `scripts/`: helper scripts for sync, Docker, and skill installation
- `env/`: Gauge environment config
- `skills/`: repo-local Codex skill sources and references

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

The repository is configured with a local `post-commit` hook that pushes commits to the `local` bare repository automatically.

Manual sync uses the configured local remote URL:

```bash
./scripts/sync-local.sh
```

The helper scripts will create the bare repository on demand, but you can also prepare it manually:

```bash
mkdir -p /tmp/gocd-repos
git init --bare /tmp/gocd-repos/demo.git
```

## Codex Skills

Install the repo skill into your local Codex home:

```bash
./scripts/install-codex-skill.sh
```

Install the Cysca QA skill into your local Codex home:

```bash
./scripts/install-cysca-qa-skill.sh
```
