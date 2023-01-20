import datetime
import os
from sensor.constant.training_pipeline import PIPELINE_NAME, ARTIFACT_DIR
from sensor.constant import training_pipeline
from sensor.constant.training_pipeline import TRAIN_FILE_NAME, TEST_FILE_NAME, DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
from sensor.constant.training_pipeline import DATA_INGESTION_COLLECTION_NAME



class TrainingPipelineConfig:

    def __init__(self, timestamp=datetime.now()):
        timestamp = timestamp.strftime('%m_%d_%Y_%H_%M_%S')
        self.pipeline_name: str = PIPELINE_NAME
        self.artifact_dir: str = os.path.join(training_pipeline.ARTIFACT_DIR, timestamp)
        self.timestamp: str = timestamp

class DataIngestionConfig:

    def __init__(self, training_pipeline_config):
        self.data_ingestion_dir: str = os.path.join(
            training_pipeline_config.artifact_dir, training_pipeline.DATA_INGESTION_DIR
        )
        self.feature_store_file_path: str = os.path.join(
            self.data_ingestion_dir, training_pipeline.DATA_INGESTION_FEATURE_STORE_DIR, training_pipeline.FILE_NAME
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
        collection_name: str = DATA_INGESTION_COLLECTION_NAME

class DataValidationConfig:
    
    def __init__(self, data_validation_config):
        self.data_validation_dir: str = os.path.join(
            data_validation_config.artifact_dir, training_pipeline.DATA_VALIDATION_DIR
        )