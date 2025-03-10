import os 
import sys

import pandas as pd
import numpy as np
from sklearn.metrics import r2_score

from src.exception import CustomException

import dill 

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file:
            dill.dump(obj,file)
    except Exception as e:
        raise CustomException(e,sys)
    
def evaluate_models(X_train,X_test,y_train,y_test,models):
    try:
        report={}
        for i in range(len(list(models))):
            model = list(models.values())[i]
            model.fit(X_train,y_train)
            y_train_pred= model.predict(X_train)
            y_test_pred = model.predict(X_test)
            train_model_score = r2_score(y_train,y_train_pred)
            test_model_score = r2_score(y_test,y_test_pred)
            report[list(models.keys())[i]]=test_model_score
        return report
    except Exception as e:
        raise CustomException(e,sys)
       
    
def load_object(file_path):
    try:
        with open(file_path, "rb") as file:
            dill.load(file)
    except Exception as e:
        raise CustomException(e,sys)
