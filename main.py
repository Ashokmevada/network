from src.network.components.data_ingestion import DataIngestion
from src.network.components.data_validation import DataValidation


from src.network.entity.config_entity import DataIngestionConfig , TrainingPipelineConfig, DataValidationConfig
from src.network.logging.logger import logging
from src.network.exception.exception import NetworkSecurityException
import sys



if __name__ == "__main__":

    try:

        training_pipeline_config = TrainingPipelineConfig()
        data_ingestion_config = DataIngestionConfig(training_pipeline_config)
        data_ingestion = DataIngestion(data_ingestion_config)    
        logging.info("Initiated Data Ingestion Completed")
        data_ingestion_artifacts =data_ingestion.initiate_data_ingestion()
        logging.info("Completed Data Ingestion")
        print(data_ingestion_artifacts)
        data_validation_config = DataValidationConfig(training_pipeline_config)
        data_validation = DataValidation(data_ingestion_artifacts,data_validation_config)
        logging.info("Initiated Data Validation")
        data_validation_artifacts = data_validation.initiate_data_validation()
        logging.info("Completed Data Validation")
        print(data_validation_artifacts)

    except Exception as e:
        raise NetworkSecurityException(e,sys)

