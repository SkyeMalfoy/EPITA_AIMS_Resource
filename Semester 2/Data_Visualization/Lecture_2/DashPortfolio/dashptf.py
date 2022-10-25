from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

# This is not financial advice
# DYOR : do your own research


app = Dash(__name__)


df = pd.read_excel("portfolio.xls", None)# reads all sheets
xls = pd.ExcelFile('portfolio.xls')

##### 1  -   Load and prepare data
maindf = pd.DataFrame(columns=['CoinName', 'count', 'totalInvest','currentValue'])

for k in df.keys():
    tdf = xls.parse(k, skiprows = 0, nrows = 1, header = None)
    row = { 'CoinName': tdf.at[0,1],
            'count':tdf.at[0,3],
            'totalInvest':tdf.at[0,5],
            'currentValue': 0 }
    maindf= maindf.append(row, ignore_index=True)

##### 2 - calculate charts

##### 3 -  define layout

app.layout = html.Div([
    html.H1('Gambled Values'),
    dcc.Dropdown( maindf["CoinName"] ,"BTC", id="coin"),
    html.Br()   ,
    html.Div(children=[
        "You have invested ",
        html.Div(id='coinvalue'),
        " Euros"])
])

@app.callback(
    Output('coinvalue', 'children'),
    Input('coin', 'value')
)
def update_output(value):
    return maindf[maindf["CoinName"]==value].totalInvest


if __name__ == '__main__':
    app.run_server(debug=True, port=8081)