from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: str 
    local_data_file: str 
    bucket_name: str
    region: str
    access_key: str
    secret_key: str
    file_key: str
        