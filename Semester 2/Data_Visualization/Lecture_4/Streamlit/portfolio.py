import plotly.express as px
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

import yfinance as yf
import datetime as dt

st.write("# Fake crypto portfolio")
st.write("Computed from local *portfolio.xlsx* file")

df = pd.read_excel("portfolio.xlsx", None); # reads all sheets
xls = pd.ExcelFile('portfolio.xlsx')


maindf = pd.DataFrame(columns=['CoinName', 'count', 'totalInvest','currentValue'])
start = dt.datetime.now() #-(1000*60*60)

for k in df.keys():
    tdf = xls.parse(k,parse_cols = 3, skiprows = 0, nrows = 1, header = None)
    val = yf.download(k, start, start)
    # st.write(val['Open'].values)
    row = { 'CoinName': tdf.at[0,1],'count':tdf.at[0,3],'totalInvest':tdf.at[0,5], 'currentValue': str(1.0*tdf.at[0,3]*val['Open'].values) }
    maindf= maindf.append(row, ignore_index=True)

st.write( type(maindf) )
st.dataframe( maindf )

pieByCount = go.Figure(
    go.Pie(
        labels = maindf['CoinName'],
        values = maindf['count'],
        hoverinfo = "label+percent+value",
        textinfo = "label+value"
    ))
st.write("## Unit Count per coin")
pieByCount


pieByVolume = go.Figure(
    go.Pie(
        labels = maindf['CoinName'],
        values = maindf['totalInvest'],
        hoverinfo = "label+percent+value",
        textinfo = "label+value"
    ))

st.write("## Investment per coin")
pieByVolume

## Treemap
st.write("## Your treasure repartition")
treemap = px.treemap(maindf, path=[px.Constant("all"), 'CoinName'], values='totalInvest', labels='CoinName',hover_name="CoinName")
treemap.update_traces(root_color="lightgreen")
treemap.update_layout(margin = dict(t=50, l=25, r=25, b=25))
st.write("## Treemap ")
st.plotly_chart(treemap, use_container_width=True)

# show comparison of total investment and current value
## Sanky


# 1/ horizontal bar chart : total invest + current value
# 2/ double donut: inner=invest , outer = value
# 3/ vertical bar chart w/ 2 columns per coin

# component showing a balance