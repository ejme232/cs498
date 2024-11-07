from dash import html
import dash_mantine_components as dmc
from pages.consistent_header import create_header  # Import the reusable header

def data_page():
    return html.Div(
        id="data-page-content",
        children=[
            # call in the header function from consistent_header.py
            create_header(),
            dmc.Container(
                id="data-page-container",
                children=[
                    dmc.Text("Data Page", id="data-page-title", style={"fontSize": "22px", "fontWeight": "bold", "marginBottom": "10px", "color": "#34495e"}),
                    # once data is imported in, utilize filters and stylize that
                    # depending on amount of data can also use Pagination to allow for different pages of data, make it easier to navigate
                ],
                style={"padding": "20px"}
            )
        ]
    )
