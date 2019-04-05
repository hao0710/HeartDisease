
# an example to read model from logistic.py
import pickle
from read_data import *
from sklearn.model_selection import train_test_split
from logistic import *

##import the data file , here I use original data as an example and use logistic_regression_with_log.sav
def use_logistic_with_log(modle_file):
    loaded_model=pickle.load(open(modle_file,'rb'))
    # assume we have new dataset,apply the clean_data_function
    data=clean_data()
    x=data.drop(['target','pressure','cholestoral','age','heart_rate'],axis=1)
    y=data['target']
    result=loaded_model.score(x,y)
    print(result)


def use_logistic_without_log(modle_file):
    loaded_model=pickle.load(open(modle_file,'rb'))
    # assume we have new dataset,apply the clean_data_function
    data=clean_data()
    x=data.drop(['target','log_pressure','log_cholestoral','log_age','log_heart_rate'],axis=1)
    y=data['target']
    result=loaded_model.score(x,y)
    print(result)

use_logistic_with_log('logistic_regression_with_log.sav')
use_logistic_without_log('logistic_regression_without_log.sav')