import pandas
import numpy as np
import pickle
from math import log

# the model use here is logistic_cv_with_log


def predict_3(age,sex,chest,pressure,cholestoral,sugar,cardiographic,heart_rate,angina,oldpeak,slope,flourosopy,thal):
    model=pickle.load(open('logistic_cv_with_log.sav','rb'))
    x=np.array([log(age),sex,chest,log(pressure),log(cholestoral),sugar,cardiographic,log(heart_rate),angina,oldpeak,slope,flourosopy,thal]).reshape(1,13)
    a=model.predict(x)
    return a.item(0)    
def predict_4(age,sex,chest,pressure,cholestoral,sugar,cardiographic,heart_rate,angina,oldpeak,slope,flourosopy,thal):
    model=pickle.load(open('logistic_cv_without_log.sav','rb'))
    x=np.array([age,sex,chest,pressure,cholestoral,sugar,cardiographic,heart_rate,angina,oldpeak,slope,flourosopy,thal]).reshape(1,13)
    a=model.predict(x)
    return a.item(0) 
def predict_final(age,sex,chest,pressure,cholestoral,heart_rate,oldpeak,floursopy):
    model=pickle.load(open('final_model.sav','rb'))
    x=np.array([log(age),sex,chest,pressure,log(pressure),cholestoral,log(cholestoral),heart_rate,log(heart_rate),oldpeak,floursopy]).reshape(1,11)
    a=model.predict(x)
    return a.item(0)

print(predict_final(63,1,1,145,150,2.3,3,0))