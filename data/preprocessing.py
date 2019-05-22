import csv
import pandas as pd


chest_pain={'1.0':"typical angin",'2.0':"atypical angina",'3.0':"non-anginal pain","4.0":"asymptomatic"}
cardiographic={'0.0':"normal",'1.0':"having ST-T",'2.0':"probable or definite"}
thal={'3.0':"normal",'6.0':"fixed defect",'7.0':"reversable defect",'?':"?"}

import os
path=os.path.abspath('.')+"/data/heart/processed.cleveland.data"


def preprocessing():
    names=['age','sex','chest','pressure','cholestoral','sugar',\
           'cardiographic','heart_rate','angina','oldpeak','slope','flourosopy','thal','target']
    
    df = pd.read_csv(path, delimiter=',',float_precision='high',header=None,names=names)
    df.iloc[:,1]= df.iloc[:,1].map(lambda x: 'male' if x == 1 else 'female')
    df.iloc[:,2]= df.iloc[:,2].map(lambda x:chest_pain[str(x)])
    df.iloc[:,6]= df.iloc[:,6].map(lambda x:cardiographic[str(x)])
    df.iloc[:,12]= df.iloc[:,12].map(lambda x:thal[str(x)])
    df.iloc[:,13]= df.iloc[:,13].map(lambda x: 'no' if x == 0 else 'yes')
    return df.to_json(orient='records')