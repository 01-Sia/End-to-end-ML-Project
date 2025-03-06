import sys 
import os 

from src.utils import load_object   #load pickle files 

from src.logger import logging 
import pandas as pd
import numpy as np 

from src.exception import CustomException



class  PredictionPipeline:
    def __init__(self):
        pass
    def predict(self,features):
        try:
            model_path = "artifacts/model.pkl"
            preprocessor_path ="artifacts/preprocessor.pkl"
            model = load_object(model_path)
            preprocess = load_object(preprocessor_path)
            print(preprocess)
            if preprocess is None:
                raise Exception("Failed to load preprocessor from {}".format(preprocessor_path))

            # features_df = pd.DataFrame([features])
            features = np.array(features).reshape(1, -1) #Reshape to 2d array


            data_scale = preprocess.transform(features)
            result = model.predict(data_scale)
            return result
        except Exception as e:
            raise CustomException(e,sys) 



class CustomData:                  # responsible in mapping all data given to the fields of form to the backend here 
    def __init__(self,
                age,
                sex,
                bmi,
                children,
                smoker,
                region):
        self.age=age
        self.sex=sex
        self.bmi=bmi
        self.children=children
        self.smoker=smoker
        self.region=region


    def data_dataframe(self):
        try:

            ''' return data in form of data frame for model '''
            custom_data ={
                "age":[self.age],
                "sex":[self.sex],
                "bmi":[self.bmi],
                "children":[self.children],
                "smoker":[self.smoker],
                "region":[self.region]
            }

            return pd.DataFrame(custom_data)
        except Exception as e:
            raise CustomException(e,sys)
    




        
