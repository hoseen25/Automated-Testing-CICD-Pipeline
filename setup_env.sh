#!/bin/bash
set -e

echo "========================================"
echo "🚀 [CI/CD] Starting Environment Setup..."
echo "========================================"

echo "Creating Virtual Environment (venv)..."
python3 -m venv venv

echo "Activating Environment..."
source venv/bin/activate

echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "========================================"
echo "✅ [CI/CD] Setup Complete Successfully!"
echo "========================================"