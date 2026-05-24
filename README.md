# Gauge Python Starter

Starter structure for test automation using the Gauge framework with Python.

## Layout

- `specs/` Gauge specifications
- `step_impl/` Python step definitions
- `skills/` repo-local Codex skill source
- `scripts/` helper scripts, including skill installation
- `env/` environment hooks and configuration

## Getting started

1. Create a virtual environment.
2. Install dependencies.
3. Run Gauge against the `specs/` directory.

## Git sync

This repo is configured with a local `post-commit` hook that pushes commits to the `local` bare repository automatically.

You can also sync manually with:

```bash
./scripts/sync-local.sh
```

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

Run the GoCD-style pipeline entrypoint:

```bash
./scripts/run-gocd.sh
```

Use that same script in the GoCD job so the stack starts, the specs run, and the containers are torn down afterward.

## Codex skill sync

Install the project skill into your local Codex home:

```bash
./scripts/install-codex-skill.sh
```

Install the Cysca QA skill into your local Codex home:

```bash
./scripts/install-cysca-qa-skill.sh
```
