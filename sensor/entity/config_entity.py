from datetime import datetime
import os
from sensor.constant.training_pipeline import PIPELINE_NAME, ARTIFACT_DIR
from sensor.constant import training_pipeline
from sensor.constant.training_pipeline import FILE_NAME, TRAIN_FILE_NAME, TEST_FILE_NAME, DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
from sensor.constant.training_pipeline import DATA_INGESTION_COLLECTION_NAME

TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")


class TrainingPipelineConfig:
    pipeline_name: str = PIPELINE_NAME

    artifact_dir: str = os.path.join(ARTIFACT_DIR, TIMESTAMP)

    timestamp: str = TIMESTAMP


training_pipeline_config: TrainingPipelineConfig = TrainingPipelineConfig()

class DataIngestionConfig:

    def __init__(self, training_pipeline_config):
        self.data_ingestion_dir: str = os.path.join(
            training_pipeline_config.artifact_dir, training_pipeline.DATA_INGESTION_DIR_NAME
        )
        self.feature_store_file_path: str = os.path.join(
            self.data_ingestion_dir, training_pipeline.DATA_INGESTION_FEATURE_STORE, FILE_NAME
        )
        self.training_file_path: str = os.path.join(
            self.data_ingestion_dir, training_pipeline.DATA_INGESTION_INGESTED_DIR, TRAIN_FILE_NAME
        )
        self.testing_file_path: str = os.path.join(
            self.data_ingestion_dir, training_pipeline.DATA_INGESTION_INGESTED_DIR, TEST_FILE_NAME
        )
        self.train_test_split_ratio: float = os.path.join(
            self.data_ingestion_dir, training_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
        )
        self.collection_name: str = training_pipeline.DATA_INGESTION_COLLECTION_NAME