#！/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time  : 27/07/2022  18:13
@Author: Skye
@File  : IMDb_analysis.py 
"""


import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Analytics according to IMDb dataset", page_icon="🕷️")
st.sidebar.success("Select a page to view different analytics.")

#Pie chart to show the ratio of amount of movie in different ranges.
df_IMDb = pd.read_csv('/Users/skyemalfoy/Desktop/Final_projet/Multi-pages-version/IMDB_data.csv')
#Group the rating
bins = [8.0, 8.2, 8.4, 8.6, 8.8, 9.0, 9.2, 9.4]
segment = pd.cut(df_IMDb['score'], bins, right=False)
IMDb_count = pd.value_counts(segment, sort=False)
#Make dataframe
df_IMDb_pie = pd.DataFrame({
    'Range': ['8.0-8.1', '8.2-8.3', '8.4-8.5', '8.6-8.7', '8.8-8.9', '9.0-9.1', '9.2-9.3'],
    "Amount": IMDb_count.values
})
#Draw pie chart
fig_IMDb_pie = px.pie(df_IMDb_pie, labels="Range", values="Amount", color="Range", title='The ratio of ranges of score of TOP250 movies on IMDb')

fig_IMDb_pie.update_layout(
    title_font=dict(size=25, color='#8a8d93', family="Lato, sans-serif"),
    plot_bgcolor='#333',
    paper_bgcolor='#444',
    legend=dict(orientation="h", yanchor="bottom", y=1, xanchor="center", x=0.5),
    font=dict(color='#8a8d93'),

)



#-----layout------
#Dataset
st.write('## Dataset of IMDb TOP250')
st.write('''A crawler to obtain the titles and rating points from IMDb TOP250 movies (the web crawler) and then display here in the following dataframe''')
st.dataframe(df_IMDb, width=1800)
st.write("      ")
st.write("      ")

#Pie chart
st.write('## Pie chart to show the ratio of ranges of score of TOP250 movies on IMDb')
st.write('''We noticed that <b>nearly half</b> of the movies in IMDb TOP250 list are rated between <b>8.0-8.1</b>;<br/>
then about <b>32%</b> or works are scored <b>8.2-8.3</b>...<br/>
We also noted that <b>the higher score</b> they are rated, <b>the fewer number of works</b> involved.''', unsafe_allow_html=True)
fig_IMDb_pie
