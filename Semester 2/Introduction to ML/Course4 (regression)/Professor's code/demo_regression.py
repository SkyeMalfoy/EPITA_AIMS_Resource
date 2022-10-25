#!/usr/bin/python3

import math
import json
import random
import pandas as pd
from sklearn import linear_model
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.preprocessing import MinMaxScaler

import matplotlib.pyplot as plt
import sys

pd.options.mode.chained_assignment = None 

def toNumeric(x):
  #return x.map({"no":0,"yes":1})
  return x.map({"no":0,"yes":1,"unfurnished":0,"semi-furnished":0.5,"furnished":1})


def convert_binary(data): 
  for column in list(data.select_dtypes(['object']).columns):
    data[[column]] = data[[column]].apply(toNumeric)
  return data
     


matrix = pd.read_csv("price_houses_full_train.csv")
matrix_test = pd.read_csv("price_houses_full_test.csv")

data_size = len(matrix)

print(data_size)


def split_train(data_train, nfolds):
    df_train_to_return = []
    df_test_to_return = []
    n_size = int((len(data_train) / nfolds)+1)
    #print(n_size)
    start = 0
    for l_inc in range(nfolds):
      end = start + n_size
      if end > len(data_train):
          end = len(data_train)
      test_filtered = data_train.iloc[start:end,:]
      train_filtered = data_train
      for l_index in range(start,end):
          train_filtered = train_filtered.drop([l_index])
      start = end
      #print("********************** head test", test_filtered.head())
      #print("********************** head train", train_filtered.head())
      #print("info test", len(test_filtered))
      #print("info train", len(train_filtered))
      df_train_to_return.append(train_filtered)
      df_test_to_return.append(test_filtered)

    return df_train_to_return, df_test_to_return



def train_and_test(data_train, data_test):
    #scaler = MinMaxScaler()
    scaler = MinMaxScaler(feature_range=[0,10000])


    scaled_train_x = data_train[['bedrooms','bathrooms','area','parking']]
    scaled_test_x = data_test[['bedrooms','bathrooms','area','parking']]
    train_binary_x = data_train[['mainroad','guestroom','basement','hotwaterheating','airconditioning','prefarea','furnishingstatus']]
    test_binary_x = data_test[['mainroad','guestroom','basement','hotwaterheating','airconditioning','prefarea','furnishingstatus']]
    #print(train_binary_x.info())
    #print(train_binary_x.head())

    train_binary_encoded_x = convert_binary(train_binary_x)
    test_binary_encoded_x = convert_binary(test_binary_x)

    #print(train_binary_encoded_x.info())
    #print(train_binary_encoded_x.head())

    train_full_x = pd.concat([scaled_train_x,train_binary_encoded_x],axis=1)
    test_full_x = pd.concat([scaled_test_x,test_binary_encoded_x],axis=1)

    scaled_train_y = data_train[['price']]
    scaled_test_y = data_test[['price']]

    scaler.fit(train_full_x)
    train_full_x = scaler.transform(train_full_x)
    scaled_test_x = scaler.transform(test_full_x)

    scaled_regression = linear_model.LinearRegression()
    scaled_regression.fit(train_full_x,scaled_train_y)

    scaled_predictions = scaled_regression.predict(scaled_test_x)
    
    #print(scaled_regression.coef_)
    #print(scaled_regression.intercept_)
    #print("MAE", mean_absolute_error(scaled_test_y,scaled_predictions))
    #print("MSE", mean_squared_error(scaled_test_y,scaled_predictions))
    return mean_absolute_error(scaled_test_y,scaled_predictions), mean_squared_error(scaled_test_y,scaled_predictions)


#fig = matrix.hist(bins=50, figsize=(10, 8))
#plt.show()
#fig = matrix_test.hist(bins=50, figsize=(10, 8))
#plt.show()


print(matrix.info())

#matrix_filtered = matrix.loc[(matrix["area"] < 10001)]

#print(matrix_filtered.info())

#train_filtered_x = matrix_filtered[['bedrooms','bathrooms','area','parking']]
#train_filtered_y = matrix_filtered[['price']]

num_folds = 10

splitted_train, splitted_test = split_train(matrix,num_folds)

#results = []
for l_inc in range(num_folds):
    MAE, MSE = train_and_test(splitted_train[l_inc], splitted_test[l_inc])
    print("Fold number",l_inc)
    print("MAE:",MAE)
    print("MSE:",MSE)
#print(results)

#train_and_test(matrix, matrix_test)



#train_and_test(matrix_filtered, matrix_test)






