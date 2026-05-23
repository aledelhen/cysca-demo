# Project Map

## Layout

- `specs/`: Gauge specifications
- `step_impl/`: Gauge Python step definitions
- `manifest.json`: Gauge project manifest
- `.venv/`: project-local Python environment
- `logs/gauge.log`: Gauge runtime log

## Working rules

- Run Gauge from a shell where `.venv/bin` is on `PATH`.
- Use `getgauge.python` for step definitions.
- If Gauge fails, inspect `logs/gauge.log` before changing code.
- Keep the repo focused on test automation, not agent metadata.
