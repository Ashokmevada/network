import os
import pandas as pd
import numpy as np
import sys

"""
Some common Constant start with VAR NAME

"""
TARGET_COLUMN = "Result"
PIPELINE_NAME = "Network"
ARTIFACT_DIR = "Artifacts"
FILE_NAME = "phisingData"

TRAIN_FILE_NAME = "train.csv"
TEST_FILE_NAME = "test.csv"


"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME
"""
DATA_INGESTION_COLLECTION_NAME: str = "NetworkData"
DATA_INGESTION_DATABASE_NAME: str = "NetworkDemoData"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION: float = 0.3

