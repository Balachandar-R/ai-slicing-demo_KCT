import random, json

def generate_telemetry(slice_id="embb-01"):
    return {
        "slice_id": slice_id,
        "traffic": random.randint(50, 500),
        "latency": round(random.uniform(5, 50), 2),
        "jitter": round(random.uniform(1, 10), 2),
        "slice_type": random.choice([0,1,2])
    }

if __name__ == "__main__":
    print(json.dumps(generate_telemetry(), indent=2))