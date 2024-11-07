from dash import html
import dash_mantine_components as dmc
from pages.consistent_header import create_header  # Import the reusable header

#define the home page
def home_page():
    return html.Div(
        id="home-page-content",
        children=[
            # call in the header function from consistent_header.py
            create_header(),  
            dmc.Container(
                id="home-page-container",
                children=[
                    dmc.Text("Home Page", id="home-page-title", style={"fontSize": "22px", "fontWeight": "bold", "marginBottom": "10px", "color": "#34495e"}),
                    dmc.Text("This is where our data visualizations will go.", id="home-page-description"),
                    #include various data visualizations
                ],
                style={"padding": "40px", "maxWidth": "800px", "margin": "auto"}
            )
        ]
    )
