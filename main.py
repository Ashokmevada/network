from src.network.components.data_ingestion import DataIngestion
from src.network.entity.config_entity import DataIngestionConfig , TrainingPipelineConfig
from src.network.logging.logger import logging



if __name__ == "__main__":

    training_pipeline_config = TrainingPipelineConfig()
    data_ingestion_config = DataIngestionConfig(training_pipeline_config)
    data_ingestion = DataIngestion(data_ingestion_config)
    
    logging.info("Initiated Data Ingestion Completed")
    data_ingestion_artifacts =data_ingestion.initiate_data_ingestion()
    logging.info("Completed Data Ingestion")
    print(data_ingestion_artifacts)
