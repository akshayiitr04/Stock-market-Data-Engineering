#Import requirements
import json
import boto3
import time
from kafka import KafkaConsumer

#Minio Connection
s3 = boto3.client(
    "s3",
    endpoint_url="http://localhost:9002",
    aws_access_key_id="admin",
    aws_secret_access_key="password123"
)

bucket_name = "bronze-transactions"

# Ensure bucket exists (idempotent)
try:
    s3.head_bucket(Bucket=bucket_name)
    print(f"Bucket {bucket_name} already exists.")
except Exception:
    s3.create_bucket(Bucket=bucket_name)
    print(f"Created bucket {bucket_name}.")

#Define Consumer
consumer = KafkaConsumer(
    "stock-quotes",
    bootstrap_servers=["localhost:29092"], # Use localhost for external access
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="stock-group",
    value_deserializer=lambda v: json.loads(v.decode("utf-8")),
    api_version=(7, 4, 1) # Explicitly set version to match your Docker image
)

print("Consumerstreaming and saving to MinIO...")

#Main Function
for message in consumer:
    record = message.value
    symbol = record.get("symbol", "unknown")
    ts = record.get("fetched_at",int(time.time()))
    key = f"{symbol}/{ts}.json"

    s3.put_object(
        Bucket=bucket_name,
        Key=key,
        Body=json.dumps(record),
        ContentType="application/json"
    )
    print(f"Saved record for {symbol} = s3://{bucket_name}/{key}")
                    