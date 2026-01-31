#utils will have all the cmmon functionalities which can be used across the project
import os
import sys
import pickle
from src.exceptions import CustomException
import numpy as np
import pandas as pd
import dill

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