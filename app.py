from flask import Flask,request,render_template

import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictionPipeline

app=Flask(__name__)




@app.route("/")
def index():
    return render_template('home.html')


@app.route('/predict',methods =['GET','POST'])
def  prediction():
    if request.method =='GET':
        return render_template('index.html')   # this will cntain simple data fields to provide to the model 
    else:
        data = CustomData(
            age = int(request.form.get('age')),
            sex = request.form.get('sex'),
            bmi = float(request.form.get('bmi')),
            children = int(request.form.get('children')),
            smoker = request.form.get('smoker'),
            region= request.form.get('region')
        )

        prediction_df = data.data_dataframe()
        print(prediction_df)

        predict_pipe = PredictionPipeline()
        predicted = predict_pipe.predict(prediction_df)
        return render_template('index.html',results = predicted[0])
    


if __name__=="__main__":
    app.run(host = "0.0.0.0", debug = True)


        