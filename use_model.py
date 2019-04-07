import pandas
import numpy as np
import pickle
from math import log

# the model use here is logistic_cv_with_log
def predict_1(age,sex,chest,pressure,cholestoral,sugar,cardiographic,heart_rate,angina,oldpeak,slope,flourosopy,thal):
    model=pickle.load(open('logistic_regression_with_log.sav','rb'))
    x=np.array([log(age),sex,chest,log(pressure),log(cholestoral),sugar,cardiographic,log(heart_rate),angina,oldpeak,slope,flourosopy,thal]).reshape(1,13)
    a=model.predict(x)
    return a.item(0)


def predict_2(age,sex,chest,pressure,cholestoral,sugar,cardiographic,heart_rate,angina,oldpeak,slope,flourosopy,thal):
    model=pickle.load(open('logistic_regression_without_log.sav','rb'))
    x=np.array([age,sex,chest,pressure,cholestoral,sugar,cardiographic,heart_rate,angina,oldpeak,slope,flourosopy,thal]).reshape(1,13)
    a=model.predict(x)
    return a.item(0)

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


print(predict_1(63,1,1,145,233,1,2,150,0,2.3,3,0,6))
print(predict_2(63,1,1,145,233,1,2,150,0,2.3,3,0,6))
print(predict_3(63,1,1,145,233,1,2,150,0,2.3,3,0,6))
print(predict_4(63,1,1,145,233,1,2,150,0,2.3,3,0,6))