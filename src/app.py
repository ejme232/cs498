import dash
import dash_mantine_components as dmc
import pandas as pd
from dash import Dash, dash_table, dcc, _dash_renderer, html, Input, Output, State
import plotly.express as px
from dash_iconify import DashIconify
_dash_renderer._set_react_version("18.2.0")

# Initialize the app
app = Dash(__name__, suppress_callback_exceptions=True)

## Stylizing the website 
# Define the reusable header with the hamburger menu
def create_header():
    return dmc.Group(
        # Align items across the header
        justify="space-between",
        # create the style for header
        style={"padding": "10px", "borderBottom": "1px solid #ccc", "backgroundColor": "#f8f9fa"},
        children=[
            # Left side of header
            dmc.Group(
                children=[
                    dmc.Menu(
                        children=[
                            # Hamburger menu for navigation
                            dmc.MenuTarget(
                                dmc.Button("☰", variant="light", size="sm")  # Hamburger icon as a button
                            ),
                            # set up the dropdown menu for when the hamburger button is clicked
                            dmc.MenuDropdown(
                                children=[
                                    dmc.NavLink(label="Home", href="/home"),
                                    dmc.NavLink(label="Data", href="/data"),
                                    dmc.NavLink(label="Documentation", href="/documentation"),
                                    dmc.NavLink(label="About", href="/about"),
                                ]
                            )
                        ],
                    ),
                ]
            ),

            # Middle of header with Title
            dmc.Group(
                children=[
                    # Title
                    dmc.Text("Website Name", style={"fontSize": "24px", "fontWeight": "bold", "color": '#2c3e50'}),  
                ],
            ),

            # Right side of header
            dmc.Group(
                children=[
                    # Settings dropdown menu
                    dmc.Menu(
                        children=[
                            dmc.MenuTarget(
                                dmc.ActionIcon(
                                   DashIconify(icon="ep:setting", width=24),
                                   variant="light",
                                   size="md"
                                )
                            ),
                            ## add some functionality to this
                        ],
                    ),
                ]
            )
        ]
    )

# Define the home page
def home_page():
    return html.Div([
        create_header(),
        dmc.Container(
            children=[
                dmc.Text("Home Page", style={"fontSize": "22px", "fontWeight": "bold", "marginBottom": "10px", "color": "#34495e"}),
                dmc.Text("This is where our data visualizations will go. Here is an example:"),
                
                # example bar chart from dash-mantine-components manual; our data/visualizations would take the place of this
                dmc.BarChart(
                    h=400,
                    dataKey="month",
                    data=data,
                    withLegend=True,
                    series=[
                        {"name": "Smartphones", "color": "violet.6"},
                        {"name": "Laptops", "color": "blue.6"},
                        {"name": "Tablets", "color": "teal.6"},
                    ],
                    tickLine="y",
                    gridAxis="y",
                    withXAxis=True,
                    withYAxis=True,
                    legendProps={"padding": "10px"},  # Add padding to the legend
                )
            ],
            style={"padding": "40px", "maxWidth": "800px", "margin":"auto"}
        ),
    ])

#define the data page
def data_page():
    return html.Div([
        create_header(),
        dmc.Container(
            children=[
                dmc.Text("Data Page", style={"fontSize": "22px", "fontWeight": "bold", "marginBottom": "10px", "color": "#34495e"}),
                # once data is imported in, utilize filters and stylize that
                # depending on amount of data can also use Pagination to allow for different pages of data, make it easier to navigate
            ],
            style={"padding": "20px"}
        ),
    ])

def documentation_page():
    return html.Div([
        create_header(),
        dmc.Container(
            children=[
                dmc.Text("Documentation Page", style={"fontSize": "22px", "fontWeight": "bold", "marginBottom": "10px", "color": "#34495e"}),
                # could use drop down sections that show header and then when clicked show the rest of the info
                # or could utilize a list of links to separate pages
            ],
            style={"padding": "20px"}
        ),
    ])

def about_page():
    return html.Div([
        create_header(),
        dmc.Container(
            children=[
                dmc.Text("About Page", style={"fontSize": "22px", "fontWeight": "bold", "marginBottom": "10px", "color": "#34495e"}),
                # create a brief overview of purpose of website
                # create a stylized "what's next section"
            ],
            style={"padding": "20px"}
        ),
    ])

# App layout with URL routing
app.layout = dmc.MantineProvider(
    children=[
        # URL component to track the current page
        dcc.Location(id="url"),  
        # Placeholder for page content
        html.Div(id="page-content"),  
    ],
    withCssVariables=True,
)

# Callback to render the correct page based on URL
@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname")
)
def display_page(pathname):
    if pathname == "/data":
        return data_page()
    elif pathname == "/documentation":
        return documentation_page()
    elif pathname == "/about":
        return about_page()
    else:
        return home_page()
## ---- end of stylizing related code

# data for example table
data = [
    {"month": "January", "Smartphones": 1200, "Laptops": 900, "Tablets": 200},
    {"month": "February", "Smartphones": 1900, "Laptops": 1200, "Tablets": 400},
    {"month": "March", "Smartphones": 400, "Laptops": 1000, "Tablets": 200},
    {"month": "April", "Smartphones": 1000, "Laptops": 200, "Tablets": 800},
    {"month": "May", "Smartphones": 800, "Laptops": 1400, "Tablets": 1200},
    {"month": "June", "Smartphones": 750, "Laptops": 600, "Tablets": 1000}
]


# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
