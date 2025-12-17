#!/usr/bin/env bash
set -euo pipefail

rm -rf build lambda.zip
mkdir -p build/python

pip install -r requirements.txt -t build/python
cp handler.py build/

cd build && zip -r ../lambda.zip .
echo "Built lambda.zip"