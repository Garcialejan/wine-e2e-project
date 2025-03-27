from src.wine_e2e_project.config.configuration import ConfigurationManager
from src.wine_e2e_project.components.model_trainer import ModelTrainer
from src.wine_e2e_project import logger

STAGE_NAME = "Model Training Stage"


class ModelTrainerTrainingPipeline():
    def __init__(self):
        pass
    
    def initiate_model_training(self):
        config=ConfigurationManager()
        model_trainer_config=config.get_model_trainer_config()
        model_trainer=ModelTrainer(config=model_trainer_config)
        model_trainer.train()
        
# if __name__ == "__main__":
#     try:
#         logger.info(f">>>> stage {STAGE_NAME} started <<<<")
#         obj = ModelTrainerTrainingPipeline()
#         obj.initiate_model_training()
#         logger.info(f">>>> stage {STAGE_NAME} completed <<<<")
#     except Exception as e:
#         logger.exception(e)
#         raise e