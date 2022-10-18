'''
Module for dealing with data
'''
import pandas as pd
import numpy as np
import pickle
import joblib
import warnings
warnings.filterwarnings('ignore')

import datetime as dt

from sklearn.preprocessing import OrdinalEncoder

df_raw = pd.read_csv('TrainData_Raw.csv')


def GetBINVal(val):
    val = float(val)
    df_mileage = pd.read_csv('TrainData_Processed.csv', index_col=[0])['Mileage']
    df_mileage = pd.concat([df_mileage, pd.Series(val)], ignore_index=True)
    df_mileage = df_mileage.to_frame(name='Vals')
    mileage_intervals = [i for i in range(0,10)]
    df_mileage['Mileage_BIN'] = pd.cut(df_mileage['Vals'], len(mileage_intervals), labels=mileage_intervals)
    df_mileage['Mileage_BIN'] = df_mileage['Mileage_BIN'].astype(float)
    return float(df_mileage.tail(1)['Mileage_BIN'])

#Preparing input for feeding the model
def ArrangeInput(params):
    inp = [params['levy'],
           params['prod_year'],     
           params['leather'],
           params['engine_vol'],
           params['mileage'],
           params['cylinders'],
           params['airbags'],
           params['turbo'],
           GetBINVal(params['mileage']),
           params['left'],
           params['right'],
           #String Parameters (to be encoded)
           params['manufacturer'],
           params['model'],
           params['category'],
           params['fuel_type'],
           params['gear_box_type'],
           params['drive_wheels'],
           params['color']
    ]
    

    
    categ_col = ['Manufacturer', 'Model', 'Category', 'Fuel type', 'Gear box type', 'Drive wheels', 'Color']
    categ_var = inp[len(inp) - 7 ::]
    categ_data = pd.DataFrame(categ_var, index=categ_col).T
    f = open('Encoder.bin', 'rb')
    encoder = pickle.load(f)
    f.close()
    categ_var_enc = pd.DataFrame(encoder.transform(categ_data), columns=categ_col)
    
    
    numeric_col = ['Levy', 'Prod. year', 'Leather interior', 'Engine volume', 'Mileage', 'Cylinders', 'Airbags', 'Turbo', 'Mileage_BIN', 'left wheel', 'right wheel']
    numeric_data = pd.DataFrame(inp[:11], index=numeric_col).T

    final_data = pd.concat([numeric_data, categ_var_enc], axis=1)

    return final_data

def Predict(data):
    rf_model = joblib.load("D:\\School\\2.CS\\2. Grd 12\\Car-Pricing-Foodmen\\Models\\RF_final_1_1_0.obj")
    y_pred = rf_model.predict(data)
    return np.exp(y_pred)[0] * 79.52

#Getting a unique model for each manufacturer
def ManufactUniqueModels(choice = 'M') -> tuple:
    manufacturers = list(df_raw.Manufacturer.unique())
    if choice.upper() == 'M':
        return manufacturers
    else:
        manufacturers_unique_models = {}
        for i in range(len(manufacturers)):
            manufacturers_unique_models[manufacturers[i]] = df_raw[df_raw['Manufacturer'] == manufacturers[i]].Model.unique()
        return manufacturers_unique_models

#Getting unique category, fuel type, gear box type, drivewheels, color
def CategValsUnique() -> dict:
    category = list(df_raw['Category'].unique())
    fuel_type = list(df_raw['Fuel type'].unique())
    gear_box_type = list(df_raw['Gear box type'].unique())
    drivewheels = list(df_raw['Drive wheels'].unique())
    color = list(df_raw['Color'].unique())
    
    categ_dict = {
        "category": category,
        "fuel_type": fuel_type,
        "gear_box_type": gear_box_type,
        "drive_wheels": drivewheels,
        "color": color
    }
    return categ_dict

#Segregating models based on category
def FetchModelsCateg(model):
    categ_list = CategValsUnique().get('category')
    df = pd.read_csv('TrainData_Raw.csv')[['Model', 'Category']]
    categ_models = {}
    
    for i in categ_list:
        categ_models[i] = list(set(list(df['Model'][df['Category'] == i])))
    current_categ = []
    for categ, val_l in categ_models.items():
        if model in val_l:
            current_categ.append(categ) 
    return current_categ