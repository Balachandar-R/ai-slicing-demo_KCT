# AI-Optimized Network Slicing Demo (AWS Free Tier)

End-to-end demo using Python + AWS:
EC2 telemetry → S3 → SageMaker training → Lambda/API Gateway inference → DynamoDB → CloudWatch → QuickSight.

## Steps
1. Launch EC2 (t2.micro) → run telemetry_generator.py
2. Create S3 buckets → store telemetry + models
3. Train model in SageMaker (ml.t2.medium) → upload alloc_model.pkl
4. Deploy Lambda → load model from S3 → predict allocations
5. Expose Lambda via API Gateway → /predict endpoint
6. Store allocations in DynamoDB → slice_state table
7. Monitor SLA with CloudWatch → alarms trigger Lambda
8. Visualize KPIs in QuickSight → dashboards


## Structure 
```plaintext
ai-slicing-demo/
├─ README.md
├─ ec2/
│  ├─ telemetry_generator.py
│  ├─ publish_to_s3.py
│  ├─ requirements.txt
│  └─ run.sh
├─ sagemaker/
│  ├─ train.py
│  ├─ sample_data.csv
│  └─ requirements.txt
├─ lambda/
│  ├─ handler.py
│  ├─ requirements.txt
│  └─ build_zip.sh
├─ api/
│  ├─ openapi.json
│  └─ test_request.json
├─ dynamodb/
│  └─ schema.md
├─ cloudwatch/
│  ├─ publish_metrics.py
│  └─ requirements.txt
├─ quicksight/
│  └─ dashboard_guide.md
└─ scripts/
   ├─ create_s3_buckets.sh
   ├─ create_dynamodb_table.sh
   ├─ deploy_lambda.sh
   └─ deploy_apigw.sh
