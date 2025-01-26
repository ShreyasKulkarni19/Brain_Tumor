
import yaml
import boto3
import os

def download_data():
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)

    data_cfg = config["data_ingestion"]
    bucket_name = data_cfg["bucket_name"]
    region = data_cfg["region"]
    access_key = data_cfg["access_key"]
    secret_key = data_cfg["secret_key"]
    file_key = data_cfg["file_key"]
    local_data_file = data_cfg["local_data_file"]

    os.makedirs(os.path.dirname(local_data_file), exist_ok=True)

    s3 = boto3.client(
        "s3",
        region_name=region,
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
    )

    s3.download_file(bucket_name, file_key, local_data_file)
    print(f"Data downloaded to {local_data_file}")

if __name__ == "__main__":
    download_data()