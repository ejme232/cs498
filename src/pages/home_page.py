from dash import html
import dash_mantine_components as dmc
from pages.consistent_header import create_header  # Import the reusable header

def home_page():
    return html.Div(
        id="home-page-content",
        children=[
            create_header(),  # Use the header here
            dmc.Container(
                id="home-page-container",
                children=[
                    dmc.Text("Home Page", id="home-page-title", style={"fontSize": "22px", "fontWeight": "bold", "marginBottom": "10px", "color": "#34495e"}),
                    dmc.Text("This is where our data visualizations will go. Here is an example:", id="home-page-description"),
                ],
                style={"padding": "40px", "maxWidth": "800px", "margin": "auto"}
            )
        ]
    )
