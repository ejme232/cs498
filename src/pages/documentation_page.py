from dash import html
import dash_mantine_components as dmc
from pages.consistent_header import create_header  

def documentation_page():
    return html.Div(
        id="documentation-page-content",
        children=[
            # call in the header function from consistent_header.py
            create_header(),
            dmc.Container(
                id="documentation-page-container",
                children=[
                    dmc.Text(
                        "Documentation Page", 
                        id="documentation-page-title",
                        style={"fontSize": "22px", "fontWeight": "bold", "marginBottom": "10px", "color": "#34495e"}
                        # could use drop down sections that show header and then when clicked show the rest of the info
                        # or could utilize a list of links to separate pages
                    ),
                   
                ],
                style={"padding": "20px"}
            ),
        ]
    )
