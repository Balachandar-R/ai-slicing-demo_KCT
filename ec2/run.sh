#!/usr/bin/env bash
set -euo pipefail

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

export AWS_REGION=${AWS_REGION:-us-east-1}
export TELEMETRY_BUCKET=${TELEMETRY_BUCKET:-slice-telemetry-demo}

python publish_to_s3.py
