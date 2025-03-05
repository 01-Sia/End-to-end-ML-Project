import os 
import sys
from src.logger import logging 
from src.exception import CustomException
import pandas as pd
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from dataclasses import dataclass
import numpy as np

from src.utils import save_object

@dataclass 
class DataTransformationConfig:   
    ''' class will provide any inputs for data transformation processes.
    The data tranformation refers to the process of 
     converting the data into model ready form such as numerical -> normalized ina range and categorical -> onehotencoded'''
    
    preprocessor_file_path = os.path.join('artifacts','preprocessor.pkl')



class DataTransform:
    def __init__(self):
        self.data_transform= DataTransformationConfig()

    def transformation(self,df):
        ''' converting the cat-> one hot encoding and numerical standardized'''
        try:
            

            numerical_features = df.select_dtypes(exclude=['object']).columns
            categorical_features =df.select_dtypes(include=['object']).columns
            preprocessor= ColumnTransformer(
                [
                    ("scaler", StandardScaler(),numerical_features),
                    ("onehot",OneHotEncoder(),categorical_features)
                ]
            )
            logging.info("Pipeline formation is done and implemented")
            pipeline = Pipeline(steps=[
                ('preprocessor',preprocessor)
            ])
            logging.info("The pipeline was created")
            return pipeline
            
        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_transform(self,train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            # preprocessor_obj = self.transformation(train_df)
            target_column = 'charges'

            X_train_df = train_df.drop(columns =[target_column], axis = 1)
            y_train_df = train_df[target_column]
            X_test_df = test_df.drop(columns =[target_column], axis = 1)
            y_test_df = test_df[target_column]
            preprocessor_obj = self.transformation(X_train_df)

            logging.info("Applying  preprocessing on X_train,y_train , X_test and y_test")
            X_train_preprocessed= preprocessor_obj.fit_transform(X_train_df) # fit_transform fits the training data before the 
            X_test_preprocessed= preprocessor_obj.transform(X_test_df)

            train_arr = np.c_[
                X_train_preprocessed, np.array(y_train_df)
                    ] # concatenate the preprocessed num columns with the org cat colmns
            test_arr = np.c_[
                X_test_preprocessed, np.array(y_test_df)
                ]
            logging.info("Saved preprocessing object")

            save_object(
                file_path = self.data_transform.preprocessor_file_path,
                obj = preprocessor_obj
            )

            return train_arr,test_arr,self.data_transform.preprocessor_file_path







        except Exception as e:
            raise CustomException(e,sys)



