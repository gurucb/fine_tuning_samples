from data_extractor import DataExtractor
from data_transformer import DataTransformer
from data_validator import DataValidator
import logging

class DataGenerator():
    def __init__(self,
                 task_config:dict):
        logger = logging.getLogger(__name__)
        self.task_config = task_config
        logger.info("DataGenerator Initialized!!")
        self.data_extractor = DataExtractor()
        print(self.task_config)
    
    def generate_data(self):
        extraction_config = self.task_config["extraction"]
        dataset_name = extraction_config["dataset_name"]
        destination_path = extraction_config["destination_path"]
        self.data_extractor.fetch_datasets(
                                                dataset_name=dataset_name,
                                                destination_path=destination_path
                                            )
        
        
        