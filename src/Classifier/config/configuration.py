from Classifier.constants import *
from Classifier.utils.common import read_yaml,create_directories
from Classifier.entity.config_entity import DataIngestionConfig
from Classifier.entity.config_entity import ModelConfig



class ConfigurationManager:
    def __init__(self,
                 config_file_path=CONFIG_FILE_PATH,
                 params_file_path=PARAMS_FILE_PATH):
    
        self.config=read_yaml(config_file_path)
        self.params=read_yaml(params_file_path)

        create_directories([self.config.artifacts_root])
    

    def get_data_ingestion_config(self)->DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_file_data=config.local_file_data,
            unzip_file_path=config.unzip_file_path,
        )

        return data_ingestion_config
    
    def get_base_model_config(self)->ModelConfig:
        config = self.config.prepare_model
        params = self.params
        create_directories([config.root_dir])

        model_config=ModelConfig(
            root_dir=config.root_dir,
            model_path=config.model_path,
            updated_model_path=config.updated_model_path,
            learning_rate=params.LEARNING_RATE,
            image_size=params.IMAGE_SIZE,
            include_top=params.INCLUDE_TOP,
            weights = params.WEIGHTS,
            classes= params.CLASSES
            
        )
        return model_config
