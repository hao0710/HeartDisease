import csv
import pandas as pd
import os
import numpy as np

def clean_data():
    path = os.path.abspath('.')+"/data/heart/processed.cleveland.data"
    chest_pain = {'1.0':"typical angin",'2.0':"atypical angina",'3.0':"non-anginal pain","4.0":"asymptomatic"}
    cardiographic = {'0.0':"normal",'1.0':"having ST-T",'2.0':"probable or definite"}
    thal = {'3.0':"normal",'6.0':"fixed defect",'7.0':"reversable defect",'?':"?"}
    names = ['age','sex','chest','pressure','cholestoral','sugar',\
        'cardiographic','heart_rate','angina','oldpeak','slope','flourosopy','thal','target']        
    df = pd.read_csv(path, delimiter=',',float_precision='high',header=None,names=names)
    df = df.drop(df[(df['thal']=='?')|(df['flourosopy']=='?')].index)
    df.iloc[:,1]= df.iloc[:,1].map(lambda x: 1 if x == 1 else 0)
    df.iloc[:,13]= df.iloc[:,13].map(lambda x: 0 if x == 0 else 1)
    # df['log_pressure'] = np.log(df['pressure'])
    # df['log_cholestoral']=np.log(df['cholestoral'])
    # df['log_age']=np.log(df['age'])
    # df['log_heart_rate']=np.log(df['heart_rate'])
    df = df[['age','sex','chest','pressure','cholestoral','sugar',\
        'cardiographic','heart_rate','angina','oldpeak','slope','flourosopy','thal','target']]
    return df

def pressure(df):
    df_male = df[df['sex'] == 1]
    df_female = df[df['sex'] == 0]
    male_pressure_list = []
    female_pressure_list = []
    for index,row in df_male[['age', 'pressure']].iterrows():
        for column_name in df_male[['age', 'pressure']].columns:
            male_pressure_set = {"x": row['age'],"y": row['pressure']}
            male_pressure_list.append(male_pressure_set)
    for index,row in df_female[['age', 'pressure']].iterrows():
        for column_name in df_female[['age', 'pressure']].columns:
            female_pressure_set = {"x": row['age'],"y": row['pressure']}
            female_pressure_list.append(female_pressure_set)
    pressure_dataset = {"male": male_pressure_list, "female": female_pressure_list}
    print(pressure_dataset)

def chest(df):
    # male>60
    df_male_60 = df[(df['age'] > 60) & (df['sex'] == 1)]
    df_chest_m_60 = df_male_60['chest']
    chest_m_60 = df_chest_m_60.value_counts()
    chest_m_60 = chest_m_60.to_json()
    # female>60
    df_female_60 = df[(df['age'] > 60) & (df['sex'] == 0)]
    df_chest_f_60 = df_female_60['chest']
    chest_f_60 = df_chest_f_60.value_counts()
    chest_f_60 = chest_f_60.to_json()

    #  male 40-60
    df_male_4060 = df[(df['age'] <= 60) & (df["age"] >=40) & (df['sex'] == 1)]
    df_chest_m_4060 = df_male_4060['chest']
    chest_m_4060 = df_chest_m_4060.value_counts()
    chest_m_4060 = chest_m_4060.to_json()
    # feamle 40-60
    df_female_4060 = df[(df['age'] > 60) & (df['sex'] == 0)]
    df_chest_f_4060 = df_female_4060["chest"]
    chest_f_4060 = df_chest_f_4060.value_counts()
    chest_f_4060 = chest_f_4060.to_json()
    # male <40
    df_male_40 = df[(df['age'] < 40) & (df['sex'] == 1)]
    df_chest_m_40 = df_male_40['chest']
    chest_m_40 = df_chest_m_40.value_counts()
    chest_m_40 = chest_m_40.to_json()
    # feamle <40
    df_female_40 = df[(df['age'] > 40) & (df['sex'] == 0)]
    df_chest_f_40 = df_female_40['chest']
    chest_f_40 = df_chest_f_40.value_counts()
    chest_f_40 = chest_f_40.to_json()
    chest_dataset = {"male":{"<40": chest_m_40,"40-60": chest_m_4060, ">60": chest_m_60},"female":{"<40": chest_f_40,"40-60": chest_f_4060, ">60": chest_f_60}}
    print(chest_dataset)

def cholestoral(df):
    df_male = df[df['sex'] == 1]
    df_female = df[df['sex'] == 0]
    male_cholestoral_list = []
    female_cholestoral_list = []
    for index,row in df_male[['age', 'cholestoral']].iterrows():
        for column_name in df_male[['age', 'cholestoral']].columns:
            male_cholestoral_set = {"x": row['age'],"y": row['cholestoral']}
            male_cholestoral_list.append(male_cholestoral_set)
    for index,row in df_female[['age', 'cholestoral']].iterrows():
        for column_name in df_female[['age', 'cholestoral']].columns:
            female_cholestoral_set = {"x": row['age'],"y": row['cholestoral']}
            female_cholestoral_list.append(female_cholestoral_set)
    cholestoral_dataset = {"male": male_cholestoral_list, "female": female_cholestoral_list}
    # print(cholestoral_dataset)
    
def heart_rate(df):
    df_male = df[df['sex'] == 1]
    df_female = df[df['sex'] == 0]
    male_heart_rate_list = []
    female_heart_rate_list = []
    for index,row in df_male[['age', 'heart_rate']].iterrows():
        for column_name in df_male[['age', 'heart_rate']].columns:
            male_heart_rate_set = {"x": row['age'],"y": row['heart_rate']}
            male_heart_rate_list.append(male_heart_rate_set)
    for index,row in df_female[['age', 'heart_rate']].iterrows():
        for column_name in df_female[['age', 'heart_rate']].columns:
            female_heart_rate_set = {"x": row['age'],"y": row['heart_rate']}
            female_heart_rate_list.append(female_heart_rate_set)
    heart_rate_dataset = {"male": male_heart_rate_list, "female": female_heart_rate_list}
    print(heart_rate_dataset)

def oldpeak(df):
    df_male = df[df['sex'] == 1]
    df_female = df[df['sex'] == 0]
    male_oldpeak_list = []
    female_oldpeak_list = []
    for index,row in df_male[['age', 'oldpeak']].iterrows():
        for column_name in df_male[['age', 'oldpeak']].columns:
            male_oldpeak_set = {"x": row['age'],"y": row['oldpeak']}
            male_oldpeak_list.append(male_oldpeak_set)
    for index,row in df_female[['age', 'oldpeak']].iterrows():
        for column_name in df_female[['age', 'oldpeak']].columns:
            female_oldpeak_set = {"x": row['age'],"y": row['oldpeak']}
            female_oldpeak_list.append(female_oldpeak_set)
    oldpeak_dataset = {"male": male_oldpeak_list, "female": female_oldpeak_list}
    print(oldpeak_dataset)

def sugar(df):
    # male>60
    df_male_60 = df[(df['age'] > 60) & (df['sex'] == 1)]
    df_sugar_m_60 = df_male_60['sugar']
    sugar_m_60 = df_sugar_m_60.value_counts()
    sugar_m_60 = sugar_m_60.to_json()
    # female>60
    df_female_60 = df[(df['age'] > 60) & (df['sex'] == 0)]
    df_sugar_f_60 = df_female_60['sugar']
    sugar_f_60 = df_sugar_f_60.value_counts()
    sugar_f_60 = sugar_f_60.to_json()
    # print(sugar_f_60)
    #  male 40-60
    df_male_4060 = df[(df['age'] <= 60) & (df["age"] >=40) & (df['sex'] == 1)]
    df_sugar_m_4060 = df_male_4060['sugar']
    sugar_m_4060 = df_sugar_m_4060.value_counts()
    sugar_m_4060 = sugar_m_4060.to_json()
    # print(sugar_m_4060)
    # feamle 40-60
    df_female_4060 = df[(df['age'] <= 60) & (df["age"] >=40) & (df['sex'] == 0)]
    df_sugar_f_4060 = df_female_4060["sugar"]
    # print(df_sugar_f_4060)
    sugar_f_4060 = df_sugar_f_4060.value_counts()
    # print(sugar_f_4060)
    sugar_f_4060 = sugar_f_4060.to_json()
    
    # male <40
    df_male_40 = df[(df['age'] < 40) & (df['sex'] == 1)]
    df_sugar_m_40 = df_male_40['sugar']
    sugar_m_40 = df_sugar_m_40.value_counts()
    sugar_m_40 = sugar_m_40.to_json()
    # feamle <40
    df_female_40 = df[(df['age'] < 40) & (df['sex'] == 0)]
    df_sugar_f_40 = df_female_40['sugar']
    sugar_f_40 = df_sugar_f_40.value_counts()
    sugar_f_40 = sugar_f_40.to_json()
    sugar_dataset = {"male":{"<40": sugar_m_40,"40-60": sugar_m_4060, ">60": sugar_m_60},"female":{"<40": sugar_f_40,"40-60": sugar_f_4060, ">60": sugar_f_60}}
    print(sugar_dataset)

def cardiographic(df):
    # male>60
    df_male_60 = df[(df['age'] > 60) & (df['sex'] == 1)]
    df_cardiographic_m_60 = df_male_60['cardiographic']
    cardiographic_m_60 = df_cardiographic_m_60.value_counts()
    cardiographic_m_60 = cardiographic_m_60.to_json()
    # female>60
    df_female_60 = df[(df['age'] > 60) & (df['sex'] == 0)]
    df_cardiographic_f_60 = df_female_60['cardiographic']
    cardiographic_f_60 = df_cardiographic_f_60.value_counts()
    cardiographic_f_60 = cardiographic_f_60.to_json()

    #  male 40-60
    df_male_4060 = df[(df['age'] <= 60) & (df["age"] >=40) & (df['sex'] == 1)]
    df_cardiographic_m_4060 = df_male_4060['cardiographic']
    cardiographic_m_4060 = df_cardiographic_m_4060.value_counts()
    cardiographic_m_4060 = cardiographic_m_4060.to_json()
    # feamle 40-60
    df_female_4060 = df[(df['age'] > 60) & (df['sex'] == 0)]
    df_cardiographic_f_4060 = df_female_4060["cardiographic"]
    cardiographic_f_4060 = df_cardiographic_f_4060.value_counts()
    cardiographic_f_4060 = cardiographic_f_4060.to_json()
    # male <40
    df_male_40 = df[(df['age'] < 40) & (df['sex'] == 1)]
    df_cardiographic_m_40 = df_male_40['cardiographic']
    cardiographic_m_40 = df_cardiographic_m_40.value_counts()
    cardiographic_m_40 = cardiographic_m_40.to_json()
    # feamle <40
    df_female_40 = df[(df['age'] > 40) & (df['sex'] == 0)]
    df_cardiographic_f_40 = df_female_40['cardiographic']
    cardiographic_f_40 = df_cardiographic_f_40.value_counts()
    cardiographic_f_40 = cardiographic_f_40.to_json()
    cardiographic_dataset = {"male":{"<40": cardiographic_m_40,"40-60": cardiographic_m_4060, ">60": cardiographic_m_60},"female":{"<40": cardiographic_f_40,"40-60": cardiographic_f_4060, ">60": cardiographic_f_60}}
    print(cardiographic_dataset)

if __name__ == "__main__":
    df = clean_data()
    # chest(df)
    # pressure(df)
    # cholestoral(df)
    # heart_rate(df)
    # oldpeak(df)
    sugar(df)
    cardiographic(df)