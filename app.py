import dash
from dash import html
import dash_bootstrap_components as dbc

app = dash.Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[
        dbc.themes.DARKLY,
        'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css'
    ],
    suppress_callback_exceptions=True
)

app.layout = html.Div([
    dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink(page["name"], href=page["path"]))
            for page in dash.page_registry.values()
        ],
        brand="Financial Dashboard",
        brand_href="/",
        color="primary",
        dark=True,
        className="mb-4",
    ),
    dash.page_container
])

if __name__ == '__main__':
    app.run_server(debug=True, port=8051)
