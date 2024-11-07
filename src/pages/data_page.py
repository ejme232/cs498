from dash import html, register_page
from dash_mantine_components import Container, Text

register_page(__name__)
data_page_container =  Container(
                id="data-page-container",
                children=[
                    Text("Data Page", id="data-page-title", style={"fontSize": "22px", "fontWeight": "bold", "marginBottom": "10px", "color": "#34495e"}),
                    # once data is imported in, utilize filters and stylize that
                    # depending on amount of data can also use Pagination to allow for different pages of data, make it easier to navigate
                ],
                style={"padding": "20px"}
            )
layout = html.Div(
        id="data-page-content",
        children=[
           data_page_container
        ]
    )
