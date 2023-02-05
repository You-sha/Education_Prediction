# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 17:52:44 2023

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
df = df.drop('Unnamed: 0', axis=1)
dummy_vars = pd.get_dummies(df['Marital_Status'])
dummy_vars = dummy_vars[['Divorced', 'Married', 'Single', 'Together', 'Widow']]
#df_new = pd.concat([df,dummy_vars],axis=0)
#df.drop('Marital_Status', axis=1, inplace= True)

## Models
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

model = LogisticRegression(solver='liblinear')

X = df.drop(['Marital_Status','Education'],axis=1)
y = df['Education']

X_train,X_test,Y_train,Y_test = train_test_split(X,y,test_size=0.3,random_state=1)

model.fit(X_train,Y_train)

model.score(X_test,Y_test)
