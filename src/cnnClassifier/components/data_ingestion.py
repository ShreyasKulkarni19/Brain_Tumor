import os
import boto3
import yaml
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
from cnnClassifier.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
        self.s3_client = self.create_s3_client()

    # def read_config(self, config_path):
    #     with open(config_path, "r") as f:
    #         config = yaml.safe_load(f)
    #     return config["data_ingestion"]

    # def create_s3_client(self):
    #     return boto3.client(
    #         "s3",
    #         region_name=self.config["region"],
    #         aws_access_key_id=self.config["access_key"],
    #         aws_secret_access_key=self.config["secret_key"],
    #     )

    # def download_data(self):
    #     bucket_name = self.config["bucket_name"]
    #     file_key = self.config["file_key"]
    #     local_data_file = self.config["local_data_file"]
    #     os.makedirs(os.path.dirname(local_data_file), exist_ok=True)
    #     self.s3_client.download_file(bucket_name, file_key, local_data_file)
    #     logger.info(f"Data downloaded to {local_data_file}")
    #     logger.info(f"File size: {get_size(local_data_file)}")

    def create_s3_client(self):
        return boto3.client(
            "s3",
            region_name=self.config.region,
            aws_access_key_id=self.config.access_key,
            aws_secret_access_key=self.config.secret_key,
        )

    def download_data(self):
        bucket_name = self.config.bucket_name
        file_key = self.config.file_key
        local_data_file = self.config.local_data_file
        os.makedirs(os.path.dirname(local_data_file), exist_ok=True)
        self.s3_client.download_file(bucket_name, file_key, local_data_file)
