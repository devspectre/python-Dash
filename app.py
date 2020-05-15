# import dash
# import dash_core_components as dcc
# import dash_html_components as html
# import pandas as pd

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')

# def generate_table(dataframe, max_rows=10):
#   return html.Table([
#     html.Thead(
#       html.Tr([html.Th(col) for col in dataframe.columns])
#     ),
#     html.Tbody([
#       html.Tr([html.Td(dataframe.iloc[i][col]) for col in dataframe.columns]) for i in range(min(len(dataframe), max_rows))
#     ])
#   ])

# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# colors = {
#   'background': '#111111',
#   'text': '#7FDBFF'
# }

# app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
#   html.H4(children='US Agriculture Exports (2011)'),
#   generate_table(df),
#   html.H1(
#     children='Hello Dash! I wanna a bite!',
#     style={
#       'textAlign': 'center',
#       'color': colors['text']
#     }
#   ),

#   html.Div(
#     children='Dash: A web application framework for Python.', 
#     style={
#       'textAlign': 'center',
#       'color': colors['text']
#     }
#   ),

#   dcc.Graph(
#     id='example-graph',
#     figure={
#       'data': [
#         {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
#         {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
#       ],
#       'layout': {
#         'title': 'Dash Data Visualization',
#         'plot_bgcolor': colors['background'],
#         'paper_bgcolor': colors['background'],
#         'font': {
#           'color': colors['text']
#         }
#       }
#     }
#   )
# ])

# if __name__ == '__main__':
#   app.run_server(debug=True)

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')


app.layout = html.Div([
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure={
            'data': [
                dict(
                    x=df[df['continent'] == i]['gdp per capita'],
                    y=df[df['continent'] == i]['life expectancy'],
                    text=df[df['continent'] == i]['country'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df.continent.unique()
            ],
            'layout': dict(
                xaxis={'type': 'log', 'title': 'GDP Per Capita'},
                yaxis={'title': 'Life Expectancy'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)