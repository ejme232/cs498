from dash_mantine_components import MantineProvider
from dash import Dash, dcc, _dash_renderer, html, page_registry
import dash
from components.header import create_header

# Set React Version
_dash_renderer._set_react_version("18.2.0")

# Initialize the app
app = Dash(__name__, suppress_callback_exceptions=True, use_pages=True)

# App layout with URL routing
app.layout = MantineProvider(
    children=[
        create_header(page_registry),
        dcc.Location(id="url"),
        html.Div(id="page-content"),
        dash.page_container
    ],
    
    withCssVariables=True,
)
    
# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)