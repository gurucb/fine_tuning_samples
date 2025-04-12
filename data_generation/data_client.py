from data_extractor import DataExtractor
from data_generation import DataGenerator
from data_validator import DataValidator
from data_transformer import DataTransformer
import logging
import json

class DataClient():
    #Initialize Data Client for given DataHub

    def __init__(
                    self,
                    task_config_filepath:str
                 ):
        self.logger = logging.getLogger(__name__)
        with  open(task_config_filepath) as tc:
            self.task_config = json.loads(tc.read())
            print(self.task_config)

        self.logger.info("Data Client Intialized!!")

    #Perform specifie task against Hub and dataset. 
    def execute_data_task(self):
        self.logger.info(f"Starting data task {self.task_config["task_type"]} from ")
