#!/bin/bash

DISPLAY_NUM=${DISPLAY_NUM:-99}
VNC_PORT=${VNC_PORT:-5900}
WS_PORT=${WS_PORT:-6080}
RESOLUTION=${RESOLUTION:-1920x1080x24}

export DISPLAY=:${DISPLAY_NUM}

cleanup_stale() {
    pkill -f "Xvfb :${DISPLAY_NUM}" 2>/dev/null
    pkill -f "x11vnc.*:${DISPLAY_NUM}" 2>/dev/null
    pkill -f "websockify.*${WS_PORT}" 2>/dev/null
}

if pgrep -f "Xvfb :${DISPLAY_NUM}" > /dev/null; then
    echo "VNC services already running"
    exit 0
fi

cleanup_stale

echo "Starting Xvfb on display :${DISPLAY_NUM}..."
Xvfb :${DISPLAY_NUM} -screen 0 ${RESOLUTION} &
XVFB_PID=$!
sleep 1

if ! kill -0 $XVFB_PID 2>/dev/null; then
    echo "Failed to start Xvfb"
    exit 1
fi

echo "Starting x11vnc on port ${VNC_PORT}..."
x11vnc -display :${DISPLAY_NUM} -forever -shared -nopw -listen 0.0.0.0 -rfbport ${VNC_PORT} -bg

# Wait for x11vnc to be listening before starting websockify
for i in {1..10}; do
    if ss -tuln | grep -q ":${VNC_PORT}"; then
        echo "x11vnc ready on port ${VNC_PORT}"
        break
    fi
    sleep 1
done

echo "Starting websockify on port ${WS_PORT}..."
websockify 0.0.0.0:${WS_PORT} 127.0.0.1:${VNC_PORT} &
WEBSOCKIFY_PID=$!
sleep 1

if ! kill -0 $WEBSOCKIFY_PID 2>/dev/null; then
    echo "Failed to start websockify"
    exit 1
fi

# Verify both ports are connectable before exiting
for i in {1..10}; do
    if ss -tuln | grep -q ":${VNC_PORT}" && ss -tuln | grep -q ":${WS_PORT}"; then
        echo "VNC services ready"
        exit 0
    fi
    sleep 1
done

echo "VNC services failed to become ready"
exit 1
