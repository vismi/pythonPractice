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
#print(df.head()) #DataFrame

from sklearn import preprocessing

#set Mean and Std Deviation to Standardization Scaler instance
std_scale = preprocessing.StandardScaler().fit(df[['Alcohol', 'Malic acid']])
#scale data frame according to set Mean and Std Deviation parameters, using Standardization Scaler instance
df_std = std_scale.transform(df[['Alcohol', 'Malic acid']])

#set min and max values from Data Frame to MinMaxScaler instance
minmax_scale = preprocessing.MinMaxScaler().fit(df[['Alcohol', 'Malic acid']])
#scale data frame according to set min and max values, using Min Max Scaler instance
df_minmax = minmax_scale.transform(df[['Alcohol', 'Malic acid']])

print(df_std) #converted to numpy array
#Mean of data set lies at 0 now
print('mean of Alcohol, using Standardization Scaler = {:.2f}'.format(df_std[:,0].mean()))
print('mean of Malic Acid, using Standardization Scaler = {:.2f}'.format(df_std[:,1].mean()))

print('mean of Alcohol, using MinMax Scaler = {:.2f}'.format(df_minmax[:,0].mean())) #means are not set to 0 by transformation
print('mean of Malic Acid, using MinMax Scaler = {:.2f}'.format(df_minmax[:,1].mean())) #means are not set to 0 by transformation

#Min-Max standardizes all values to fall between 1 and 0

print('Min-value after min-max scaling:\nAlcohol={:.2f}, Malic acid={:.2f}'
      .format(df_minmax[:,0].min(), df_minmax[:,1].min()))
print('\nMax-value after min-max scaling:\nAlcohol={:.2f}, Malic acid={:.2f}'
      .format(df_minmax[:,0].max(), df_minmax[:,1].max()))


#plotting graphs


import matplotlib.pyplot as plt


def plot():
    plt.figure(figsize=(10,10)) #size of the graph

    plt.scatter(df['Alcohol'], df['Malic acid'], color='green', label='input scale', alpha=0.5) #input

    plt.scatter(df_std[:,0], df_std[:,1], color='red', label='Standardized [$N  (\mu=0, \; \sigma=1)$]', alpha=0.3) #standardization

    plt.scatter(df_minmax[:,0], df_minmax[:,1], color='blue', label='min-max scaled [min=0, max=1]', alpha=0.3) #normalization

    plt.title('Alcohol and Malic Acid content of the wine dataset')
    plt.xlabel('Alcohol')
    plt.ylabel('Malic Acid')
    plt.legend(loc='upper left')
    plt.grid()
    #plt.tight_layout()


plot()
plt.show()


#plots using input, Normalized input and Standardized input to differentiate the three classes

fig, ax = plt.subplots(3, figsize=(6,14))

for a,d,l in zip(range(len(ax)),
               (df[['Alcohol', 'Malic acid']].values, df_std, df_minmax), #values for d, array of graph data
               ('Input scale',
                'Standardized [$N  (\mu=0, \; \sigma=1)$]',
                'min-max scaled [min=0, max=1]')            #values for l, label for the graph
                ):
    for i,c in zip(range(1,4), ('red', 'blue', 'green')):  #looping over the three classes, for individual graph type
        ax[a].scatter(d[df['Class label'].values == i, 0],
                  d[df['Class label'].values == i, 1],
                  alpha=0.5,
                  color=c,
                  label='Class %s' %i
                  )
    ax[a].set_title(l)
    ax[a].set_xlabel('Alcohol')
    ax[a].set_ylabel('Malic Acid')
    ax[a].legend(loc='upper left')
    ax[a].grid()

plt.tight_layout()

plt.show()
