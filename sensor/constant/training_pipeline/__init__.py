import os
from sensor.constant.s3_bucket import TRAINING_BUCKET_NAME


TARGET_COLUMN = 'class'
PIPELINE_NAME: str = 'sensor'
ARTIFACT_DIR: str = 'artifact'

# common file name 

FILE_NAME: str = 'sensor.csv'

TRAIN_FILE_NAME: str = 'train.csv'
TEST_FILE_NAME: str = 'test.csv'


PREPROCESSING_OBJECT_FILE_NAME = 'preprocessing.pkl'
MODEL_NAME = 'model.pkl'
SCHEMA_FILE_PATH = os.path.join('congig', 'schema.yaml')

## we will drop unwanted data using config folder with schema.yaml file 
# will call drop_columns in schema.yaml file

SCHEMA_DROP_COLS = "drop_columns"

## Data Ingestion related constant start with DATA_INGESTION VAR NAME

