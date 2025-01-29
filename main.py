from src.cnnClassifier import logger
# from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline

# STAGE_NAME = "Data Ingestion Stage"
# try:
#     logger.info(f"Starting {STAGE_NAME}...")
#     pipeline = DataIngestionTrainingPipeline()
#     pipeline.main()
#     logger.info(f"{STAGE_NAME} completed successfully.")
# except Exception as e:
#     logger.exception(e)
#     raise e

STAGE_NAME = "Prepare Base Model"
try:
    logger.info(f"Starting {STAGE_NAME}...")
    pipeline = PrepareBaseModelTrainingPipeline()
    pipeline.main()
    logger.info(f"{STAGE_NAME} completed successfully.")
except Exception as e:
    logger.exception(e)
    raise e