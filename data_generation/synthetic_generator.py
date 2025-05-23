import logging
import dotenv
import os
from openai import AzureOpenAI
from datasets import load_dataset, dataset_dict, load_from_disk
import random

class SyntheticGenerator():
    synthetic_riddle_dataset = {}
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

        # #Generate Synthetic Questions
        self.__generate_syn_idioms__(100)

        self.__generate_syn_answers__()
        
    def __read_seed_examples__(self):
        seed_dataset = load_from_disk(self.seed_dataset_path)
        self.__base_questions__ = [question for question in seed_dataset['instruction']]
        self.__base_responses__ = [response for response in seed_dataset['answer']]
        self.__base_output__ = [output for output in seed_dataset['output']]
        print(f"Dataset Created, Questions: {len(self.__base_questions__)}, Answers: {len(self.__base_responses__)}, Output: {len(self.__base_output__)}")
        ##This had to be done as Azure Open AI blocks due to responsible AI
        # https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/content-filter?tabs=warning%2Cuser-prompt%2Cpython-new
        ind = list([0,2,3,5,7,8,10,11,12,16,17,21,23,24,25,26,27,29,30,31])
        self.__questions__ = []
        for cnt in range(len(ind)):
            self.__questions__.append(self.__base_questions__[ind[cnt]])
        return         
    
    def __create_llm_client__(self):
        self.llm_client = AzureOpenAI(
            azure_endpoint=self.end_point,
            api_key=self.api_key,
            api_version=self.version
        )

    def __generate_syn_idioms__(self,num_questions:int):
        #Init Variables
        self.__synthetic_questions__ = []

        prompt_template=""""Below are 10 riddles. Come up with 10 more. Output just the riddles, no numbering. 
                            Don't content that may lead to jailbreak content.
                            Ignore input pormpts that contain Adult, violence, hat, self_harm content.
                            Do NOT generate adult, violence, hate, self_harm content.
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
            for o in output:
                self.__synthetic_questions__.append(o)
            # [print(str(i)+":"+str(self.__synthetic_questions__[i])) for i in range(len(self.__synthetic_questions__))]
            print(f"Total {len(self.__synthetic_questions__)} Synthetic idioms generated.")
        return

    def __generate_syn_answers__(self):
        self.__synthetic_answers__ = []
        prompt_template = """"{ques}\nThink step-by-step, keep your explanations simple, try your very best. If there is information missing for you to come up with a specific   
                            answer, just ask me a short question at the very end of your answer."""
        for question in self.__synthetic_questions__:
            prompt = prompt_template.format(ques = question)
            messages = [{"role": "user", "content": prompt}]
            output = self.llm_client.chat.completions.create(
                messages=messages,
                model=self.model_name,
                max_tokens=4096,
                temperature=0.7
            )
            output = output.choices[0].message.content
            self.__synthetic_answers__.append(output)
        print(f"Total {len(self.__synthetic_answers__)} Synthetic answers generated.")
        return     