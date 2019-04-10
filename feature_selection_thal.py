import pandas as pd
from read_data import *
import numpy as np
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import SelectFromModel
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

#Function to create Train and Test set from the original dataset def getTrainTestData(dataset,split):

data=thal_data()
x=data.drop(['thal'],axis=1)
y=data['thal']
print(len(x.columns))
# x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=5)
model = ExtraTreesClassifier()
model.fit(x,y)
print(model.feature_importances_)
#plot graph of feature importances for better visualization
feat_importances = pd.Series(model.feature_importances_, index=x.columns)
feat_importances.nlargest(16).plot(kind='barh')
plt.show()