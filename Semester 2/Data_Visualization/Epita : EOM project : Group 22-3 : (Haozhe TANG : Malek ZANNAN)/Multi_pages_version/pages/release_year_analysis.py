#！/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time  : 27/07/2022  17:47
@Author: Skye
@File  : release_year_analysis.py 
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt


st.set_page_config(page_title="Analytics according to release year of works", page_icon="0⃣️")
st.sidebar.success("Select a page to view different analytics.")
df = pd.read_csv("/Users/skyemalfoy/Desktop/Final_projet/Multi-pages-version/netflix_info.csv")

#Data cleaning
df['director'] = df['director'].fillna("Unknown")
df['cast'] = df['cast'].fillna("Unknown")
df['country'] = df['country'].fillna("Unknown")
df['rating'] = df['rating'].fillna("Unknown")
df['duration'] = df['duration'].fillna("Unknown")

#Seperate dataframe for movie and show
movie_df = df[df['type'] == 'Movie']
show_df = df[df['type'] == 'TV Show']


#-----------chart 4---------
df_selected = df.value_counts(['release_year', 'type'])

year = []
amount = []
types = []

df_selected = df_selected.sort_index(ascending=True)

for i in df_selected.index:
    year.append(i[0])
    types.append(i[1])

for i in df_selected:
    amount.append(i)

df4 = pd.DataFrame({
    "Year": year,
    "Amount": amount,
    "Type": types
})

fig4 = px.line(df4, x='Year', y='Amount', color='Type', line_group="Type", title="The amount of TV Show and Movie released on Netflix")
fig4.update_layout(
    title_font=dict(size=26, color='#8a8d93', family="Lato, sans-serif", ),
    plot_bgcolor='#333',
    paper_bgcolor='#444',
    legend=dict(orientation="h", yanchor="bottom", y=1, xanchor="center", x=0.5),
    font=dict(color='#8a8d93'),
)

#------Slider-------
year_for_slider = []
df_select_slider_prepare = df.value_counts(['release_year', 'country'])
df_select_slider_prepare = df_select_slider_prepare.sort_index()

for i in df_select_slider_prepare.index:
    if i[1] == 'Unknown':
        df_select_slider_prepare = df_select_slider_prepare.drop(i)
        continue
    else:
        year_for_slider.append(i[0])

year_for_slider = list(set(year_for_slider))

#----layout-----

#----The amount of TV Show and Movie released on NetFlix.-----
st.write("## The amount of TV Show and Movie released on NetFlix each year")
st.write('''<b>x-Year, y-Amount</b> <br/>
It shows that whether Movies or TV shows had not some much products before <b>2000</b> but after that moment the amount produced every year soared amazingly, but the number of movie production dropped significantly after <b>2018</b>.''', unsafe_allow_html=True)
fig4
st.write("      ")
st.write("      ")


#----Slider of year which can select a specific year and it will show the top 10 countries' amount of release.(Lolipop)----
st.write("## Slider of year")
st.write('''Slider of year which can select a specific year and it will return the lolipop graph shows the top 10 countries' amount of release.''')
st.write('''<b>x-amount, y-countries</b> <br/>
''', unsafe_allow_html=True)
st.title("Slider for year to choose")
year_slider_selected = st.select_slider("Please choose a year:", options=year_for_slider, value=2021)
st.write("The year you chose is :", year_slider_selected)


fig_slider, ax = plt.subplots(1, figsize=(15, 10))

country_slider = []
df_select_slider = df_select_slider_prepare.loc[year_slider_selected].sort_values(ascending=False)

# 国家数
if len(df_select_slider.index) > 10:
    amount_coutry_slider = 10
    country_slider_prepare = df_select_slider.index[:10]
    for i in country_slider_prepare:
        if "," in i:
            i = i.replace(',', '\n').lstrip(' ')
        country_slider.append(i)
    amount_contents_slider = df_select_slider.values[:10]
else:
    amount_coutry_slider = len(df_select_slider.index)
    country_slider = df_select_slider.index
    amount_contents_slider = df_select_slider.values

# 颜色设置：
colors = ["k", "#696969", 'b', 'c', 'g', 'm', 'r', 'y', "#FFE4C4", "#FFD700"][:amount_coutry_slider]

plt.bar(country_slider, amount_contents_slider, color=colors, width=0.05)
plt.scatter(country_slider, amount_contents_slider, color=colors, s=40)
plt.title('Top 10 countries produced contents in the year: {0}'.format(year_slider_selected))
plt.xticks(fontsize=13.3)
plt.xlabel('Country')
plt.ylabel('Amount')

fig_slider


