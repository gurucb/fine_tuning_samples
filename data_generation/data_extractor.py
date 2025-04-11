
"""
    Purpose: Extract seed datasets (See datasets may be public datasets or private purpose built datasets) 
    Seed Datasets may be enhanced and transformed into "Instruction set" format like Question / Answer.
    Using foundational model, augument dataset to train any SLM model.

    Scenarios:
        1. fetch data from public datasets (but not purpose built for LLMs like stock tick data etc)
        2. fetch data from public data hubs like HuggingFaceHub
        3. private data repositories

    Input:
        1. dataset_name: Dataset name to fetch.
        2. dataset_hub: Hub where dataset is hosted or URI of dataset.
        3. dataset_modality: text / image / audio / video
    Output:
        1. location where dataset needs to be persisted locally.
        2. 
    
    User:
        1. User will need to select from list of datasets (future)

"""
class DataExtractor():
    dataset_name:str
    dataset_hub:str
    def __init__(self):
        pass
    def list_datasets(self):
        pass
    def fetch_datasets(self):
        pass
    def save_datasets(self):
        pass