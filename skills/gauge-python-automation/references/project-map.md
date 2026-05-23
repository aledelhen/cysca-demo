# Project Map

## Layout

- `specs/`: Gauge specifications
- `step_impl/`: Gauge Python step definitions
- `manifest.json`: Gauge project manifest
- `.venv/`: project-local Python environment
- `logs/gauge.log`: Gauge runtime log

## Working rules

- Run single specs from `specs/` with `gauge run <spec_name>`.
- Run Gauge from a shell where `.venv/bin` is on `PATH`.
- If the sandbox blocks Gauge startup, use escalated execution instead of rewriting the spec to compensate.
- Use `getgauge.python` for step definitions.
- If Gauge fails, inspect `logs/gauge.log` before changing code.
- Keep the repo focused on test automation, not agent metadata.
