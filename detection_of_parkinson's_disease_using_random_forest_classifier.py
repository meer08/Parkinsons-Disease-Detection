# -*- coding: utf-8 -*-
"""Detection_of_Parkinson's_disease_using_Random_Forest_Classifier.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xsNfa-YBpp2gkIEN-GRLqMZV8Hxe0beA
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from google.colab import files
uploadedfiles=files.upload()

data = pd.read_csv('parkinsons.data')
data.head()

features=data.loc[:,data.columns!='status'].values[:,1:]
labels=data.loc[:,'status'].values

scaler=MinMaxScaler((-1,1))
x=scaler.fit_transform(features)
y=labels

# Fitting Random Forest Regression to the dataset
X_train,X_test,y_train,y_test = train_test_split(x,y,test_size=0.25,random_state=0)
# import the classifier
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(n_estimators=100)
clf.fit(X_train,y_train)
y_pred=clf.predict(X_test)

import seaborn as sn
confusion_matrix = pd.crosstab(y_test, y_pred, rownames=['Actual'], colnames=['Predicted'])
sn.heatmap(confusion_matrix, annot=True)

from sklearn import metrics
print('Accuracy: ',metrics.accuracy_score(y_test, y_pred))