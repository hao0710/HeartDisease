def thal(df):
    # male>60
    df_male_60 = df[(df['age'] > 60) & (df['sex'] == 1)]
    df_thal_m_60 = df_male_60['thal']
    thal_m_60 = df_thal_m_60.value_counts()
    thal_m_60 = thal_m_60.to_json()
    # female>60
    df_female_60 = df[(df['age'] > 60) & (df['sex'] == 0)]
    df_thal_f_60 = df_female_60['thal']
    thal_f_60 = df_thal_f_60.value_counts()
    thal_f_60 = thal_f_60.to_json()

    #  male 40-60
    df_male_4060 = df[(df['age'] <= 60) & (df["age"] >=40) & (df['sex'] == 1)]
    df_thal_m_4060 = df_male_4060['thal']
    thal_m_4060 = df_thal_m_4060.value_counts()
    thal_m_4060 = thal_m_4060.to_json()
    # feamle 40-60
    df_female_4060 = df[(df['age'] > 60) & (df['sex'] == 0)]
    df_thal_f_4060 = df_female_4060["thal"]
    thal_f_4060 = df_thal_f_4060.value_counts()
    thal_f_4060 = thal_f_4060.to_json()
    # male <40
    df_male_40 = df[(df['age'] < 40) & (df['sex'] == 1)]
    df_thal_m_40 = df_male_40['thal']
    thal_m_40 = df_thal_m_40.value_counts()
    thal_m_40 = thal_m_40.to_json()
    # feamle <40
    df_female_40 = df[(df['age'] > 40) & (df['sex'] == 0)]
    df_thal_f_40 = df_female_40['thal']
    thal_f_40 = df_thal_f_40.value_counts()
    thal_f_40 = thal_f_40.to_json()
    thal_dataset = {"male":{"<40": thal_m_40,"40-60": thal_m_4060, ">60": thal_m_60},"female":{"<40": thal_f_40,"40-60": thal_f_4060, ">60": thal_f_60}}
    print(thal_dataset)