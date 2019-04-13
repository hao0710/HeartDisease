import pandas
import numpy as np
import pickle
from math import log

# the model use here is logistic_cv_with_log
def predict_final(age,sex,chest,pressure,cholestoral,heart_rate,oldpeak,floursopy):
    model=pickle.load(open('final_model.sav','rb'))
    x=np.array([log(age),sex,chest,pressure,log(pressure),cholestoral,log(cholestoral),heart_rate,log(heart_rate),oldpeak,floursopy]).reshape(1,11)
    a=model.predict(x)
    if a.item(0)=='7' or a.item(0)=='7.0' :
    	return 'reversable defect'
    if a.item(0)=='6' or a.item(0)=='6.0':
    	return " fixed defect"
    if a.item(0)=='3' or a.item(0)=='3.0':
    	return "normal"
    
    #return a.item(0)

print(predict_final(63,1,1,145,150,2.3,3,0))