from Classifier import logger
from Classifier.pipeline.data_ingestion_pipeline01 import DataIngestionPipeline
from Classifier.pipeline.base_model_prep_02 import BaseModelPipeline

Stage_name= 'DATA INGESTION'
try:
        logger.info(f">>>>>> stage {Stage_name} started <<<<<<")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f">>>>>> stage {Stage_name} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

Stage_name= 'BASE MODEL PREP'
if __name__=='__main__':
    try:
        logger.info(f">>>>>> stage {Stage_name} started <<<<<<")
        obj = BaseModelPipeline()
        obj.main()
        logger.info(f">>>>>> stage {Stage_name} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
