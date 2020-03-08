from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app

import pandas as pd
import pickle

from sklearn.neighbors import NearestNeighbors

dtm = pickle.load(open('model/dtm.pkl', 'rb'))
tf = pickle.load(open('model/tf.pkl', 'rb'))

cities = ['Belvedere',
          'Bolinas',
          'Corte Madera',
          'Dillon Beach',
          'Fairfax',
          'Greenbrae',
          'Inverness',
          'Kentfield',
          'Larkspur',
          'Marshall',
          'Mill Valley',
          'Muir Beach',
          'Nicasio',
          'Novato',
          'Point Reyes',
          'Ross',
          'San Anselmo',
          'San Geronimo Valley',
          'San Rafael',
          'Sausalito',
          'Stinson Beach',
          'Tiburon',
          'Tomales',
          'Other'
          ]

style = {'padding': '1.5em'}

layout = html.Div([
    dcc.Markdown("""
        ### Predict
        Use the controls below to update your predicted offer, based on city,
        beds, baths, number of offers, and list price.
    """),

    html.Div(id='prediction-content', style={'fontWeight': 'bold'}),

    html.Div([
        dcc.Markdown('###### Area'),
        dcc.Dropdown(
            id='area',
            options=[{'label': city, 'value': city} for city in cities],
            value=cities[10]
        ),
    ], style=style),
  
])
