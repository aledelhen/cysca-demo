#!/bin/sh
set -eu

mkdir -p /home/go/.gauge/config /home/go/.gauge/plugins /home/go/.gauge/logs
chown -R 997:984 /home/go /workspace

exec gosu 997:984 sh -c 'export HOME=/home/go PYTHONPATH=/workspace GAUGE_PYTHON_COMMAND=${GAUGE_PYTHON_COMMAND:-/app/.venv/bin/python}; exec gauge run specs --env docker'
