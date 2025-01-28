"""
Main application file for the Financial Dashboard
"""

import os
import sys
import dash
from dash import html
import dash_bootstrap_components as dbc

print("Starting Financial Dashboard...", file=sys.stderr)

# Initialize the app with a dark theme
app = dash.Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[
        dbc.themes.DARKLY,
        'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css'
    ],
    suppress_callback_exceptions=True,
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ]
)

# Create cache directory if it doesn't exist
os.makedirs('cache', exist_ok=True)

# Set up the app layout
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

# Import all pages
from pages import (
    home,
    market_movers,
    company_comparison,
    financial_analysis,
    cash_flow,
    market_overview,
    company_comparison,
    market_movers,
)

if __name__ == '__main__':
    print("Running server on http://127.0.0.1:8050", file=sys.stderr)
    app.run_server(debug=True, port=8050)
