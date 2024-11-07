from dash import html, register_page
from dash_mantine_components import Container, Text

register_page(__name__)
documentation_page_container = Container(
                id="documentation-page-container",
                children=[
                    Text(
                        "Documentation Page", 
                        id="documentation-page-title",
                        style={"fontSize": "22px", "fontWeight": "bold", "marginBottom": "10px", "color": "#34495e"}
                        # could use drop down sections that show header and then when clicked show the rest of the info
                        # or could utilize a list of links to separate pages
                    ),
                   
                ],
                style={"padding": "20px"}
            )
layout = html.Div(
        id="documentation-page-content",
        children=[
            documentation_page_container
        ]
    )
