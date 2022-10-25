#！/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time  : 27/07/2022  17:10
@Author: Skye
@File  : country_analysis.py
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

st.set_page_config(page_title="Analytics according to country", page_icon="🇫🇷")
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


#----------Dragdown2--------
drag_2_movie_prepare = movie_df.value_counts(['country', 'release_year'])
drag_2_tv_prepare = show_df.value_counts(['country', 'release_year'])

#Make the list of countries in drag-down selectbox.
drag_2_country_select = []
for i in drag_2_movie_prepare.index:
    if i[0] == "Unknown":
        drag_2_movie_prepare = drag_2_movie_prepare.drop(i)
for j in drag_2_tv_prepare.index:
    if j[0] == "Unknown":
        drag_2_tv_prepare = drag_2_tv_prepare.drop(j)
for i in drag_2_movie_prepare.index:
    if "," in i[0]:
        drag_2_country_select.append(i[0][:i[0].find(",")])
drag_2_country_select = list(set(drag_2_country_select))

drag_2_year = []
drag_2_amount = []
drag_2_type = []
drag_2_df_country_mv_new = pd.DataFrame(columns=['Year_mv', "Amount_mv"])
drag_2_df_country_tv_new = pd.DataFrame(columns=['Year_tv', "Amount_tv"])

#------Bar chart to show the Top 10 number of works for actors.----
cast_count = df['cast'].value_counts()
actors = cast_count[1:11]
labels_work = []
for i in actors.index:
    if "," in i:
        i = i.replace(',', '\n').lstrip(' ')
        labels_work.append(i)
    else:
        labels_work.append(i)

fig5 = plt.figure(figsize=(18, 10), dpi=100)

sns.barplot(x=labels_work, y=cast_count.values[1:11], data=actors, palette='coolwarm_r')
sns.set(font_scale=2, color_codes=True)
plt.xticks(fontsize=12)
plt.yticks(range(0, 21))
plt.title('Bar chart to show the most casted actor on NetFlix', fontsize=26, weight='semibold')
plt.xlabel("Actors' name", fontsize=24)
plt.ylabel('Count', fontsize=24)



movie_df = df[df['type'] == 'Movie']
show_df = df[df['type'] == 'TV Show']



#-----------chart 1---------
df_country = df['country'].value_counts()
df_country.pop('Unknown')

df2 = pd.DataFrame({
    "countries": df_country.index[0:10],
    'count_countries': df_country[0:10]
})

fig1 = px.bar(df2, x="countries", y="count_countries", color='countries', title="Top 10 countries produce works on NetFlix")

fig1.update_layout(
    title_font=dict(size=30, color='#8a8d93', family="Lato, sans-serif", ),
    plot_bgcolor='#333',
    paper_bgcolor='#444',
    legend=dict(orientation="h", yanchor="bottom", y=1, xanchor="center", x=0.5),
    font=dict(color='#8a8d93'),

)


#-----------map------------
map_image = Image.open('/Users/skyemalfoy/Desktop/Final_projet/Photos/map.png')

#------Number of contents by country showed by movie and TV show-----
data_country = df.groupby(['country']).count()['show_id'].to_frame().reset_index()
data_country = data_country.sort_values('show_id',ascending=False)
data_country = data_country.head(5).reset_index(drop=True)
list_c = data_country['country']
top_8_data = df[df['country'].isin(list_c)]
year_with_show = top_8_data.groupby(['country','type']).count()['show_id'].to_frame().reset_index()
year_with_show = year_with_show.sort_values(by = 'show_id', ascending= False)


plt.style.use('seaborn-pastel')
fig7 = plt.figure(figsize=(20,10))
sns.barplot(x="country", y="show_id", hue="type",data= year_with_show)
plt.xlabel("")
plt.title('Shows by Country')
plt.ylabel("Amount")


#------layout--------
#------Top 10 countries produce works on NetFlix.-------
st.write("## Top 10 countries produce works on NetFlix.")
st.write('''<b>x-Country, y-Amount</b> <br/>
We can see that throughout the years, the two leaders in content producing are the <b>US</b> and <b>India</b>.<br/>
This can be easily explained because of the potential market these countries represent and the habits of consuming.<br/>
Cinema is a very important subject and a very profitable field for US and for Bollywood.<br/>
We can see from the graph that the <b>US</b> produced the most contents on Netflex even as nearly three times as india did.''', unsafe_allow_html=True)
fig1
st.write("      ")
st.write("      ")

#----A drag-down box that select a country and display contents they produced each year.----
st.write('## A drag-down box that select a country and display contents they produced each year.')
st.write('''<b>x-Year, y-Amount</b>''', unsafe_allow_html=True)
st.write('''All the countries followed the same trend regarding the amount of content produced throughout the years.<br/>
The year 2020 was very significant with a big overall dip due to the pandemic.<br/>
The production companies decided to slow down the speed of production and extend the publication period.''', unsafe_allow_html=True)
select_box2 = st.selectbox('Please select a country:', drag_2_country_select, index=0)
st.write("The country selected now is:", select_box2)

#Find the certain series in the DataFrame and build a unique dataframe
for i in drag_2_movie_prepare.index:
    if select_box2 in i[0]:
        row_mv = {
           'Year_mv': i[1],
           'Amount_mv': drag_2_movie_prepare[i]
    }
        drag_2_df_country_mv_new = drag_2_df_country_mv_new.append(row_mv, ignore_index=True)

for i in drag_2_tv_prepare.index:
    if select_box2 in i[0]:
        row_tv = {
           'Year_tv': i[1],
           'Amount_tv': drag_2_tv_prepare[i]
    }
        drag_2_df_country_tv_new = drag_2_df_country_tv_new.append(row_tv, ignore_index=True)

#Group the dataseries according to year and let it be the dataframe of drawing graph.
drag_2_df_country_mv_new = drag_2_df_country_mv_new.groupby('Year_mv')['Amount_mv'].sum()
drag_2_df_country_tv_new = drag_2_df_country_tv_new.groupby('Year_tv')['Amount_tv'].sum()

#DataFrame Preperation

for i in drag_2_df_country_mv_new.index:
    drag_2_year.append(i)
    drag_2_amount.append(drag_2_df_country_mv_new[i])
    drag_2_type.append("Movie")

for i in drag_2_df_country_tv_new.index:
    drag_2_year.append(i)
    drag_2_amount.append(drag_2_df_country_tv_new[i])
    drag_2_type.append("TV Show")

df_drag_2 = pd.DataFrame({
    "Year": drag_2_year,
    "Amount": drag_2_amount,
    "Type": drag_2_type
})

#Draw figure
drag_2_fig = px.line(df_drag_2, x='Year', y='Amount', color='Type', line_group="Type", title="The amount of contents in years of {0}".format(select_box2))
drag_2_fig.update_layout(
    title_font=dict(size=30, color='#8a8d93', family="Lato, sans-serif"),
    plot_bgcolor='#333',
    paper_bgcolor='#444',
    legend=dict(orientation="h", yanchor="bottom", y=1, xanchor="center", x=0.5),
    font=dict(color='#8a8d93'),
)
drag_2_fig
st.write("      ")
st.write("      ")



#----Map the show the countries produce works.----
st.write("## Map to show countries produce works.")
st.write('#### The more contents they produced, the darker that country on the map will be.')
st.write('''It reveals that the <b>US</b> and <b>India</b> have the darkest color, which means they producted the most contents on Netflix. Besides, most of countries contributed <b>less than 100</b> contents on Netflix''', unsafe_allow_html=True)
# st_pyecharts(map_get)
st.image(map_image)
st.write("      ")
st.write("      ")

#-----Bar chart shows the number of contents in top5 countries--------
st.write("## Bar chart shows the number of contents in top5 countries")
st.write('''We can clearly see that the “movie-business” is mainly runed by <b>Hollywood</b> and <b>Bollywood</b>.<br/>
They’re focusing on quality products.<br/>
However, we can notice that the rest of the world is focusing on <b>TV-Shows</b> based on quantity of release.''', unsafe_allow_html=True)
fig7
