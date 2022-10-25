#！/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time  : 30/06/2022  12:44
@Author: Skye
@File  : Pokemon_pour_lecture2.py
"""
import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# leave this live
app = Dash(__name__)

# load the data
df = pd.read_csv('Pokemon.csv')
#Graph1:
count_type = df['Type 1'].value_counts()
type_pokemon = ['Water', 'Normal', 'Grass', 'Bug', 'Psychic', 'Fire', 'Electric', 'Rock', 'Dragon', 'Ground', 'Ghost', 'Dark', 'Poison', 'Steel', 'Fighting', 'Ice', 'Fairy', 'Flying']
df1 = pd.DataFrame({
    'Count': count_type[:],
    'Type of pokemon': type_pokemon
})

#Graph2:
count_legendary = df['Legendary'].value_counts()
count_legendary = count_legendary.sort_values()
# print(count_legendary)
df2 = pd.DataFrame({
    'Legendary or not': ['Yes', 'No'],
    'Count': count_legendary[:]
})

#Graph3:
df3 = pd.DataFrame({
    "Name": df['Name'],
    "Total index": df["Total"],
    "HP": df['HP'],
    "Type": df["Type 1"]
})

#Graph4:


#Callback1
df4 = pd.DataFrame(columns=['Type', 'HP', 'Attack', 'Defense', 'Sp_Atk', 'Sp_Def', 'Speed', 'Generation'])
for i in range(len(df)):
    row = {
           'Type': df['Type 1'][i],
           'HP': df['HP'][i],
           'Attack': df['Attack'][i],
           'Defense': df['Defense'][i],
           'Sp_Atk': df['Sp. Atk'][i],
           'Sp_Def': df['Sp. Def'][i],
           'Speed': df['Speed'][i],
           'Generation': df['Generation'][i]
    }
    df4 = df4.append(row, ignore_index=True)

#Callback

# print(df4)
type_pokemon = ['Water', 'Normal', 'Grass', 'Bug', 'Psychic', 'Fire', 'Electric', 'Rock', 'Dragon', 'Ground', 'Ghost', 'Dark', 'Poison', 'Steel', 'Fighting', 'Ice', 'Fairy', 'Flying']

# create charts
fig1 = px.bar(df1, x='Type of pokemon', y='Count', color="Type of pokemon") #Bar chart for display the amount of each type of Pokémon.
fig2 = px.pie(df2, labels='Legendary or not', values='Count', color='Legendary or not') #Bar chart for display the amount of whether Pokémons are legendary or not.
fig3 = px.scatter(df3, x="Name", y="Total index", size="HP", color="Type") #Classify Pokémons by its type and shows the total index and the initial HP of them.
fig4 = px.pie(df1, labels="Type of pokemon", values="Count", color="Type of pokemon")
fig5 = px.treemap(df1, path=[px.Constant('All'), 'Type of pokemon'], values="Count", color='Type of pokemon')

#Separate layout:
####### Callback Part1
dropdown = html.Div([
    html.H3(children='Basic information of Pokémon', style={
        'textAlign': "center"
    }),
    dcc.Dropdown(df["Name"], df["Name"][0], id="Name"),
    html.Br(),
    # html.Div(children=[
    #     "It's HP:", html.Div(id='HP'),
    #     "It's Attack::", html.Div(id='Attack'),
    #     "It's Defense:", html.Div(id='Defense'),
    #     "It's Super Attack:", html.Div(id='Sp_Atk'),
    #     "It's Super Attack:", html.Div(id='Sp_Def'),
    #     "It's Speed:", html.Div(id='Speed'),
    #     "It's in Generation:", html.Div(id='Generation'),
    # ]),

    # Information table
    html.Table([
        html.Tr([html.Td(["Name:"]), html.Td(id='Name_print')], style={'textAlign': 'center'}),
        html.Tr([html.Td(["Type:"]), html.Td(id='Type')], style={'textAlign': 'center'}),
        html.Tr([html.Td(["Initial HP:"]), html.Td(id='HP')], style={'textAlign': 'center'}),
        html.Tr([html.Td(["Attack:"]), html.Td(id='Attack')], style={'textAlign': 'center'}),
        html.Tr([html.Td(["Defense:"]), html.Td(id='Defense')], style={'textAlign': 'center'}),
        html.Tr([html.Td(["Super Attack:"]), html.Td(id='Sp_Atk')], style={'textAlign': 'center'}),
        html.Tr([html.Td(["Super Defense:"]), html.Td(id='Sp_Def')], style={'textAlign': 'center'}),
        html.Tr([html.Td(["Speed:"]), html.Td(id='Speed')], style={'textAlign': 'center'}),
        html.Tr([html.Td(["In Generation:"]), html.Td(id='Generation')], style={'textAlign': 'center'}),
    ]),
])

    # Callback 2
    # Information graph (using "slider" callback)
# slider = html.Div([
#     dcc.Graph(id='callback_with_slider'),
#     dcc.Slider(
#         0,
#         17,
#         step=None,
#         value=df['Type 1'].unique()[0],
#         marks={str(i): str(i) for i in df["Type 1"].unique()},
#         id='type_slider'
#     ),
# ])

#######Chart 1
chart1 = html.Div([
    html.H3(children='The amonut of each type of Pokémon(Bar chart)', style={
            'textAlign': "center"
        }),
    dcc.Graph(
        id='Type of Pokémon(Bar)',
        figure=fig1
    ),
])

chart2_and_chart3 = html.Div([
    #######Chart 2
    html.Div([
        html.H3(children='The ratio of each type of Pokémon(Pie chart)', style={
            'textAlign': "center"
        }),
    dcc.Graph(
        figure=fig4
        )
    ]),

#######Chart 3
    html.Div([
    html.H3(children='The amonut of whether Pokémons are legendary or not', style={
            'textAlign': "center"
        }),
    dcc.Graph(
        id='Whether Pokémons are legendary or not',
        figure=fig2
    )
    ])
])

#chart 4
chart4 = html.Div([
    html.H3(children='Total index and initial HP of Pokémons clasified by their type', style={
            'textAlign': "center"
        }),
    dcc.Graph(
        id='Total index and initial HP of Pokémons',
        figure=fig3
    )
])
#Chart 5
chart5 = html.Div([
    html.H3(children='The amont and ratio of each type of Pokémon(Treemap)', style={
            'textAlign': "center"
        }),
    dcc.Graph(
        id='treemap',
        figure=fig5
    )
])

# create layout:
app.layout = html.Div([
    html.H1(children="Welcome to the world of Pokémon"),
    html.Div([
    dropdown,
    # slider,
    chart5,
    chart1,
    chart2_and_chart3,
    chart4
    ]),
])

@app.callback(
    Output('Name_print', 'children'),
    Output('Type', 'children'),
    Output('HP', 'children'),
    Output('Attack', 'children'),
    Output('Defense', 'children'),
    Output('Sp_Atk', 'children'),
    Output('Sp_Def', 'children'),
    Output('Speed', 'children'),
    Output('Generation', 'children'),
    Input('Name', 'value')
)

# @app.callback(
#     Output('callback_with_slider', 'figure'),
#     Input('type_slider', 'value')
# )

#Func for callback 1
def update_output(value):
    Name = value
    Type = df4[df['Name'] == value].Type
    HP = df4[df['Name'] == value].HP
    Attack = df4[df['Name'] == value].Attack
    Defense = df4[df['Name'] == value].Generation
    Sp_Atk = df4[df['Name'] == value].Sp_Atk
    Sp_Def = df4[df['Name'] == value].Sp_Def
    Speed = df4[df['Name'] == value].Speed
    Generation = df4[df['Name'] == value].Generation
    return Name, Type, HP, Attack, Defense, Sp_Atk, Sp_Def, Speed, Generation
    # return Attack, Generation

#Func for callback 2
# def update_figure(select_type):
#     filtered_df = df[df['Type 1'] == select_type]
#     fig5 = px.scatter(filtered_df, x="Name", y="Total", size='HP')
#     fig5.update_layout(transition_duration=500)
#     return fig5

# leave this part
if __name__ == '__main__':
    app.run_server(debug=True, port=8090)