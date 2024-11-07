from dash import html
import dash_mantine_components as dmc
from pages.consistent_header import create_header  # Import the reusable header

def about_page():
    return html.Div(
        id="about-page-content",  
        children=[
            # call in the header function from consistent_header.py
            create_header(),
            dmc.Container(
                id="about-page-container",
                children=[
                    dmc.Text("About Page", id="about-page-title", style={"fontSize": "22px", "fontWeight": "bold", "marginBottom": "10px", "color": "#34495e"}),
                    # create a brief overview of purpose of website
                    # create a stylized "what's next section"
                ],
                style={"padding": "20px"}
            ),
        ]
    )
