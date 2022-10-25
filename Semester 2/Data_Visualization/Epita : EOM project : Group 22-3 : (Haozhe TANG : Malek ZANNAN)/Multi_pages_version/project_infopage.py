#！/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time  : 27/07/2022  17:12
@Author: Skye
@File  : project_info.py 
"""

import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="Project Information",
    page_icon="👋",
)

st.write("# 🎬Netflix and IMDb datasets analytics and visualization🎬")
st.sidebar.success("Select a page to view different analytics.")
st.write("### Work of: <br/>Haozhe TANG <br/>Malek ZANNAN", unsafe_allow_html=True)
st.write('<b>We did 12 graphs and one crawler, which are:</b> <br/>', unsafe_allow_html=True)
st.write('''<ol>
<li> Two dragdown box and one slider </li>
<li> One map and two wordcloud graphs </li>
<li> Two pie charts ( One single, one double )</li>
<li> Four bar charts (Three vertical, one horizontal) </li>
<li> One categorized line chart </li>
''', unsafe_allow_html=True)
st.write('#### <b>Thanks for checking our work. Hope you like what we have done, professor.</b>', unsafe_allow_html=True)
df = pd.read_csv("/Users/skyemalfoy/Desktop/Final_projet/Multi-pages-version/netflix_info.csv")

df['director'] = df['director'].fillna("Unknown")
df['cast'] = df['cast'].fillna("Unknown")
df['country'] = df['country'].fillna("Unknown")
df['rating'] = df['rating'].fillna("Unknown")
df['duration'] = df['duration'].fillna("Unknown")

#------------Layout------------------
#----dataset-----
st.write("## Dataset of Netflix")
st.write('''### Columns  &  Descriptions
- **show_id**: Unique ID for every Movie / TV Show
- **type**: Identifier - A Movie or TV Show
- **title**: Title of the Movie / TV Show
- **director**: Director of the Movie
- **cast**: Actors involved in the movie/show
- **country**: Country where the movie/show was produced
- **release_year**: Actual Release year of the movie/show
- **rating**: TV Rating of the Movie/TV Show
- **duration**: Total Duration - in minutes or number of seasons
- **listed_in**: Genre
- **description**: The summary description''')
df