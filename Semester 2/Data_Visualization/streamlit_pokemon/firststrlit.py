import plotly.express as px
import streamlit as st
import pandas as pd
from dash import Dash, dcc, html, Input, Output


app = Dash(__name__)

df = pd.read_csv("Pokemon.csv")
st.write("# Welcome to the world of Pokémon")   # this is markdown

# df2 = pd.DataFrame({
#     "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
#     "Amount": [4, 1, 2, 2, 4, 5],
#     "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
# })

#Graph1
count_type = df['Type 1'].value_counts()
type_pokemon = ['Water', 'Normal', 'Grass', 'Bug', 'Psychic', 'Fire', 'Electric', 'Rock', 'Dragon', 'Ground', 'Ghost', 'Dark', 'Poison', 'Steel', 'Fighting', 'Ice', 'Fairy', 'Flying']
df1 = pd.DataFrame({
    'Count': count_type[:],
    'Type of pokemon': type_pokemon
})

#Graph2
count_legendary = df['Legendary'].value_counts()
count_legendary = count_legendary.sort_values()
# print(count_legendary)
df2 = pd.DataFrame({
    'Legendary or not': ['Yes', 'No'],
    'Count': count_legendary[:]
})

#Graph3
df3 = pd.DataFrame({
    "Name": df['Name'],
    "Total index": df["Total"],
    "HP": df['HP'],
    "Type": df["Type 1"]
})

#Callback
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

# fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
fig1 = px.bar(df1, x='Type of pokemon', y='Count', color="Type of pokemon") #Bar chart for display the amount of each type of Pokémon.
fig2 = px.pie(df2, labels='Legendary or not', values='Count', color='Legendary or not') #Bar chart for display the amount of whether Pokémons are legendary or not.
fig3 = px.scatter(df3, x="Name", y="Total index", size="HP", color="Type") #Classify Pokémons by its type and shows the total index and the initial HP of them.
fig4 = px.pie(df1, labels="Type of pokemon", values="Count", color="Type of pokemon")
fig5 = px.treemap(df1, path=[px.Constant('All'), 'Type of pokemon'], values="Count", color='Type of pokemon')

st.write("## Here's our first attempt at using data to create a table:")
df

dropdown

st.write("## tests")
fig1
st.write("## tests")
fig2
st.write("## tests")
fig3
st.write("## tests")
fig4
st.write("## tests")
fig5



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
