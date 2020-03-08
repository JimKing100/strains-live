from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app

import pandas as pd
import pickle

from sklearn.neighbors import NearestNeighbors

dtm = pickle.load(open('model/dtm.pkl', 'rb'))
tf = pickle.load(open('model/tf.pkl', 'rb'))

effects = ['Creative',
           'Energetic',
           'Tingly',
           'Euphoric',
           'Relaxed',
           'Aroused',
           'Happy',
           'Uplifted',
           'Hungry',
           'Talkative',
           'Giggly',
           'Focused',
           'Sleepy',
           'Dry'
          ]

style = {'padding': '1.5em'}

layout = html.Div([
    dcc.Markdown("""
        ### Predict
        Use the controls below to select your effects and flavors.
    """),

    html.Div(id='prediction-content', style={'fontWeight': 'bold'}),

    html.Div([
        dcc.Markdown('###### Effects 1'),
        dcc.Dropdown(
            id='effects1',
            options=[{'label': effect, 'value': effect} for effect in effects],
            value=effects[0]
        ),
    ], style=style),
  
])
