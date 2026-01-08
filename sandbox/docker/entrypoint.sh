#!/bin/bash

# Start VNC services in background
start-vnc.sh &

# Start IDE server in background
openvscode-server --host 0.0.0.0 --port ${OPENVSCODE_PORT:-8765} --without-connection-token --disable-telemetry &

# Wait for VNC services to be ready (ports 5900 and 6080)
for i in {1..15}; do
    if ss -tuln 2>/dev/null | grep -q ':5900' && ss -tuln 2>/dev/null | grep -q ':6080'; then
        break
    fi
    sleep 1
done

# Execute the main command (default: bash)
exec "$@"
