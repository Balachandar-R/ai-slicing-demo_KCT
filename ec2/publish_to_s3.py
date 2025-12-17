import os
import time
import json
import uuid
import boto3
from telemetry_generator import generate_telemetry

REGION = os.getenv("AWS_REGION", "us-east-1")
BUCKET = os.getenv("TELEMETRY_BUCKET", "slice-telemetry-demo")
s3 = boto3.client("s3", region_name=REGION)

def upload_record(record):
    key = f"telemetry/{int(time.time())}-{uuid.uuid4().hex}.json"
    s3.put_object(Bucket=BUCKET, Key=key, Body=json.dumps(record).encode("utf-8"))
    print(f"Uploaded: s3://{BUCKET}/{key}")

if __name__ == "__main__":
    for i in range(50):
        rec = generate_telemetry(slice_id=f"slice-{i%3}")
        upload_record(rec)
        time.sleep(0.5)