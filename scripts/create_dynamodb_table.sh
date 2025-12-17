#!/usr/bin/env bash
set -e

TABLE=${DYNAMODB_TABLE:-slice_state}

aws dynamodb create-table \
  --table-name "$TABLE" \
  --attribute-definitions AttributeName=slice_id,AttributeType=S \
  --key-schema AttributeName=slice_id,KeyType=HASH \
  --billing-mode PAY_PER_REQUEST || true

echo "DynamoDB table ready: $TABLE"