import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/r')

def generate_table(dataframe, max_rows=10):
  return html.Table([
    html.Thead(
      html.Tr([html.Th(col) for col in dataframe.columns])
    ),
    html.Tbody([
      html.Tr([html.Td(dataframe.iloc[i][col]) for col in dataframe.columns]) for i in range(min(len(dataframe), max_rows))
    ])
  ])

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
  'background': '#111111',
  'text': '#7FDBFF'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
  html.H4(children='US Agriculture Exports (2011)'),
  generate_table(df),
  html.H1(
    children='Hello Dash! I wanna a bite!',
    style={
      'textAlign': 'center',
      'color': colors['text']
    }
  ),

  html.Div(
    children='Dash: A web application framework for Python.', 
    style={
      'textAlign': 'center',
      'color': colors['text']
    }
  ),

  dcc.Graph(
    id='example-graph',
    figure={
      'data': [
        {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
        {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
      ],
      'layout': {
        'title': 'Dash Data Visualization',
        'plot_bgcolor': colors['background'],
        'paper_bgcolor': colors['background'],
        'font': {
          'color': colors['text']
        }
      }
    }
  )
])

if __name__ == '__main__':
  app.run_server(debug=True)