import os 
import sys 
from src.logger import logging 
from src.exception import CustomException
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score,mean_squared_error
from sklearn.preprocessing import PolynomialFeatures
from sklearn.ensemble import RandomForestRegressor
from dataclasses import dataclass 
from src.utils import evaluate_models,save_object

@dataclass
class ModelTrainConfig:
    trained_model_path = os.path.join('artifacts','model.pkl')

class Model:
    def __init__(self):
        self.model_train=ModelTrainConfig()

    
    def model(self,train,test):
        try:
            logging.info("Making X_train, y_train and X_test , y_test for training the model. ")
            # train_arr = tarnsformed_num +y_train_df 
            X_train,y_train,X_test,y_test = (
                train[:,:-1],
                train[:,-1],
                test[:,:-1],
                test[:,-1]
            )
            models = {
                "Random Forest": RandomForestRegressor(),
                "Linear Regression" : LinearRegression(),
                # "Polynomial Regression" : PolynomialFeatures()  bcz it is a preproceesing technique for feature engineering 
            }

            # params={
            #     "Random Forest":{'n_estimators':[8,16,32,64,128,256]}
            # }
            model_reports:dict = evaluate_models(X_train=X_train, y_train=y_train, X_test=X_test,y_test=y_test,models=models)

            ## To get best model score from report 
            best_model_score = max(sorted(model_reports.values()))

            ## to get name of the model 

            best_model_name = list(model_reports.keys())[
                list(model_reports.values()).index(best_model_score)
            ]

            best_model = models[best_model_name]

            if best_model_score<0.6:
                raise CustomException("No best model found")
            
            # preprocessor is called if any new data for testing is being added.

           
            logging.info("The model is trained and best model is formed")
            save_object(
                file_path = self.model_train.trained_model_path,
                obj = best_model

            )
            predicted = best_model.predict(X_test)
            r2_values = r2_score(y_test, predicted)
            return r2_values
        
        
            
        except Exception as e:
            raise CustomException(e,sys)
           

