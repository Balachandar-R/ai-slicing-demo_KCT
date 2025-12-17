#!/usr/bin/env bash
set -e

echo "Use AWS Console → API Gateway:"
echo "1) Create REST API"
echo "2) Resource /predict → Method POST → Lambda proxy integration"
echo "3) Stage 'dev' → Deploy"
echo "4) Test with: curl -X POST https://<api-id>.execute-api.<region>.amazonaws.com/dev/predict -H 'Content-Type: application/json' -d @api/test_request.json"