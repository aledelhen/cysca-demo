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

## Codex skill sync

Install the project skill into your local Codex home:

```bash
./scripts/install-codex-skill.sh
```

Install the Cysca QA skill into your local Codex home:

```bash
./scripts/install-cysca-qa-skill.sh
```
