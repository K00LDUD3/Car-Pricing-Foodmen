import pandas as pd
import numpy as np
import pickle

import warnings
warnings.filterwarnings('ignore')

import datetime as dt

from sklearn.preprocessing import OrdinalEncoder
from scipy.stats import shapiro

def ReadTrainData(filename, raw=False, encode = True) -> pd.DataFrame:
    #Reading the data
    df = pd.read_csv(filepath_or_buffer=filename, index_col=[0]).drop('Doors', axis=1)
    
    ##PRICE has high variance so it will be reduced to 100 - 100k $
    df = df.drop(df[(df['Price'] > 100000) | (df['Price'] < 100)].index)
    
    ##MANUFACTURER redundancies
    manuf_count = pd.DataFrame(df.Manufacturer.value_counts())
    manuf_count = manuf_count[manuf_count['Manufacturer'].isin([i for i in range(0,10)])]
    df = df[~df['Manufacturer'].isin(manuf_count.index)]
    print(df.shape)

    ##MILEAGE
    df.Mileage = pd.to_numeric(df.Mileage.apply(lambda x: float(str(x).split(' ')[0])))

    ##LEVY
    #Replacing hyphens with 0s
    def replaceHyphen(n):
        if n == '-':
            return 0.0
        return float(n)
    df.Levy = pd.to_numeric(df.Levy.apply(lambda x: replaceHyphen(x)))
    
    #ENGINE VOLUME
    #Getting raw number
    def convToVol(n):
        n = str(n).strip()
        tokens = n.split()
        return float(tokens[0])
    #Splitting Turbo and non turbo engine types
    def TurboClass(n):
        n = str(n).strip()
        tokens = n.split()
        if len(tokens) == 1:
            return 0
        else:
            return 1
    df['Turbo'] = df['Engine volume'].apply(lambda x: TurboClass(x))
    df['Engine volume'] = df['Engine volume'].apply(lambda x: convToVol(x))

    if raw:
        return df

    #Removing INDEX column
    #df.drop('index', inplace=True, axis=1)

    ##LEATHER INTERIOR replacing yes or no with 1 and 0
    def YNReplace(n):
        n = str(n).strip().lower()
        if n == 'yes':
            return 1
        return 0
    df['Leather interior'] = df['Leather interior'].apply(lambda x: YNReplace(x))

    # OUTLIERS - Pattern breakers/ Exceptions
    def FindOutliersLim(column_name, df):
        q1 = np.percentile(df[column_name], 25) #1st quartile - 25%
        q3 = np.percentile(df[column_name], 75) #3rd quartile - 75%
        IQR = q3 - q1 #Inter Quartile Range
        liniency_factor = 1.3
        lim = IQR * liniency_factor
        lower_lim, upper_lim = q1 - lim, q3 + lim
        return lower_lim, upper_lim

    def RemoveOutlier(df, column_name, upper_lim, lower_lim):
        outlier_list = [x for x in df[column_name] if x < upper_lim] #List of Outliers that exist
        outlier_elimmed = [x for x in df[column_name] if x >= lower_lim and x <= upper_lim]
        final_col = np.where(df[column_name]>upper_lim,upper_lim,np.where(df[column_name]<lower_lim,lower_lim,df[column_name]))
        return final_col

    outliers = ['Levy', 'Engine volume', 'Mileage']
    for i in outliers:
        lower_lim, upper_lim = FindOutliersLim(column_name=i, df=df)
        df[i] = RemoveOutlier(df, i, upper_lim=upper_lim, lower_lim=lower_lim)


    #Creating Intervals aka BIN variables 
    #Alternative to scaling down data
    mileage_intervals = [i for i in range(0,10)]
    df['Mileage_BIN'] = pd.cut(df['Mileage'], len(mileage_intervals), labels=mileage_intervals)
    df['Mileage_BIN'] = df['Mileage_BIN'].astype(float)

    #Making everything lower case
    df['Manufacturer'] = df['Manufacturer'].apply(lambda x: x.lower())
    df['Model'] = df['Model'].apply(lambda x: x.lower())
    df['Category'] = df['Category'].apply(lambda x: x.lower())
    df['Fuel type'] = df['Fuel type'].apply(lambda x: x.lower())
    df['Gear box type'] = df['Gear box type'].apply(lambda x: x.lower())
    df['Wheel'] = df['Wheel'].apply(lambda x: x.lower())
    df['Color'] = df['Color'].apply(lambda x: x.lower())
    df['Color'] = df['Color'].apply(lambda x: x.lower())


    #WHEEL cleaning up wheel column to make it say either left wheel or right wheel
    def SplitWheel(n):
        n = str(n)
        return ''+n.split(' ')[0].split('-')[0]+' wheel'
    df['Wheel'] = df['Wheel'].apply(lambda x: SplitWheel(x))
    wheel_dummies = pd.get_dummies(df['Wheel'], drop_first = False)
    df = pd.concat([df, wheel_dummies], axis=1)


    if not encode:
        return df
    
    #Ordinal Encoding Categorical Variables
    numeric_data = df.select_dtypes(include=np.number)
    categ_data = df.select_dtypes(include='object')
    encode = OrdinalEncoder()
    categ_col = categ_data.columns.tolist()
    encode.fit(categ_data[categ_col])

    '''
    Categorical Columns
    ['Manufacturer', 'Model', 'Category', 'Fuel type', 'Gear box type', 'Drive wheels', 'Wheel', 'Color']
    '''
    
    categ_ordinal_encoded = encode.transform(categ_data[categ_col])
    categ_ordinal_encoded = pd.DataFrame(categ_ordinal_encoded, columns=categ_col)
    categ_data.reset_index(inplace=True)
    categ_ordinal_encoded.head()

    #Storing encoder for future reference
    f = open('Encoder.bin', 'wb')
    pickle.dump(encode, f)
    f.close()

    numeric_data.reset_index(inplace=True)
    categ_ordinal_encoded.reset_index(inplace=True)
    categ_ordinal_encoded.drop('index', axis=1, inplace=True)
    final_data = pd.concat([numeric_data, categ_ordinal_encoded], axis=1)

    #Log Transforming Price to increase relation with other columns 
    #Makes it easier to find a pattern
    final_data['Price'] = np.log(final_data['Price'])

    df.reset_index(inplace=True)
    df.drop('Unnamed: 0', axis=1, inplace=True)
    return final_data


def GetBINVal(val):
    val = float(val)
    df_mileage = pd.read_csv('TrainData_Processed.csv', index_col=[0])['Mileage']
    df_mileage = pd.concat([df_mileage, pd.Series(val)], ignore_index=True)
    df_mileage = df_mileage.to_frame(name='Vals')
    mileage_intervals = [i for i in range(0,10)]
    df_mileage['Mileage_BIN'] = pd.cut(df_mileage['Vals'], len(mileage_intervals), labels=mileage_intervals)
    df_mileage['Mileage_BIN'] = df_mileage['Mileage_BIN'].astype(float)
    return float(df_mileage.tail(1)['Mileage_BIN'])