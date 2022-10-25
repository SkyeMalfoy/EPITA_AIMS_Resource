#!/usr/bin/python3

import math
import json
import random
import pandas as pd
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

matrix = pd.read_csv("iris.data", header=None)

print(matrix)

shuffle_matrix = matrix.sample(frac=1)

print(shuffle_matrix)

shuffle_matrix_x = shuffle_matrix.iloc[:,:4]
shuffle_matrix_y = shuffle_matrix.iloc[:,4:]

train_x, evaluation_x, train_y, evaluation_y = train_test_split(shuffle_matrix_x, shuffle_matrix_y, test_size = 0.10)

print(train_x.shape)
print(train_y.shape)

print(evaluation_x.shape)
print(evaluation_y.shape)

model = svm.SVC(kernel='linear')
model.fit(train_x,train_y)
prediction_y = model.predict(evaluation_x)
print(prediction_y)

results = classification_report(evaluation_y, prediction_y)
print(results)


