import csv
import pandas as pd
import os
import numpy as np
# chest_pain={'1.0':"typical angin",'2.0':"atypical angina",'3.0':"non-anginal pain","4.0":"asymptomatic"}
# cardiographic={'0.0':"normal",'1.0':"having ST-T",'2.0':"probable or definite"}
# thal={'3.0':"normal",'6.0':"fixed defect",'7.0':"reversable defect",'?':"?"}
# path=os.path.abspath('.')+"/data/heart/processed.cleveland.data"

def clean_data():
    path=os.path.abspath('.')+"/data/heart/processed.cleveland.data"
    chest_pain={'1.0':"typical angin",'2.0':"atypical angina",'3.0':"non-anginal pain","4.0":"asymptomatic"}
    cardiographic={'0.0':"normal",'1.0':"having ST-T",'2.0':"probable or definite"}
    thal={'3.0':"normal",'6.0':"fixed defect",'7.0':"reversable defect",'?':"?"}
    names=['age','sex','chest','pressure','cholestoral','sugar',\
        'cardiographic','heart_rate','angina','oldpeak','slope','flourosopy','thal','target']        
    df = pd.read_csv(path, delimiter=',',float_precision='high',header=None,names=names)
    df=df.drop(df[(df['thal']=='?')|(df['flourosopy']=='?')].index)
    df.iloc[:,1]= df.iloc[:,1].map(lambda x: 1 if x == 1 else 0)
    df.iloc[:,13]= df.iloc[:,13].map(lambda x: 0 if x == 0 else 1)
    df['log_pressure'] = np.log(df['pressure'])
    df['log_cholestoral']=np.log(df['cholestoral'])
    df['log_age']=np.log(df['age'])
    df['log_heart_rate']=np.log(df['heart_rate'])
    df=df[['age','log_age','sex','chest','pressure','log_pressure','cholestoral','log_cholestoral','sugar',\
        'cardiographic','heart_rate','log_heart_rate','angina','oldpeak','slope','flourosopy','thal','target']]
    return df
def thal_data():
    path=os.path.abspath('.')+"/data/heart/processed.cleveland.data"
    chest_pain={'1.0':"typical angin",'2.0':"atypical angina",'3.0':"non-anginal pain","4.0":"asymptomatic"}
    cardiographic={'0.0':"normal",'1.0':"having ST-T",'2.0':"probable or definite"}
    thal={'3.0':"normal",'6.0':"fixed defect",'7.0':"reversable defect",'?':"?"}
    names=['age','sex','chest','pressure','cholestoral','sugar',\
        'cardiographic','heart_rate','angina','oldpeak','slope','flourosopy','thal','target']        
    df = pd.read_csv(path, delimiter=',',float_precision='high',header=None,names=names)
    df=df.drop(df[(df['thal']=='?')|(df['flourosopy']=='?')].index)
    df=df.drop(columns=['target'],axis=1)
    df.iloc[:,1]= df.iloc[:,1].map(lambda x: 1 if x == 1 else 0)
    df['log_pressure'] = np.log(df['pressure'])
    df['log_cholestoral']=np.log(df['cholestoral'])
    df['log_age']=np.log(df['age'])
    df['log_heart_rate']=np.log(df['heart_rate'])
    df=df[['age','log_age','sex','chest','pressure','log_pressure','cholestoral','log_cholestoral','sugar',\
        'cardiographic','heart_rate','log_heart_rate','angina','oldpeak','slope','flourosopy','thal']]
    return df
