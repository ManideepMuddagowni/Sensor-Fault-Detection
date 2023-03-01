import os
from sensor.constant.s3_bucket import TRAINING_BUCKET_NAME


TARGET_COLUMN = 'class'
PIPELINE_NAME: str = 'sensor'
ARTIFACT_DIR: str = 'artifact'

# common file name for training pipeline

FILE_NAME: str = 'sensor.csv'

TRAIN_FILE_NAME: str = 'train.csv'
TEST_FILE_NAME: str = 'test.csv'


PREPROCESSING_OBJECT_FILE_NAME = 'preprocessing.pkl'
MODEL_NAME = 'model.pkl'
SCHEMA_FILE_PATH = os.path.join('congig', 'schema.yaml')

## we will drop unwanted data using config folder with schema.yaml file 
## will call drop_columns in schema.yaml file

SCHEMA_DROP_COL = "drop_columns"

## Data Ingestion related constant start with DATA_INGESTION VAR NAME

'''
Import the data from the mongo db with the collection name
'''
DATA_INGESTION_COLLECTION_NAME: str = 'sensor'
'''
Export that data from the mongo db to feature store
'''
DATA_INGESTION_DIR_NAME: str = 'data_ingestion'

DATA_INGESTION_FEATURE_STORE: str = 'feature_store'

'''
Dividing the data into train test split and store it in the ingested folder
'''
DATA_INGESTION_INGESTED_DIR: str = 'ingested'

DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = '0.2'


