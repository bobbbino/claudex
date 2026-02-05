#!/bin/sh
set -e

# Replace build-time placeholders with runtime env vars
if [ -n "$VITE_API_BASE_URL" ]; then
  find /usr/share/nginx/html -name '*.js' -exec sed -i "s|__VITE_API_BASE_URL__|${VITE_API_BASE_URL}|g" {} +
fi
if [ -n "$VITE_WS_URL" ]; then
  find /usr/share/nginx/html -name '*.js' -exec sed -i "s|__VITE_WS_URL__|${VITE_WS_URL}|g" {} +
fi

exec "$@"
