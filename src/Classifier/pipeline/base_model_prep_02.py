from Classifier.config.configuration import ConfigurationManager
from Classifier.components.base_model_prep import Prepare_Base_Model
from Classifier import logger

Stage_name= 'BASE MODEL PREP'

class BaseModelPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            params_base_model_config = config.get_base_model_config()
            params_base_model = Prepare_Base_Model(config=params_base_model_config)
            params_base_model.get_base_model()
            params_base_model.update_base_model()

        except Exception as e:
            raise e

if __name__=='__main__':
    try:
        logger.info(f">>>>>> stage {Stage_name} started <<<<<<")
        obj = BaseModelPipeline()
        obj.main()
        logger.info(f">>>>>> stage {Stage_name} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
