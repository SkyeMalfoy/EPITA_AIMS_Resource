#！/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time  : 13/07/2022  15:32
@Author: Skye
@File  : map.py 
"""

import pandas as pd
import numpy as np
import map_draw
from snapshot_selenium import snapshot
from pyecharts.render import make_snapshot

df = pd.read_csv("/Users/skyemalfoy/Desktop/Final_projet/Final_codes/netflix_info.csv")
# st.write("# 🎬Netflix dataset analytics and visualization🎬")
#Data cleaning
df['director'] = df['director'].fillna("Unknown")
df['cast'] = df['cast'].fillna("Unknown")
df['country'] = df['country'].fillna("Unknown")
df['rating'] = df['rating'].fillna("Unknown")
df['duration'] = df['duration'].fillna("Unknown")
countries = []
country_df = df['country']

for i in country_df:
    if "," in i:
        country_multiple = i.split(",")
        for j in country_multiple:
            j = j.lstrip(" ")
            countries.append(j)
    elif i == "Unknown":
        continue
    else:
        countries.append(i)

df_map_prepare = pd.DataFrame({
    "country": countries
})
map_country = []
map_value = []
map_value_counts_prepare = df_map_prepare.value_counts()

for i in map_value_counts_prepare.index:
    #     print(i[0])
    map_country.append(i[0])
for i in map_value_counts_prepare.values:
    map_value.append(str(i))


map = map_draw.Draw_map()
map_get = map.draw_the_world(map_country, map_value)
make_snapshot(snapshot, map_get.render(), 'test.png')