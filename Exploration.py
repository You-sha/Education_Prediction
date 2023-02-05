# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 17:02:52 2023

@author: Yousha
"""

import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns
plt.style.use('ggplot')
pd.set_option('display.max_columns', 10)
pd.set_option('display.width', None)


df = pd.read_csv('Cleaned_data.csv')
df = df.drop('Unnamed: 0', axis= 1)

df.shape
df.columns
df.dtypes
df.describe()
df.head()
df.isna().sum()
df_corr = df.corr()

## Visualisations ##


# Univariate

ed = df['Education'].value_counts() \
    .plot(kind='bar', title='Education level')
ed.set_xlabel('Degree')
ed.set_ylabel('Counts')

inc = df['Income'].plot(kind='hist',
                  bins=50,
                  title='Income')
inc.set_xlabel('Amount')
inc.set_ylabel('Counts')

inc = df['Income'].plot(kind='kde',
                  title='Income')
inc.set_xlabel('Amount')
inc.set_ylabel('Counts')


# Multivariate

sns.scatterplot(x='MntFishProducts', y='Income', 
                data=df, hue='Education',
                )

sns.pairplot(df, hue='Education')
sns.heatmap(df_corr, annot=True)




















