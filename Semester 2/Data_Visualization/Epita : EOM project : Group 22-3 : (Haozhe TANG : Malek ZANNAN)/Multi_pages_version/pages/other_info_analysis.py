#！/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time  : 27/07/2022  17:56
@Author: Skye
@File  : other_info_analysis.py 
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from matplotlib import colors
import seaborn as sns
from plotly.subplots import make_subplots
import plotly.graph_objects as go

st.set_page_config(page_title="Analytics according to other info in dataset", page_icon="🔢")
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


#-----------WordCloud-------
description_movie = ''.join(movie_df['description'])
description_tv = ''.join(show_df['description'])
#---------WC_movie----------
plt.figure(figsize=(7,7))
color_list= ['DarkBlue','LightBlue','MediumAquamarine',
              'Plum','OrangeRed','FireBrick','Pink','DarkOrange']

color_map = colors.ListedColormap(color_list)


wordcloud_movie = WordCloud(max_words=80,
                           background_color='white',
                           width=1400,
                           height=1200,
                           colormap=color_map).generate(description_movie)

plt.title("Wordcloud for movies' description", fontsize=20)
# wordcloud_movie.to_file('Wordcloud_movie.png')
movie_image = Image.open('/Users/skyemalfoy/Desktop/Final_projet/Photos/Wordcloud_movie.png')
#---------WC_tv----------
plt.figure(figsize=(7,7))
color_list=['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']

color_map_tv = colors.ListedColormap(color_list)

wordcloud_tv = WordCloud(max_words=120,
                        background_color='#444',
                        width=1400,
                        height=1200,
                        colormap=color_map_tv).generate(description_tv)

plt.title("Wordcloud for tv' description", fontsize=20)
# wordcloud_movie.to_file('Wordcloud_tv.png')
tv_image = Image.open('/Users/skyemalfoy/Desktop/Final_projet/Photos/Wordcloud_tv.png')

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
plt.title('Bar chart to show the most participated workers on NetFlix', fontsize=26, weight='semibold')
plt.xlabel("ame", fontsize=24)
plt.ylabel('Count', fontsize=24)


#------Double Pie chart to show the ratio of ratings between Movies and TV Shows------
ratings_ages = {
    'TV-PG': 'Older Kids',
    'TV-MA': 'Adults',
    'TV-Y7-FV': 'Older Kids',
    'TV-Y7': 'Older Kids',
    'TV-14': 'Teens',
    'R': 'Adults',
    'TV-Y': 'Kids',
    'NR': 'Adults',
    'PG-13': 'Teens',
    'TV-G': 'Kids',
    'PG': 'Older Kids',
    'G': 'Kids',
    'UR': 'Adults',
    'NC-17': 'Adults'
}
movie_df['target_ages'] =movie_df['rating'].replace(ratings_ages)
show_df['target_ages'] =show_df['rating'].replace(ratings_ages)

colors1 = ['#9ed900', '#bce672', '#c9dd22','#bddd22','#c9dd22']
colors2 = ['#ff8c69', '#ffaeb9', '#ffbbff','#ffd39b', '#ffe1ff']

fig_rating = make_subplots(rows=1, cols=2, specs=[[{"type": "pie"}, {"type": "pie"}]])

fig_rating.add_trace(go.Pie(values=movie_df.value_counts(), labels=movie_df['target_ages'],
                     marker_colors=colors1), row=1, col=1)

fig_rating.add_trace(go.Pie(values=show_df.value_counts(), labels=show_df['target_ages'],
                     marker_colors=colors2), row=1, col=2)

fig_rating.update_traces(textposition='inside', hole=0.5, hoverinfo='label+percent+name')
fig_rating.update_layout(title_text='Rating distribution by Type of content',
                  title_x=0.5,
                  title_font=dict(size=20, color='Blue'),
                  annotations=[dict(text='Movies', x=0.18, y=0.5, font_size=16, showarrow=False,
                                      font_color='DarkSlateBlue'),
                                 dict(text='TV Shows', x=0.85, y=0.5, font_size=16,
                                      showarrow=False,font_color = 'DarkSlateBlue')])

#------Duration bar chart-----------
fig6 = plt.figure(figsize=(16, 8), dpi=100)
sns.countplot(y='duration', data=df, order=df['duration'].value_counts()[:10].index)
plt.title("Contents' duration analysis", fontsize=26, weight="semibold")


#-----layout------

#----A drag-down box that can display the information of the selected movie.-----
st.write('## Drag-down box of title')
st.write('A drag-down box that can display the information of the selected movie.')

select_box1 = st.selectbox('Please select a movie you would like to know about:', df['title'])
st.write("Your choice is:", select_box1)
df_title_selected = df[(df['title'] == select_box1)]
st.markdown('''<table>
<tr align="center">
    <td>Name:</td>
    <td>{0}</td>
</tr>
<tr align="center">
    <td>Type:</td>
    <td>{1}</td>
</tr>
<tr align="center">
    <td>Country:</td>
    <td>{2}</td>
</tr>
<tr align="center">
    <td>Actors:</td>
    <td>{3}</td>
</tr>
<tr align="center">
    <td>Director:</td>
    <td>{4}</td>
</tr>
<tr align="center">
    <td>Duration:</td>
    <td>{5}</td>
</tr>
<tr align="center">
    <td>Release Year:</td>
    <td>{6}</td>
</tr>
<tr align="center">
    <td>Rating</td>
    <td>{7}</td>
</tr><tr>
    <td>Description</td>
    <td>{8}</td>
</tr>

</table>'''.format(df_title_selected['title'].values[0], df_title_selected['type'].values[0], df_title_selected['country'].values[0], df_title_selected['cast'].values[0], df_title_selected['director'].values[0], df_title_selected['duration'].values[0], df_title_selected['release_year'].values[0], df_title_selected['rating'].values[0], df_title_selected['description'].values[0]), unsafe_allow_html=True)
st.write("      ")
st.write("      ")


#-----wordcloud-----
st.write("## Wordcloud for movies' and tv shows' description")
st.write('''We note that the topics and the stories approached are <b>nearly the same</b> whether it is a movie or a tv-show.<br/>
We can conclude from this that tv-shows are not a new concept in term of content but in term of consumption.''', unsafe_allow_html=True)
col_wc_1, col_wc_2 = st.columns(2)
with col_wc_1:
    st.header("Wordcloud for movies' description")
    st.write('''Most common words in description of movies:<br/>
    <ul>
    <li>life</li>
    <li>find</li>
    <li>family</li>
    <li>take</li>
    <li>friend</li>
    </ul>''', unsafe_allow_html=True)
    st.image(movie_image)
with col_wc_2:
    st.header("Wordcloud for tv shows' description")
    st.write('''Most common words in description of movies:<br/>
        <ul>
        <li>life</li>
        <li>find</li>
        <li>family</li>
        <li>take</li>
        <li>new</li>
        </ul>''', unsafe_allow_html=True)
    st.image(tv_image)
st.write("      ")
st.write("      ")


#----Bar chart to show the Top 10 number of works for actors.----
st.write('## Bar chart to show the Top 10 number of works people who participated in.')
st.write('''<b>x-name(s), y-amount of works</b> <br/>
It shows that <b>David Attenborough</b> (a writer) contributed the most contents on Netflex (19 works), the 10th place is <b>Jim Gaffigan</b> who played in 5 works.''', unsafe_allow_html=True)
fig5
st.write("      ")
st.write("      ")

#-----Double Pie chart to show the ratio of ratings between Movies and TV Shows----
st.write('## Double Pie chart to show the ratio of ratings between Movies and TV Shows')
st.write('''I replaced the rating by different age group according to the following chart:<br/>
''', unsafe_allow_html=True)
st.markdown('''<table align="center">
<tr align="center">
    <td>TV-MA/UR/NC-17</td>
    <td>Adults</td>
</tr>
<tr align="center">
    <td>TV-Y7-FV/TV-Y7/PG/TV-PG</td>
    <td>Older Kids</td>
</tr>
<tr align="center">
    <td>TV-14</td>
    <td>Teens</td>
</tr>
<tr align="center">
    <td>TV-G/G</td>
    <td>Kids</td>''', unsafe_allow_html=True)
st.write("      ")
st.write("      ")
st.write('Ignoring the <b>missing data(unknowns)</b>, it shows that:<br/>', unsafe_allow_html=True)
st.write('''<ol>
<li>About a half of movies on Netflix are rated for <b>adults</b>, followed by <b>teens-31.3%</b>, the remainder is less than <b>25%</b>.</li>
<li>About <b>27.4%</b> of TV Shows are rated for <b>teens</b> and <b>19.4%</b> of contents are for <b>older kids</b>.</li>
We can deduct that TV-shows are more turned towards young audience and movies are reserved for an older audience.
''', unsafe_allow_html=True)
fig_rating
st.write("      ")
st.write("      ")

#-----The duration of tv shows and movies?----
st.write('## The duration of tv shows and movies?')
st.write('''<b>x-amount; y-duration</b> <br/>
We can see that a new trend has been created since covid.<br/>
The <b>“mini-series”</b> format which is a serie show with only one season.<br/>
This new concept was created to give the consumer the impression of being feeded with new content whereas the amount released decreased significantly since <b>2020</b>. <br/>
The ultimate goal of this new trend was to change consumer habits and to push the viewer to consume the content available more slowly.<br/>''', unsafe_allow_html=True)
fig6


