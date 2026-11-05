#!/bin/sh
# Copy source deck to index.html for GitHub Pages (root URL).
set -e
cd "$(dirname "$0")"
cp deck.html index.html
echo "Published: deck.html → index.html (commit and push to update the live link)"
