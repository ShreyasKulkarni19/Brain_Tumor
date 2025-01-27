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

    def create_s3_client(self):
        return boto3.client(
            "s3",
            # region_name="us-east-1",
            region_name=self.config.region,
            aws_access_key_id=self.config.access_key,
            aws_secret_access_key=self.config.secret_key,
            
        )

    # def download_data(self):
    #     bucket_name = self.config.bucket_name
    #     file_key = self.config.file_key
    #     local_data_file = self.config.local_data_file
    #     os.makedirs(os.path.dirname(local_data_file), exist_ok=True)
    #     self.s3_client.download_file(bucket_name, file_key, local_data_file)
    def download_data(self):
        bucket_name = self.config.bucket_name
        folder_key = self.config.file_key  # This should be the folder prefix, e.g., 'brain/training/'
        local_folder = self.config.local_data_file  # Local folder to save files

        # Ensure the local directory exists
        os.makedirs(local_folder, exist_ok=True)

        # List all objects with the given prefix (folder_key)
        response = self.s3_client.list_objects_v2(Bucket=bucket_name, Prefix=folder_key)

        # Check if the folder has any contents
        if 'Contents' in response:
            for obj in response['Contents']:
                file_key = obj['Key']  # The full S3 key of the file
                file_name = os.path.relpath(file_key, folder_key)  # Relative file path
                local_file_path = os.path.join(local_folder, file_name)  # Local file path

                # Create necessary directories for nested files
                os.makedirs(os.path.dirname(local_file_path), exist_ok=True)

                # Download the file
                self.s3_client.download_file(bucket_name, file_key, local_file_path)
                print(f"Downloaded: {file_key} to {local_file_path}")
        else:
            print(f"No files found in folder: {folder_key}")

