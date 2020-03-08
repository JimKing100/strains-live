from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app, server
from tabs import intro, recommend, about

style = {'maxWidth': '960px', 'margin': 'auto'}

app.layout = html.Div([
    dcc.Markdown('## Marijuana Recommendation System Using TF-IDF and k-NN'),
    dcc.Tabs(id='tabs', value='tab-intro', children=[
        dcc.Tab(label='Intro', value='tab-intro'),
        dcc.Tab(label='Recommend', value='tab-recommend'),
        dcc.Tab(label='About', value='tab-about'),
    ]),
    html.Div(id='tabs-content'),
], style=style)

@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'tab-intro': return intro.layout
    elif tab == 'tab-recommend': return recommend.layout
    elif tab == 'tab-about': return about.layout

if __name__ == '__main__':
    app.run_server(debug=True)
