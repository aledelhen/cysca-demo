#!/bin/sh
set -eu

export HOME=/home/go
export PYTHONPATH=/workspace
export GAUGE_PYTHON_COMMAND="${GAUGE_PYTHON_COMMAND:-/app/.venv/bin/python}"

cd /workspace
exec gauge run specs --env docker --log-level debug
