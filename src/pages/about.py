from dash import html, register_page
from dash_mantine_components import Container, Text

register_page(__name__)
about_page_container = Container(
                id="about-page-container",
                children=[
                    Text("About Page", id="about-page-title", style={"fontSize": "22px", "fontWeight": "bold", "marginBottom": "10px", "color": "#34495e"}),
                    # create a brief overview of purpose of website
                    # create a stylized "what's next section"
                    Text("The goal of this project is to bring together data on mental health and substance abuse in order to bring awareness and information to the public.", style={"fontSize": "16px", "marginBottom": "15px"}),  
                    Text("Future goals section coming soon", style={"fontSize": "12px", "fontStyle": "italic"}),  
                ],
                style={"padding": "20px"}
            )
layout = html.Div(
        id="about-page-content",  
        children=[
            about_page_container
        ]
    )
