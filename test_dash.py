import dash
from dash import html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

app.layout = html.Div([
    html.H1("Test Dashboard")
])

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8051, debug=True)
