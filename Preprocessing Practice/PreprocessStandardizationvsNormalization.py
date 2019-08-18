import pandas as pd
import numpy as np

#load wine data set, reading only Alcohol and Malic acid information
df = pd.io.parsers.read_csv(
    'Data/wine.data',
     header=None,
     usecols=[0,1,2]
    )

df.columns=['Class label', 'Alcohol', 'Malic acid']

#Alcohol (percent/volumne) and Malic acid (g/l) are measured on different scales
print(df.head())

from sklearn import preprocessing

std_scale = preprocessing.StandardScaler().fit(df[['Alcohol', 'Malic acid']])
df_std = std_scale.transform(df[['Alcohol', 'Malic acid']])

minmax_scale = preprocessing.MinMaxScaler().fit(df[['Alcohol', 'Malic acid']])
df_minmax = minmax_scale.transform(df[['Alcohol', 'Malic acid']])
