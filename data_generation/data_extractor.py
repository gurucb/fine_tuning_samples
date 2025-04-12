from datasets import load_dataset, DatasetDict, Dataset, load_from_disk
import logging
import os
import json

class DataExtractor():
    dataset_name:str
    dataset_hub:str
    def __init__(self):
        logger = logging.getLogger(__file__)
        logger.info("DataExtractor Initialized!!!")
    def list_datasets(self):
        pass
    def fetch_datasets(self,dataset_name,destination_path):
        self.seed_data = []
        self.dataset_name = dataset_name
        self.destination_path= destination_path
        self.dataset = load_dataset(self.dataset_name, split="all")
        self.save_datasets()
    def save_datasets(self):
        os.makedirs(self.destination_path, exist_ok=True)
        file_name = os.path.join(self.destination_path,"seed_dataset")
        self.dataset.save_to_disk(file_name)
       