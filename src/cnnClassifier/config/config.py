from cnnClassifier.constants import *
from cnnClassifier.utils.common import read_yaml, create_directories
from cnnClassifier.entity.config_entity import DataIngestionConfig

class ConfigurationManager:
    def __init__(self,
                 config_file_path = CONFIG_FILE_PATH,
                 params_file_path = PARAMS_FILE_PATH):
        self.config = read_yaml(str(config_file_path))
        self.params = read_yaml(str(params_file_path))
        
        create_directories([self.config.artifacts_root])
        
    def get_data_ingestion(self)->DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            local_data_file = config.local_data_file,
            bucket_name = config.bucket_name,
            region = config.region,
            access_key = config.access_key,
            secret_key = config.secret_key,
            file_key = config.file_key
        )
        return data_ingestion_config