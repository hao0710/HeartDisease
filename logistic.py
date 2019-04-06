import csv
import pandas as pd
import os
import numpy as np
from read_data import *
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report,accuracy_score,confusion_matrix
import statsmodels.api as sm
import pickle
from sklearn.metrics import r2_score
from sklearn.linear_model import LogisticRegressionCV

#achieved with 0.8444444444444444 with test_size 0.3
def logistic_regression_without_log():
    raw_frame=clean_data()
    x=raw_frame.drop(['target','log_pressure','log_cholestoral','log_age','log_heart_rate'],axis=1)
    y=raw_frame['target']
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=5)
    lr=LogisticRegression(solver='liblinear')
    lr.fit(x_train,y_train)
    y_pred=lr.predict(x_test)
    # confusion=confusion_matrix(y_test, y_pred)
    # print('here is confusion_matrix')
    # print(confusion)
    # print('report')
    # print(classification_report(y_test,y_pred))
    # print('here is accuracy_score')
    # print(accuracy_score(y_test,y_pred))
    # filename='logistic_regression_without_log.sav'
    # pickle.dump(lr,open(filename,'wb'))

    pass


#achieve accurancy with 0.8555555555555555 with test_size 0.3
def logistic_regression_with_log():
    raw_frame=clean_data()
    x=raw_frame.drop(['target','pressure','cholestoral','age','heart_rate'],axis=1)
    y=raw_frame['target']
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=5)
    lr=LogisticRegression(solver='liblinear')
    lr.fit(x_train,y_train)
    y_pred=lr.predict(x_test)
    # print(classification_report(y_test,y_pred))
    #print(accuracy_score(y_test,y_pred))
    # print(accuracy_score(y_test,y_pred))
    # filename='logistic_regression_with_log.sav'
    # pickle.dump(lr,open(filename,'wb'))
    pass


#achieved with score 0.8585858585858586
def logistic_cv_without_log():
    raw_frame=clean_data()
    x=raw_frame.drop(['target','log_pressure','log_cholestoral','log_age','log_heart_rate'],axis=1)
    y=raw_frame['target']
    clf=LogisticRegressionCV(cv=5, random_state=5,multi_class='ovr',max_iter=1000,solver='liblinear').fit(x, y)
    # print(clf.score(x, y))
    # filename='logistic_cv_without_log.sav'
    # pickle.dump(clf,open(filename,'wb'))


#achieved with 0.8518518518518519
def logistic_cv_with_log():
    raw_frame=clean_data()
    x=raw_frame.drop(['target','pressure','cholestoral','heart_rate','age'],axis=1)
    y=raw_frame['target']
    clf=LogisticRegressionCV(cv=5, random_state=5,multi_class='ovr',max_iter=1000,solver='liblinear').fit(x, y)
#     print(clf.score(x, y))
#     filename='logistic_cv_with_log.sav'
#     pickle.dump(clf,open(filename,'wb'))
# logistic_regression_without_log()
# logistic_cv_without_log()
# logistic_regression_with_log()
# logistic_cv_with_log()

