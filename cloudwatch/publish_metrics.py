import os
import time
import random
import boto3

REGION = os.getenv("AWS_REGION", "us-east-1")
NAMESPACE = "AISlicing"
METRIC = "SliceLatency"

cw = boto3.client("cloudwatch", region_name=REGION)

def publish(latency_ms: float, slice_id: str = "embb-01"):
    cw.put_metric_data(
        Namespace=NAMESPACE,
        MetricData=[{
            "MetricName": METRIC,
            "Dimensions": [{"Name": "SliceId", "Value": slice_id}],
            "Timestamp": time.time(),
            "Value": latency_ms,
            "Unit": "Milliseconds"
        }]
    )
    print(f"Published latency={latency_ms}ms for {slice_id}")

if __name__ == "__main__":
    for _ in range(20):
        publish(latency_ms=random.uniform(10, 40))
        time.sleep(5)
