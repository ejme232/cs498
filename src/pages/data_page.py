from dash import html
import dash_mantine_components as dmc
from pages.consistent_header import create_header  # Import the reusable header

def data_page():
    return html.Div(
        id="data-page-content",
        children=[
            create_header(),  # Use the header here
            dmc.Container(
                id="data-page-container",
                children=[
                    dmc.Text("Data Page", id="data-page-title", style={"fontSize": "22px", "fontWeight": "bold", "marginBottom": "10px", "color": "#34495e"}),
                    # Add other data-specific components here
                ],
                style={"padding": "20px"}
            )
        ]
    )
