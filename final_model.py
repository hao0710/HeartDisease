import pandas as pd
import numpy as np
import matplotlib
from sklearn.multiclass import OutputCodeClassifier
from sklearn.svm import LinearSVC
from read_data import *
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LogisticRegressionCV
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.linear_model import RidgeClassifierCV
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn import linear_model
from sklearn.linear_model import Perceptron
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV, StratifiedKFold, train_test_split
from sklearn.naive_bayes import MultinomialNB
import pickle
def naive_bayess_selected_feature():
    raw_frame=thal_data()
    # name=raw_frame.drop(['sugar','age','cardiographic','angina','slope','thal'],axis=1).columns
    x=raw_frame.drop(['sugar','age','cardiographic','angina','slope','thal'],axis=1).values
    y=raw_frame['thal'].values
    # x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=5)
    clf = GaussianNB().fit(x,y)
    filename='final_model.sav'
    pickle.dump(lr,open(filename,'wb'))
    # print(name)
    # print(clf.predict(x_test))

naive_bayess_selected_feature()