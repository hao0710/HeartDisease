import os
import pandas as pd
import numpy as np
from sklearn import preprocessing
import matplotlib
import matplotlib.pyplot as plt 
plt.rc("font", size=14)
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import seaborn as sns
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)

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

df = thal_data()
x = df.drop(['thal'],axis=1)
y = df['thal']

test = SelectKBest(score_func=chi2, k=4)
fit = test.fit(x, y)

np.set_printoptions(precision=3)
print(fit.scores_)
print(type(fit.scores_))

objects = ['age','log_age','sex','chest','pressure','log_pressure','cholestoral','log_cholestoral','sugar',\
	    'cardiographic','heart_rate','log_heart_rate','angina','oldpeak','slope','flourosopy']
performance = fit.scores_
performance,objects = zip(*sorted(zip(performance,objects)))

plt.xlim(-0.1,100)
plt.figure(figsize=(14, 8))
plt.barh(objects, performance, align='center',alpha = 0.9)
plt.yticks(objects, objects)
plt.xlabel('Importance Factor')
plt.title('Thal Feature Factor')
plt.savefig('Thal_feature_factor')
plt.show()

# features = fit.transform(x)
# # Summarize selected features
# print(features[0:5,:])
