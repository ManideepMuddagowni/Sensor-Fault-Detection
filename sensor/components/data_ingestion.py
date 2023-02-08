import os
import sys

from pandas import DataFrame
from sklearn.model_selection import train_test_split

from sensor.constant.training_pipeline import SCHEMA_DROP_COLS, SCHEMA_FILE_PATH
from sensor.entity.artifact_entity import DataIngestionArtifact
from sensor.entity.config_entity import DataIngestionConfig
from sensor.exception import SensorException
from sensor.data_access.sensor_data import SensorData
from sensor.logger import logging


class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig = DataIngestionConfig()):
        try:
            self.data_ingestion_config = data_ingestion_config

        except Exception as e:
            raise SensorException(e, sys)

    def export_data_into_feature_store(self) -> DataFrame:
        try:
            logging.info("Exporting data into feature store")
            sensor_data = SensorData()
            dataframe = sensor_data.export_collection_as_dataframe(collection_name=self.data_ingestion_config.collection_name)
        except Exception as e:
            raise SensorException(e, sys)

    def split_data_as_train_test(self, dataframe: DataFrame) -> None:
        """
        Method Name :   split_data_as_train_test
        Description :   This method splits the dataframe into train set and test set based on split ratio 
        
        Output      :   Folder is created in s3 bucket
        On Failure  :   Write an exception log and then raise an exception
        
        Version     :   1.2
        Revisions   :   moved setup to cloud
        """

        try:
            pass

        except Exception as e:
            raise SensorException(e, sys)

    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        """
        Method Name :   initiate_data_ingestion
        Description :   This method initiates the data ingestion components of training pipeline 
        
        Output      :   train set and test set are returned as the artifacts of data ingestion components
        On Failure  :   Write an exception log and then raise an exception
        
        Version     :   1.2
        Revisions   :   moved setup to cloud
        """
        logging.info("Entered initiate_data_ingestion method of Data_Ingestion class")

        try:
            dataframe = self.export_data_into_feature_store()

            logging.info("Got the data from mongodb")

            self.split_data_as_train_test(dataframe)

            logging.info("Performed train test split on the dataset")

            logging.info(
                "Exited initiate_data_ingestion method of Data_Ingestion class"
            )

            data_ingestion_artifact = DataIngestionArtifact(
                trained_file_path=self.data_ingestion_config.training_file_path,
                test_file_path=self.data_ingestion_config.testing_file_path,
            )

            logging.info(f"Data ingestion artifact: {data_ingestion_artifact}")

            return data_ingestion_artifact

        except Exception as e:
            raise SensorException(e, sys)