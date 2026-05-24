FROM python:3.11-slim

ENV DEBIAN_FRONTEND=noninteractive \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    HOME=/home/go

RUN apt-get update \
    && apt-get install -y --no-install-recommends curl gnupg ca-certificates unzip nodejs npm \
    && rm -rf /var/lib/apt/lists/*

RUN npm install -g @getgauge/cli

WORKDIR /app

COPY requirements.txt .
RUN python -m venv /app/.venv \
    && /app/.venv/bin/pip install --no-cache-dir -r requirements.txt

RUN mkdir -p /home/go/.gauge/config /home/go/.gauge/plugins /home/go/.gauge/logs \
    && cat > /home/go/.gauge/config/gauge.properties <<'EOF'
# Version 1.6.21
# This file contains Gauge specific internal configurations. Do not delete

# Allow Gauge to download template from insecure URLs.
allow_insecure_download = false

# Allow Gauge and its plugin updates to be notified.
check_updates = true

# Url to get plugin versions
gauge_repository_url = https://downloads.gauge.org/plugin

# Timeout in milliseconds for requests from runner when invoked for ide.
ide_request_timeout = 30000

# Timeout in milliseconds for making a connection to plugins.
plugin_connection_timeout = 10000

# Timeout in milliseconds for a plugin to stop after a kill message has been sent.
plugin_kill_timeout = 4000

# Timeout in milliseconds for making a connection to the language runner.
runner_connection_timeout = 30000

# Timeout in milliseconds for requests from the language runner.
runner_request_timeout = 30000
EOF
RUN chown -R 997:984 /home/go

COPY . .
RUN chmod +x /app/scripts/entrypoint.sh

ENTRYPOINT ["/app/scripts/entrypoint.sh"]
