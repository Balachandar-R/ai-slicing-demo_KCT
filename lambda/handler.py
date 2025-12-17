import os
import json
import boto3
import joblib

REGION = os.getenv("AWS_REGION", "us-east-1")
MODELS_BUCKET = os.getenv("MODELS_BUCKET", "slice-models-demo")
MODEL_KEY = os.getenv("MODEL_KEY", "alloc_model.pkl")
DDB_TABLE = os.getenv("TABLE_NAME", "slice_state")

_s3 = boto3.client("s3", region_name=REGION)
_ddb = boto3.client("dynamodb", region_name=REGION)
_model = None

def load_model():
    global _model
    if _model is None:
        obj = _s3.get_object(Bucket=MODELS_BUCKET, Key=MODEL_KEY)
        _model = joblib.load(obj["Body"])
    return _model

def lambda_handler(event, context):
    body = event.get("body")
    payload = json.loads(body) if isinstance(body, str) else event

    features = [[
        float(payload.get("traffic", 100)),
        float(payload.get("latency", 10)),
        float(payload.get("jitter", 2)),
        int(payload.get("slice_type", 0))
    ]]

    model = load_model()
    alloc = model.predict(features)[0]
    resp = {
        "bandwidth": float(alloc[0]),
        "cpu": float(alloc[1]),
        "memory": float(alloc[2])
    }

    try:
        _ddb.put_item(
            TableName=DDB_TABLE,
            Item={
                "slice_id": {"S": payload.get("slice_id", "demo")},
                "last_alloc": {"S": json.dumps(resp)},
                "ts": {"N": str(payload.get("ts", 0))}
            }
        )
    except Exception as e:
        print("DDB error:", e)

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(resp)
    }
