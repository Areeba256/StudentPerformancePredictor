from flask import Flask, request, render_template
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application= Flask(__name__) #gives entry point for the flask app, __name__ is a special variable which will have value 'app' here
app=application
@app.route('/') #decorator, connects the function to a url
def index():
    return render_template('home.html') #renders the html file
    #render_template searches for the html file in templates folder by default
@app.route('/predict', methods=['GET', 'POST']) #POST method to send data to the server
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        data=CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            writing_score=int(request.form.get('writing_score')),
            reading_score=int(request.form.get('reading_score'))
        )       
        #get the data from the form
        pred_df=data.get_data_as_data_frame() #converts the inputs to dataframe
        print(pred_df)
        predict_pipeline=PredictPipeline()
        results=predict_pipeline.predict(pred_df) #does the prediction
        return render_template('home.html', results=results[0]) #sends the result to the html file
if __name__=="__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
    #runs the flask app on the local server
    
