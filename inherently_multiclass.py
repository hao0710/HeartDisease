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


train_score=[]
test_score=[]

def naive_bayes_cv_with_log():
    raw_frame=thal_data()
    x=raw_frame.drop(['thal','pressure','cholestoral','heart_rate','age'],axis=1).values
    y=raw_frame['thal'].values
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=5)
    params = {}
    skf = StratifiedKFold(n_splits=5)
    nb = MultinomialNB().fit(x_train,y_train)
    gs = GridSearchCV(nb, cv=skf, param_grid=params, return_train_score=True,iid=False).fit(x_train,y_train)
    global train_score
    train_score.append(gs.score(x_train,y_train))
    global test_score
    test_score.append(gs.score(x_test,y_test))
def naive_bayes_cv_selected_feature():
    raw_frame=thal_data()
    x=raw_frame.drop(['sugar','age','cardiographic','angina','slope','thal'],axis=1).values
    y=raw_frame['thal'].values
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=5)
    params = {}
    skf = StratifiedKFold(n_splits=5)
    nb = MultinomialNB().fit(x_train,y_train)
    gs = GridSearchCV(nb, cv=skf, param_grid=params, return_train_score=True,iid=False).fit(x_train,y_train)
    global train_score
    train_score.append(gs.score(x_train,y_train))
    global test_score
    test_score.append(gs.score(x_test,y_test))
def naive_bayes_cv_with_all():
    raw_frame=thal_data()
    x=raw_frame.drop(['thal'],axis=1).values
    y=raw_frame['thal'].values
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=5)
    params = {}
    skf = StratifiedKFold(n_splits=5)
    nb = MultinomialNB().fit(x_train,y_train)
    gs = GridSearchCV(nb, cv=skf, param_grid=params, return_train_score=True,iid=False).fit(x_train,y_train)
    global train_score
    train_score.append(gs.score(x_train,y_train))
    global test_score
    test_score.append(gs.score(x_test,y_test))
def naive_bayes_cv_without_log():
    raw_frame=thal_data()
    x=raw_frame.drop(['thal','log_pressure','log_cholestoral','log_heart_rate','log_age'],axis=1).values
    y=raw_frame['thal'].values
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=5)
    params = {}
    skf = StratifiedKFold(n_splits=5)
    nb = MultinomialNB().fit(x_train,y_train)
    gs = GridSearchCV(nb, cv=skf, param_grid=params, return_train_score=True,iid=False).fit(x_train,y_train)
    global train_score
    train_score.append(gs.score(x_train,y_train))
    global test_score
    test_score.append(gs.score(x_test,y_test))

def knn_all():
    raw_frame=thal_data()
    x=raw_frame.drop(['thal'],axis=1).values
    y=raw_frame['thal'].values
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=5)
    neigh = KNeighborsClassifier(n_neighbors=3).fit(x_train, y_train)
    global train_score
    train_score.append(neigh.score(x_train,y_train))
    global test_score
    test_score.append(neigh.score(x_test,y_test))
def knn_without_log():
    raw_frame=thal_data()
    x=raw_frame.drop(['thal','log_pressure','log_cholestoral','log_heart_rate','log_age'],axis=1)
    y=raw_frame['thal']
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=5)
    neigh = KNeighborsClassifier(n_neighbors=3).fit(x_train, y_train)
    global train_score
    train_score.append(neigh.score(x_train,y_train))
    global test_score
    test_score.append(neigh.score(x_test,y_test))    
def knn_with_log():
    raw_frame=thal_data()
    x=raw_frame.drop(['thal','pressure','cholestoral','heart_rate','age'],axis=1)
    y=raw_frame['thal']
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=5)    
    neigh = KNeighborsClassifier(n_neighbors=3).fit(x_train, y_train)
    global train_score
    train_score.append(neigh.score(x_train,y_train))
    global test_score
    test_score.append(neigh.score(x_test,y_test))
def knn_selected_feature():
    raw_frame=thal_data()
    x=raw_frame.drop(['sugar','age','cardiographic','angina','slope','thal','log_cholestoral'],axis=1)
    y=raw_frame['thal']
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=5)    
    neigh = KNeighborsClassifier(n_neighbors=3).fit(x_train, y_train)
    global train_score
    train_score.append(neigh.score(x_train,y_train))
    global test_score
    test_score.append(neigh.score(x_test,y_test))

def naive_bayess_with_all():
    raw_frame=thal_data()
    x=raw_frame.drop(['thal'],axis=1).values
    y=raw_frame['thal'].values
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=5)
    clf = GaussianNB().fit(x_train,y_train)
    global train_score
    train_score.append(clf.score(x_train,y_train))
    global test_score
    test_score.append(clf.score(x_test,y_test))

def naive_bayess_without_log():
    raw_frame=thal_data()
    x=raw_frame.drop(['thal','log_pressure','log_cholestoral','log_heart_rate','log_age'],axis=1).values
    y=raw_frame['thal'].values
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=5)
    clf = GaussianNB().fit(x_train,y_train)
    global train_score
    train_score.append(clf.score(x_train,y_train))
    global test_score
    test_score.append(clf.score(x_test,y_test))
def naive_bayess_with_log():
    raw_frame=thal_data()
    x=raw_frame.drop(['thal','pressure','cholestoral','heart_rate','age'],axis=1).values
    y=raw_frame['thal'].values
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=5)
    clf = GaussianNB().fit(x_train,y_train)
    global train_score
    train_score.append(clf.score(x_train,y_train))
    global test_score
    test_score.append(clf.score(x_test,y_test))
#this is the best one
def naive_bayess_selected_feature():
    raw_frame=thal_data()
    x=raw_frame.drop(['sugar','age','cardiographic','angina','slope','thal'],axis=1).values
    y=raw_frame['thal'].values
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=5)
    clf = GaussianNB().fit(x_train,y_train)
    global train_score
    train_score.append(clf.score(x_train,y_train))
    global test_score
    test_score.append(clf.score(x_test,y_test))
def multi_logistic_with_all():
    raw_frame=thal_data()
    x=raw_frame.drop(['thal'],axis=1)
    y=raw_frame['thal']
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=5) 
    clf = LogisticRegression(random_state=0, solver='lbfgs',multi_class='multinomial',max_iter=10000).fit(x_train, y_train)
    global train_score
    train_score.append(clf.score(x_train,y_train))
    global test_score
    test_score.append(clf.score(x_test,y_test))
def multi_logistic_without_log():
    raw_frame=thal_data()
    x=raw_frame.drop(['thal','log_pressure','log_cholestoral','log_heart_rate','log_age'],axis=1)
    y=raw_frame['thal']
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=5) 
    clf = LogisticRegression(random_state=0, solver='lbfgs',multi_class='multinomial',max_iter=10000).fit(x_train, y_train)
    global train_score
    train_score.append(clf.score(x_train,y_train))
    global test_score
    test_score.append(clf.score(x_test,y_test))
def multi_logistic_with_log():
    raw_frame=thal_data()
    x=raw_frame.drop(['thal','pressure','cholestoral','heart_rate','age'],axis=1)
    y=raw_frame['thal']
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=5) 
    clf = LogisticRegression(random_state=0, solver='lbfgs',multi_class='multinomial',max_iter=10000).fit(x_train, y_train)
    global train_score
    train_score.append(clf.score(x_train,y_train))
    global test_score
    test_score.append(clf.score(x_test,y_test))
def multi_logistic_selected_feature():
    raw_frame=thal_data()
    x=raw_frame.drop(['sugar','age','cardiographic','angina','slope','thal','log_cholestoral'],axis=1)
    y=raw_frame['thal']
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=5) 
    clf = LogisticRegression(random_state=0, solver='lbfgs',multi_class='multinomial',max_iter=10000).fit(x_train, y_train)
    global train_score
    train_score.append(clf.score(x_train,y_train))
    global test_score
    test_score.append(clf.score(x_test,y_test))
def multi_logsitc_cv_with_all():
    raw_frame=thal_data()
    x=raw_frame.drop(['thal'],axis=1)
    y=raw_frame['thal']
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=5)
    clf = LogisticRegressionCV(cv=10, random_state=0, multi_class='multinomial',max_iter=10000).fit(x_train, y_train)
    global train_score
    train_score.append(clf.score(x_train,y_train))
    global test_score
    test_score.append(clf.score(x_test,y_test))
def multi_logsitc_cv_with_log():
    raw_frame=thal_data()
    x=raw_frame.drop(['thal','pressure','cholestoral','heart_rate','age'],axis=1)
    y=raw_frame['thal']
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=5)
    clf = LogisticRegressionCV(cv=10, random_state=0, multi_class='multinomial',max_iter=10000).fit(x_train, y_train)
    global train_score
    train_score.append(clf.score(x_train,y_train))
    global test_score
    test_score.append(clf.score(x_test,y_test))
def multi_logsitc_cv_without_log():
    raw_frame=thal_data()
    x=raw_frame.drop(['thal','log_pressure','log_cholestoral','log_age','log_heart_rate'],axis=1)
    y=raw_frame['thal']
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=5)
    clf = LogisticRegressionCV(cv=5, random_state=0, multi_class='multinomial',max_iter=10000).fit(x_train, y_train)
    global train_score
    train_score.append(clf.score(x_train,y_train))
    global test_score
    test_score.append(clf.score(x_test,y_test))
def quadratic_discriminant_analysis_without_log():
    raw_frame=thal_data()
    x=raw_frame.drop(['thal','log_pressure','log_cholestoral','log_heart_rate','log_age'],axis=1).values
    y=raw_frame['thal'].values
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=5)
    clf = QuadraticDiscriminantAnalysis().fit(x_train,y_train)
    global train_score
    train_score.append(clf.score(x_train,y_train))
    global test_score
    test_score.append(clf.score(x_test,y_test))
def quadratic_discriminant_analysis_with_log():
    raw_frame=thal_data()
    x=raw_frame.drop(['thal','pressure','cholestoral','heart_rate','age'],axis=1).values
    y=raw_frame['thal'].values
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=5)
    clf = QuadraticDiscriminantAnalysis().fit(x_train,y_train)
    global train_score
    train_score.append(clf.score(x_train,y_train))
    global test_score
    test_score.append(clf.score(x_test,y_test))

def ridge_classfier_cv_withoulog():
    raw_frame=thal_data()
    x=raw_frame.drop(['thal','log_pressure','log_cholestoral','log_age','log_heart_rate'],axis=1)
    y=raw_frame['thal']
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=5)
    clf = RidgeClassifierCV(alphas=[1e-3, 1e-2, 1e-1, 1]).fit(x_train, y_train)
    global train_score
    train_score.append(clf.score(x_train,y_train))
    global test_score
    test_score.append(clf.score(x_test,y_test))
def ridge_classfier_cv_withlog():
    raw_frame=thal_data()
    x=raw_frame.drop(['thal','pressure','cholestoral','age','heart_rate'],axis=1)
    y=raw_frame['thal']
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=5)
    clf = RidgeClassifierCV(alphas=[1e-3, 1e-2, 1e-1, 1]).fit(x_train, y_train)
    global train_score
    train_score.append(clf.score(x_train,y_train))
    global test_score
    test_score.append(clf.score(x_test,y_test))
# from here use one vs all
def support_vector_classfication_withlog():
    raw_frame=thal_data()
    x=raw_frame.drop(['thal','pressure','cholestoral','age','heart_rate'],axis=1).values
    y=raw_frame['thal'].values
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=5)
    clf = SVC(gamma='auto').fit(x_train,y_train)
    global train_score
    train_score.append(clf.score(x_train,y_train))
    global test_score
    test_score.append(clf.score(x_test,y_test))
def support_vector_classfication_withoutlog():
    raw_frame=thal_data()
    x=raw_frame.drop(['thal','log_pressure','log_cholestoral','log_age','log_heart_rate'],axis=1).values
    y=raw_frame['thal'].values
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=5)
    clf = SVC(gamma='auto').fit(x_train,y_train)
    global train_score
    train_score.append(clf.score(x_train,y_train))
    global test_score
    test_score.append(clf.score(x_test,y_test))
def gauss_process_with_log():
    raw_frame=thal_data()
    x=raw_frame.drop(['thal','pressure','cholestoral','age','heart_rate'],axis=1)
    y=raw_frame['thal']
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=5)    
    kernel = 1.0 * RBF(1.0)
    gpc = GaussianProcessClassifier(kernel=kernel,random_state=0).fit(x_train, y_train)
    global train_score
    train_score.append(gpc.score(x_train,y_train))
    global test_score
    test_score.append(gpc.score(x_test,y_test))
def gauss_process_without_log():
    raw_frame=thal_data()
    x=raw_frame.drop(['thal','log_pressure','log_cholestoral','log_age','log_heart_rate'],axis=1)
    y=raw_frame['thal']
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=5)    
    kernel = 1.0 * RBF(1.0)
    gpc = GaussianProcessClassifier(kernel=kernel,random_state=0).fit(x_train, y_train)
    global train_score
    train_score.append(gpc.score(x_train,y_train))
    global test_score
    test_score.append(gpc.score(x_test,y_test))
## from here use one vs all
def one_vs_rest_gauss_process_with_log():
    raw_frame=thal_data()
    x=raw_frame.drop(['thal','pressure','cholestoral','age','heart_rate'],axis=1)
    y=raw_frame['thal']
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=5)    
    kernel = 1.0 * RBF(1.0)
    gpc = GaussianProcessClassifier(kernel=kernel,random_state=0, multi_class = 'one_vs_rest').fit(x_train, y_train)
    global train_score
    train_score.append(gpc.score(x_train,y_train))
    global test_score
    test_score.append(gpc.score(x_test,y_test))
def one_vs_rest_multi_logistic_with_log():
    raw_frame=thal_data()
    x=raw_frame.drop(['thal','pressure','cholestoral','heart_rate','age'],axis=1)
    y=raw_frame['thal']
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=5) 
    clf = LogisticRegression(random_state=0, solver='lbfgs',multi_class='ovr',max_iter=10000).fit(x_train, y_train)
    global train_score
    train_score.append(clf.score(x_train,y_train))
    global test_score
    test_score.append(clf.score(x_test,y_test))
def one_vs_rest_multi_logistic_without_log():
    raw_frame=thal_data()
    x=raw_frame.drop(['thal','log_pressure','log_cholestoral','log_heart_rate','log_age'],axis=1)
    y=raw_frame['thal']
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=5) 
    clf = LogisticRegression(random_state=0, solver='lbfgs',multi_class='ovr',max_iter=10000).fit(x_train, y_train)
    global train_score
    train_score.append(clf.score(x_train,y_train))
    global test_score
    test_score.append(clf.score(x_test,y_test))
def one_vs_rest_multi_logsitc_cv_with_log():
    raw_frame=thal_data()
    x=raw_frame.drop(['thal','pressure','cholestoral','heart_rate','age'],axis=1)
    y=raw_frame['thal']
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=5)
    clf = LogisticRegressionCV(cv=10, random_state=0, multi_class='ovr',max_iter=10000).fit(x_train, y_train)
    global train_score
    train_score.append(clf.score(x_train,y_train))
    global test_score
    test_score.append(clf.score(x_test,y_test))
def one_vs_rest_multi_logsitc_cv_without_log():
    raw_frame=thal_data()
    x=raw_frame.drop(['thal','log_pressure','log_cholestoral','log_age','log_heart_rate'],axis=1)
    y=raw_frame['thal']
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=5)
    clf = LogisticRegressionCV(cv=5, random_state=0, multi_class='ovr',max_iter=10000).fit(x_train, y_train)
    global train_score
    train_score.append(clf.score(x_train,y_train))
    global test_score
    test_score.append(clf.score(x_test,y_test))
def sgd_classifer_without_log():
    raw_frame=thal_data()
    x=raw_frame.drop(['thal','log_pressure','log_cholestoral','log_age','log_heart_rate'],axis=1).values
    y=raw_frame['thal'].values
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=5)
    clf = linear_model.SGDClassifier(max_iter=1000, tol=1e-3).fit(x_train, y_train)
    global train_score
    train_score.append(clf.score(x_train,y_train))
    global test_score
    test_score.append(clf.score(x_test,y_test))
def sgd_classifer_with_log():
    raw_frame=thal_data()
    x=raw_frame.drop(['thal','pressure','cholestoral','age','heart_rate'],axis=1).values
    y=raw_frame['thal'].values
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=5)
    clf = linear_model.SGDClassifier(max_iter=1000, tol=1e-3).fit(x_train, y_train)
    global train_score
    train_score.append(clf.score(x_train,y_train))
    global test_score
    test_score.append(clf.score(x_test,y_test))
def perception_withlog():
    raw_frame=thal_data()
    x=raw_frame.drop(['thal','log_pressure','log_cholestoral','log_age','log_heart_rate'],axis=1)
    y=raw_frame['thal']
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=5)
    clf = Perceptron(tol=1e-3, random_state=0).fit(x_train,y_train)
    global train_score
    train_score.append(clf.score(x_train,y_train))
    global test_score
    test_score.append(clf.score(x_test,y_test))  
def perception_withoutlog():
    raw_frame=thal_data()
    x=raw_frame.drop(['thal','pressure','cholestoral','age','heart_rate'],axis=1)
    y=raw_frame['thal']
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=5)
    clf = Perceptron(tol=1e-3, random_state=0).fit(x_train,y_train)
    global train_score
    train_score.append(clf.score(x_train,y_train))
    global test_score
    test_score.append(clf.score(x_test,y_test))    
def decosion_tree_withlog():
    raw_frame=thal_data()
    x=raw_frame.drop(['thal','pressure','cholestoral','age','heart_rate'],axis=1)
    y=raw_frame['thal']
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=5)
    clf = DecisionTreeClassifier(random_state=0).fit(x_train,y_train)
    global train_score
    train_score.append(clf.score(x_train,y_train))
    global test_score
    test_score.append(clf.score(x_test,y_test))
def decosion_tree_withoutlog():
    raw_frame=thal_data()
    x=raw_frame.drop(['thal','log_pressure','log_cholestoral','log_age','log_heart_rate'],axis=1)
    y=raw_frame['thal']
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=5)
    clf = DecisionTreeClassifier(random_state=0).fit(x_train,y_train)
    global train_score
    train_score.append(clf.score(x_train,y_train))
    global test_score
    test_score.append(clf.score(x_test,y_test))
def ridge_classfier_cv_selected_feature():
    raw_frame=thal_data()
    x=raw_frame.drop(['sugar','age','cardiographic','angina','slope','thal','log_cholestoral'],axis=1)
    y=raw_frame['thal']
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=5)
    clf = RidgeClassifierCV(alphas=[1e-3, 1e-2, 1e-1, 1]).fit(x_train, y_train)
    global train_score
    train_score.append(clf.score(x_train,y_train))
    global test_score
    test_score.append(clf.score(x_test,y_test))
def one_vs_rest_multi_logisitc_selected_feature():
    raw_frame=thal_data()
    x=raw_frame.drop(['sugar','age','cardiographic','angina','slope','thal','log_cholestoral'],axis=1)
    y=raw_frame['thal']
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=5)
    clf = LogisticRegressionCV(cv=10, random_state=0, multi_class='ovr',max_iter=10000).fit(x_train, y_train)
    global train_score
    train_score.append(clf.score(x_train,y_train))
    global test_score
    test_score.append(clf.score(x_test,y_test))
def quadratic_discriminant_analysis_selected_feature():
    raw_frame=thal_data()
    x=raw_frame.drop(['sugar','age','cardiographic','angina','slope','thal','log_cholestoral'],axis=1).values
    y=raw_frame['thal'].values
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=5)
    clf = QuadraticDiscriminantAnalysis().fit(x_train,y_train)
    global train_score
    train_score.append(clf.score(x_train,y_train))
    global test_score
    test_score.append(clf.score(x_test,y_test))
def sgd_classifer_selected_feature():
    raw_frame=thal_data()
    x=raw_frame.drop(['sugar','age','cardiographic','angina','slope','thal','log_cholestoral'],axis=1).values
    y=raw_frame['thal'].values
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=5)
    clf = linear_model.SGDClassifier(max_iter=1000, tol=1e-3).fit(x_train, y_train)
    global train_score
    train_score.append(clf.score(x_train,y_train))
    global test_score
    test_score.append(clf.score(x_test,y_test))
def perception_selected_feature():
    raw_frame=thal_data()
    x=raw_frame.drop(['sugar','age','cardiographic','angina','slope','thal','log_cholestoral'],axis=1)
    y=raw_frame['thal']
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=5)
    clf = Perceptron(tol=1e-3, random_state=0).fit(x_train,y_train)
    global train_score
    train_score.append(clf.score(x_train,y_train))
    global test_score
    test_score.append(clf.score(x_test,y_test))
def decosion_tree_selected_feature():
    raw_frame=thal_data()
    x=raw_frame.drop(['sugar','age','cardiographic','angina','slope','thal','log_cholestoral'],axis=1)
    y=raw_frame['thal']
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=5)
    clf = DecisionTreeClassifier(random_state=0).fit(x_train,y_train)

    global train_score
    train_score.append(clf.score(x_train,y_train))
    global test_score
    test_score.append(clf.score(x_test,y_test))

naive_bayess_selected_feature()
print(test_score)







