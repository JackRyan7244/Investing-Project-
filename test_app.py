import dash
from dash import html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

app.layout = html.Div([
    html.H1('Test Dashboard', style={'textAlign': 'center'}),
    html.P('If you can see this, Dash is working correctly!', style={'textAlign': 'center'})
])

if __name__ == '__main__':
    print("Starting test server...")
    app.run_server(debug=True, port=8050)
