import dash
import dash_mantine_components as dmc
from dash import Dash, dash_table, dcc, _dash_renderer, html, Input, Output, State
from dash_iconify import DashIconify

# import in each website page
from pages.home_page import home_page
from pages.data_page import data_page
from pages.documentation_page import documentation_page
from pages.about_page import about_page

# Set React Version
_dash_renderer._set_react_version("18.2.0")

# Initialize the app
app = Dash(__name__, suppress_callback_exceptions=True)

# App layout with URL routing
app.layout = dmc.MantineProvider(
    children=[
        dcc.location(id="url"),
        html.Div(id="page-content"),
    ],
    withCssVariables=True,
)

#Callback to render the correct page based on URL
@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname")
)

#create a series of if/else statements to navigate through the website based on the path name
def display_page(pathname):
    if pathname == "/data":
        return data_page()
    elif pathname == "/documentation":
        return documentation_page()
    elif pathname == "/about":
        return about_page()
    elif pathname == "/home":
        return home_page()
    else:
        return '404'
    
# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)