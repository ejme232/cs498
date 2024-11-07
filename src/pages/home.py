from dash import html, register_page
from dash_mantine_components import Container, Text

#define the home page
register_page(__name__, path="/")
home_page_container = Container(
                id="home-page-container",
                children=[
                    Text("Home Page", id="home-page-title", style={"fontSize": "22px", "fontWeight": "bold", "marginBottom": "10px", "color": "#34495e"}),
                    Text("This is where our data visualizations will go.", id="home-page-description"),
                    #include various data visualizations
                ],
                style={"padding": "40px", "maxWidth": "800px", "margin": "auto"}
            )
layout = html.Div(
        id="home-page-content",
        children=[
            home_page_container
        ]
    )
