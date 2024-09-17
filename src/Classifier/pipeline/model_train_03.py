from Classifier.config.configuration import ConfigurationManager
from Classifier.components.model_train import Training
from Classifier import logger


Stage_name= 'MODEL TRAIN'

class TrainModelPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            training_config = config.get_training_config()
            training = Training(config=training_config)
            training.get_base_model()
            training.train_valid_generator()
            training.train()
        except Exception as e:
            raise e
    


if __name__=='__main__':
    try:
        logger.info(f">>>>>> stage {Stage_name} started <<<<<<")
        obj = TrainModelPipeline()
        obj.main()
        logger.info(f">>>>>> stage {Stage_name} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e