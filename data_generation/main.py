from data_client import DataClient
import logging

def main():
    configure_logging()
    logger = logging.getLogger(__name__)
    logger.info("Initializng Dataclient...")
    data_client = DataClient(task_config_filepath="data_generation/generate.json")
    data_client.execute_data_task()
    logger.info("Data Task Completed!!!")
def configure_logging():  
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        filename='SLM.log',
        filemode='w+'
    )

if __name__ == "__main__":
    main()