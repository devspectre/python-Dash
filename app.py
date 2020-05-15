import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('us.csv', header=0, escapechar='\\')


app.layout = html.Div(
  style={'height': '100%'},
  children=[
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure={
            'data': [
                dict(
                    x=df[df['date'] == i]['cases'] + df[df['date'] == i]['deaths'],
                    y=df[df['date'] == i]['date'],
                    text=f"Infection cases: {df[df['date'] == i]['cases']} Deaths: {df[df['date'] == i]['deaths']}",
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df.date.unique()
            ],
            'layout': dict(
                xaxis={'type': 'log', 'title': 'Dates'},
                yaxis={'title': 'Number of cases'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)