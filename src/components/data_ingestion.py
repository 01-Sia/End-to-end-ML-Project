import os
import sys
from src.logger import logging 
from src.exception import CustomException
from src.components.train_model import ModelTrainConfig
from src.components.train_model import Model

from src.components.data_transformation import DataTransformationConfig
from src.components.data_transformation import DataTransform

import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass 

@dataclass
class DataIngestionConfig:
    train_data_path:str = os.path.join('artifacts',"train.csv")
    test_data_path:str = os.path.join('artifacts',"test.csv")
    raw_data_path:str = os.path.join('artifacts',"data.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion=DataIngestionConfig()


    def initiate_ingestion(self):
        logging.info("The data ingestion step has started")
        try:
            df = pd.read_csv('notebook/data/insurance.csv')
            logging.info('Dataset is read as df')
            os.makedirs(os.path.dirname(self.ingestion.train_data_path), exist_ok=True)
            df.to_csv(self.ingestion.raw_data_path, index=False, header=True)
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=0)
            train_set.to_csv(self.ingestion.train_data_path, index = False, header = True)
            test_set.to_csv(self.ingestion.test_data_path, index = False, header = True)
            logging.info("The data ingestion process == completed.")
            return   self.ingestion.train_data_path,self.ingestion.test_data_path 

        except Exception as e:
            raise CustomException(e, sys)
    
    
if __name__=="__main__":
    obj = DataIngestion()
    train, test = obj.initiate_ingestion()

    ob = DataTransform()
    trai, tes,_ =ob.initiate_data_transform(train,test)

    model= Model()
    print(model.model(trai,tes))








