#!/usr/bin/env bash
set -euo pipefail

# Edit these before running:
ACCOUNT_ID=${ACCOUNT_ID:-"<YOUR_AWS_ACCOUNT_ID>"}
LAMBDA_EXEC_ROLE=${LAMBDA_EXEC_ROLE:-"<YOUR_LAMBDA_ROLE_NAME>"} # e.g., ai-slicing-lambda-role
REGION=${AWS_REGION:-us-east-1}
FUNC=${LAMBDA_FUNCTION_NAME:-slice-alloc-inference}
MODELS_BUCKET=${MODELS_BUCKET:-slice-models-demo}
MODEL_KEY=${MODEL_KEY:-alloc_model.pkl}
DDB_TABLE=${DYNAMODB_TABLE:-slice_state}

pushd lambda
./build_zip.sh
popd

ROLE_ARN="arn:aws:iam::$ACCOUNT_ID:role/$LAMBDA_EXEC_ROLE"

# Try create, else update code
aws lambda create-function \
  --function-name "$FUNC" \
  --runtime python3.11 \
  --role "$ROLE_ARN" \
  --handler handler.lambda_handler \
  --timeout 10 \
  --memory-size 256 \
  --environment "Variables={AWS_REGION=$REGION,MODELS_BUCKET=$MODELS_BUCKET,MODEL_KEY=$MODEL_KEY,TABLE_NAME=$DDB_TABLE}" \
  --zip-file fileb://lambda/lambda.zip || \
aws lambda update-function-code --function-name "$FUNC" --zip-file fileb://lambda/lambda.zip

echo "Lambda deployed: $FUNC (region: $REGION)"
