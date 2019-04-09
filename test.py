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
    # print(cardiographic_dataset)