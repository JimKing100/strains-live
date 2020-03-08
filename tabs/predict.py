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

@app.callback(
    Output('prediction-content', 'children'),
    [Input('effects1', 'value')
#     Input('effects2', 'value'),
#     Input('effects3', 'value'),
#     Input('effects4', 'value'),
#     Input('effects5', 'value'),
#     Input('flavor1', 'value'),
#     Input('flavor2', 'value'),
#     Input('flavor3', 'value')
    ])
def predict(effects1):#,effects2, effects3, effects4, effects5
            #flavor1, flavor2, flavor3):
           
    nn = NearestNeighbors(n_neighbors=5, algorithm='ball_tree')
    nn.fit(dtm)
    ideal_strain = ['Creative,Energetic,Tingly,Euphoric,Relaxed,Earthy,Sweet,Citrus']
    new = tf.transform(ideal_strain)
    results = nn.kneighbors(new.todense())

    results = [strains['Strain'][results[1][0][i]] for i in range(5)]

    return results
