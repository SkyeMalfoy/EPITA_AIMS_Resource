#!/usr/bin/python3

import math
import json
import random
import pandas as pd
from sklearn.cluster import KMeans


matrix = pd.read_csv("iris.data",usecols=[0,1,2,3])

print(matrix)

for k in range(2,11):
    kmeans = KMeans(n_clusters=k).fit(matrix)
    print(kmeans.cluster_centers_)
    print(kmeans.labels_)

