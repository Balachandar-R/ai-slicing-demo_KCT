import pandas as pd, joblib, boto3
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv("sample_data.csv")
X = df[["traffic","latency","jitter","slice_type"]]
y = df[["bandwidth","cpu","memory"]]

model = RandomForestRegressor()
model.fit(X, y)

joblib.dump(model, "alloc_model.pkl")
s3 = boto3.client("s3")
s3.upload_file("alloc_model.pkl", "slice-models-demo", "alloc_model.pkl")
print("Model uploaded to S3")
