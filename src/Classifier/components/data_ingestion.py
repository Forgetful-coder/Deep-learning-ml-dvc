import os
import zipfile
import gdown
from Classifier import logger
from Classifier.utils.common import get_size
from Classifier.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config
    
    def download_file(self)->str:
        """
        downloads the data and stores into zip file
        """
        try:
            dataset_url= self.config.source_url
            zip_location = self.config.local_file_data
            os.makedirs(self.config.root_dir,exist_ok=True)

            logger.info(f"Downloading data from {dataset_url} into file {zip_location}")

            file_id = dataset_url.split('/')[-2]
            prefix_id = 'https://drive.google.com/uc?/export=download&id='
            gdown.download(prefix_id+file_id,zip_location)
        
        except Exception as e:
            raise e
    
    def unzip_data(self):
        ''''Extracts the data 
        Function returns None'''
        unzip_path = self.config.unzip_file_path
        os.makedirs(unzip_path,exist_ok=True)
        with  zipfile.ZipFile(self.config.local_file_data,'r') as zipref:
            zipref.extractall(unzip_path)

            


            
