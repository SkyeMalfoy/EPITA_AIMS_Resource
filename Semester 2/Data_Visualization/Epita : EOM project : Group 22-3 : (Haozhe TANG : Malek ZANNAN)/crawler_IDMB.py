#！/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time  : 16/07/2022  16:19
@Author: Skye
@File  : crawler_IDMB.py 
"""

import requests
import re

url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73"}
response = requests.get(url, headers=headers)
print(response)
response.encoding = "utf-8"
html = response.text

#Create lists for store info
title = []
Rating = []

# print(html)

rel_title = '<img src=.* width=.* height=.* alt="(.*?)"'
rel_rating = '<strong title=.*>(.*?)</strong>'
# title_rel_list = re.findall(rel_title, html)
rating_rel_list = re.findall(rel_rating, html)
print(rating_rel_list)
