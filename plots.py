import csv
import pandas as pd
import os
import numpy as np
from read_data import *
from matplotlib import pyplot as plt
import seaborn as sns
import pickle
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import SelectFromModel
from sklearn.model_selection import train_test_split
from inherently_multiclass import *
import inspect
import sys
##heat map to show the variable correlation
def heatmap():
    frame=clean_data()
    fig=plt.figure(figsize=(10,10))
    plt.suptitle('heatmap')
    sns.heatmap(frame.corr(),annot=True,vmax=0.3,linewidths=0.5,annot_kws={"size": 10})
    plt.show()
    fig.savefig('heatmap.png')



def thal_feature_selection():
    data=thal_data()
    x=data.drop(['thal'],axis=1)
    y=data['thal']
    # x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=5)
    model = ExtraTreesClassifier()
    model.fit(x,y)
    fig=plt.figure(figsize=(10,10))
    plt.suptitle('feature_selection_for_thal')
    print(model.feature_importances_)
    plt.xlabel('importance factor')
    plt.ylabel('feature')
    #plot graph of feature importances for better visualization
    feat_importances = pd.Series(model.feature_importances_, index=x.columns)
    feat_importances.nlargest(10).plot(kind='barh')
    plt.show()
    fig.savefig('selected_feature_for_thal')

def heat_disease_feature_selection():
    data=clean_data()
    x=data.drop(['target'],axis=1)
    y=data['target']
    model = ExtraTreesClassifier()
    model.fit(x,y)
    fig=plt.figure(figsize=(10,10))
    plt.suptitle('selected_feature_for_heart_disease')
    plt.xlabel('importance factor')
    plt.ylabel('feature')
    print(model.feature_importances_)
    #plot graph of feature importances for better visualization
    feat_importances = pd.Series(model.feature_importances_, index=x.columns)
    feat_importances.nlargest(16).plot(kind='barh')
    plt.show()
    fig.savefig('selected_feature_for_heart_disease')
