from Classifier import logger
from Classifier.pipeline.data_ingestion_pipeline01 import DataIngestionPipeline

Stage_name= 'DATA INGESTION'
try:
        logger.info(f">>>>>> stage {Stage_name} started <<<<<<")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f">>>>>> stage {Stage_name} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
