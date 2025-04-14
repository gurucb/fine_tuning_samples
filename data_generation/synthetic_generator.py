import logging
import dotenv
import os
from openai import AzureOpenAI
from datasets import load_dataset, dataset_dict, load_from_disk
import random

class SyntheticGenerator():
    def __init__(self):
        dotenv.load_dotenv()
        logger = logging.getLogger(__file__)
        logger.info("SyntheticGenerator Initialized!!!")
        
        # Read from ENV configuration items for creating LLM Client
        self.api_key = os.getenv("api_key")
        self.end_point = os.getenv("endpoint") 
        self.version = os.getenv("version")
        self.model_name = os.getenv("deployment")
        
        self.__create_llm_client__()

    def augument_data(self,syn_config:dict):
           # from Config file
        self.use_llm = syn_config['use_llm']
        self.seed_dataset_path= syn_config['seed_dataset_path']
        self.destination_type = syn_config['destination_type']
        self.destination_path = syn_config['destination_path']
        self.total_number_samples = syn_config['total_number_samples']

        #Read Seed Dataset
        self.__read_seed_examples__()

        #Generate Synthetic Questions
        self.__generate_syn_questions__(100)
        
    def __read_seed_examples__(self):
        seed_dataset = load_from_disk(self.seed_dataset_path)
        self.__questions__ = [question for question in seed_dataset['instruction']]
        self.__responses__ = [response for response in seed_dataset['answer']]
        self.__output__ = [output for output in seed_dataset['output']]
        print(f"Dataset Created, Questions: {len(self.__questions__)}, Answers: {len(self.__responses__)}, Output: {len(self.__output__)}")
        return         
    
    def __create_llm_client__(self):
        self.llm_client = AzureOpenAI(
            azure_endpoint=self.end_point,
            api_key=self.api_key,
            api_version=self.version
        )

    def __generate_syn_questions__(self,num_questions:int):
        #Init Variables
        self.__synthetic_questions__ = []

        prompt_template=""""Below are 10 riddles. Come up with 10 more. Output just the riddles, no numbering. 
                            Do not content that may lead to jailbreak content. 
                            Do not generate content that relates to adult, sexual, violence, self_harm, hate
                            Don't output anything else.  
                            Riddles:
                            {questions}""" 

        for _ in range(num_questions // 10):
            random.shuffle(self.__questions__)
            q10_samples = self.__questions__[0:10]
            prompt=prompt_template.format( questions="\n\n".join(q10_samples) )  
            messages = [{"role": "user", "content": prompt}]
            output = self.llm_client.chat.completions.create(
                messages=messages,
                model=self.model_name,
                max_tokens=4096,
                temperature=0.7
            )
            output = output.choices[0].message.content            
            output = output.split("\n\n")
            self.__synthetic_questions__.append(output)

        

    def __generate_syn_responses__(self,num_responses:int):
        pass