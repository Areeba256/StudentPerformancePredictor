#utils will have all the cmmon functionalities which can be used across the project
import os
import sys
import pickle
from src.exceptions import CustomException
import numpy as np
import pandas as pd
import dill
from sklearn.metrics import r2_score

def save_object(file_path, obj):
    '''
    file_path: path where the object to be saved
    obj: object to be saved
    '''
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True) #creates directory if not exists
        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj) #saves the object in the file
    except Exception as e:
        raise CustomException(e, sys)

def evaluate_models(X_train, y_train, X_test, y_test, models):
    '''
    X_train: training features
    y_train: training labels
    X_test: testing features
    y_test: testing labels
    models: dictionary of models to be evaluated
    '''
    try:
        model_report = {}
        for i in range(len(models)):
            model = list(models.values())[i]
            model.fit(X_train, y_train) #training the model
            y_test_pred = model.predict(X_test) #predicting on test data
            test_model_score = r2_score(y_test, y_test_pred) #calculating r2 score
            model_report[list(models.keys())[i]] = test_model_score #storing the score in the report
        return model_report
    except Exception as e:
        raise CustomException(e, sys)