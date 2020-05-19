import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('us.csv', header=0, escapechar='\\')

app.layout = html.Div(
  style={'height': '100vh'},
  children=[
    dcc.Graph(
        id='us-coronavirus-cases',
        figure={
            'data': [
                dict(
                    type='bar',
                    x=df.index.values.tolist(),
                    y=df['cases'],
                    name="Infection cases",
                )
            ],
            'layout': dict(
                # xaxis={'type': 'log', 'title': 'Date'},
                # yaxis={'title': 'Cases'},
                # margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                # legend={'x': 1, 'y': 0},
                # hovermode='closest'
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)