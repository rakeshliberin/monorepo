#!/bin/bash

set -e  # Exit on error

# Variables
LK_VERSION="2.4.9"
LK_TAR="lk_${LK_VERSION}_linux_amd64.tar.gz"
LK_URL="https://github.com/livekit/livekit-cli/releases/download/v${LK_VERSION}/${LK_TAR}"
INSTALL_DIR="/usr/local/bin"

# Download
echo "Downloading LiveKit CLI v${LK_VERSION}..."
wget -q "$LK_URL" -O "/tmp/${LK_TAR}"

# Extract
echo "Extracting..."
tar -xzf "/tmp/${LK_TAR}" -C /tmp

# Move binary to /usr/local/bin
echo "Installing to ${INSTALL_DIR}..."
sudo mv /tmp/lk "${INSTALL_DIR}/lk"
sudo chmod +x "${INSTALL_DIR}/lk"

# Clean up
rm "/tmp/${LK_TAR}"

# Verify
echo "Installed version:"
lk --version

