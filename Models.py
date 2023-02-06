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
from sklearn.model_selection import GridSearchCV

X = df.drop(['Marital_Status','Education'],axis=1)
y = df['Education']

X_train,X_test,Y_train,Y_test = train_test_split(X,y,test_size=0.3,random_state=1)

## Logistic Regression
model = LogisticRegression(solver='liblinear')
model.fit(X_train,Y_train)
model.score(X_test,Y_test)  #59.7%


model2 = LogisticRegression(max_iter=10000)
model2.fit(X_train,Y_train)
model2.score(X_test,Y_test)  #58.8%

## K neighbors
knn = KNeighborsClassifier()
param_grid = {'n_neighbors': np.arange(2,11)}
knn_gscv =  GridSearchCV(knn, param_grid, cv=5)
knn_gscv.fit(X,y)
knn_gscv.best_params_  #9

knn_final = KNeighborsClassifier(n_neighbors=knn_gscv.best_params_['n_neighbors'])
knn_final.fit(X,y)
knn_final.score(X,y)  #61%















