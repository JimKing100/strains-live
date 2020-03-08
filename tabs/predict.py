from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app

import pandas as pd
import pickle

from sklearn.neighbors import NearestNeighbors

dtm = pickle.load(open('model/dtm.pkl', 'rb'))
tf = pickle.load(open('model/tf.pkl', 'rb'))

URL = "https://raw.githubusercontent.com/JimKing100/strains-live/master/data/cannabis.csv"
strains = pd.read_csv(URL)
strains = strains.dropna()
strains = strains.reset_index(drop=True)

strains['Criteria'] = strains['Effects'] + ',' + strains['Flavor']

effects = ['Creative', 'Energetic', 'Tingly', 'Euphoric', 'Relaxed',
           'Aroused', 'Happy', 'Uplifted', 'Hungry', 'Talkative',
           'Giggly', 'Focused', 'Sleepy', 'Dry'
          ]

flavors = ['Earthy', 'Sweet', 'Citrus', 'Flowery', 'Violet', 'Diesel',
           'Spicy/Herbal', 'Sage', 'Woody', 'Apricot', 'Grapefruit', 'Orange',
           'Pungent', 'Grape', 'Pine', 'Skunk', 'Berry', 'Pepper',
           'Menthol', 'Blue', 'Cheese', 'Chemical', 'Mango', 'Lemon', 'Peach',
           'Vanilla', 'Nutty', 'Chestnut', 'Tea', 'Tobacco', 'Tropical',
           'Strawberry', 'Blueberry', 'Mint', 'Apple', 'Honey', 'Lavender',
           'Lime', 'Coffee', 'Ammonia', 'Minty', 'Tree', 'Fruit', 'Butter',
           'Pineapple', 'Tar', 'Rose', 'Plum', 'Pear'
          ]

style = {'padding': '1.5em'}

layout = html.Div([
    dcc.Markdown("""
        ### Predict
        Use the controls below to select your effects and flavors.
    """),

    html.Div(id='effects-content', style={'fontWeight': 'bold'}),
    html.Div(id='flavors-content', style={'fontWeight': 'bold'}),
    html.Div(id='prediction-content', style={'fontWeight': 'bold'}),

    html.Div([
        dcc.Markdown('###### Effects - Select 5'),
        dcc.Dropdown(
            id='effects',
            options=[{'label': effect, 'value': effect} for effect in effects],
            value=[],
            multi=True
        ),
    ], style=style),
           
    html.Div([
        dcc.Markdown('###### Flavors - Select 3'),
        dcc.Dropdown(
            id='flavors',
            options=[{'label': flavor, 'value': flavor} for flavor in flavors],
            value=[],
            multi=True
        ),
    ], style=style),
  
])

@app.callback(
    [Output('effects-content', 'children'),
     Output('flavors-content', 'children'),
     Output('prediction-content', 'children')],
    [Input('effects', 'value'),
     Input('flavors', 'value')
#     Input('effects3', 'value'),
#     Input('effects4', 'value'),
#     Input('effects5', 'value'),
#     Input('flavor1', 'value'),
#     Input('flavor2', 'value'),
#     Input('flavor3', 'value')
    ])
def predict(effects, flavors):
           
    nn = NearestNeighbors(n_neighbors=5, algorithm='ball_tree')
    nn.fit(dtm)
    ideal_strain = ['Creative,Energetic,Tingly,Euphoric,Relaxed,Earthy,Sweet,Citrus']
    new = tf.transform(ideal_strain)
    results = nn.kneighbors(new.todense())

    results = [strains['Strain'][results[1][0][i]] for i in range(5)]

    return effects[0], flavors[0], results
