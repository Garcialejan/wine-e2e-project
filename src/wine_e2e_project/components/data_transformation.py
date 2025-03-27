from src.wine_e2e_project import logger
from sklearn.model_selection import train_test_split
import pandas as pd
import os

from src.wine_e2e_project.entity.config_entity import DataTransformationConfig

class DataTransformation():
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        
    # In these class, we can add as many functions as we want to use
    # to make the data transformatiuon pipeline
        
    def train_test_splitting(self):
        data = pd.read_csv(self.config.data_path)
        train, test = train_test_split(data, test_size=0.25, shuffle=True)
        
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"),index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"),index = False)

        logger.info("Splited data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)