#!/bin/bash

set -e  # Exit on error

# -------------------------
# 1. Install LiveKit CLI
# -------------------------

LK_VERSION="2.4.9"
LK_TAR="lk_${LK_VERSION}_linux_amd64.tar.gz"
LK_URL="https://github.com/livekit/livekit-cli/releases/download/v${LK_VERSION}/${LK_TAR}"
INSTALL_DIR="/usr/local/bin"

echo "Downloading LiveKit CLI v${LK_VERSION}..."
wget -q "$LK_URL" -O "/tmp/${LK_TAR}"

echo "Extracting..."
tar -xzf "/tmp/${LK_TAR}" -C /tmp

echo "Installing to ${INSTALL_DIR}..."
sudo mv /tmp/lk "${INSTALL_DIR}/lk"
sudo chmod +x "${INSTALL_DIR}/lk"

rm "/tmp/${LK_TAR}"

echo "Installed version:"
lk --version

# -------------------------
# 2. Start Docker Compose (root)
# -------------------------

#echo "Starting Docker Compose services in monorepo root..."
#docker compose up -d

# -------------------------
# 3. Start Docker Compose (langfuse)
# -------------------------

if [ -d "langfuse" ]; then
  echo "Starting Docker Compose services in langfuse..."
  (cd langfuse && docker compose up -d)
else
  echo "Directory 'langfuse' does not exist. Skipping 'langfuse' docker compose."
fi

echo "All setup complete!"

