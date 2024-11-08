from dash import html, register_page
from dash_mantine_components import Container, AccordionControl, AccordionPanel, Group, Avatar, Text
import dash_mantine_components as dmc



register_page(__name__)

documentation_page_container = Container(
                id="documentation-page-container",
                children=[
                    Text(
                        "Documentation Page", 
                        id="documentation-page-title",
                        style={"fontSize": "22px", "fontWeight": "bold", "marginBottom": "10px", "color": "#34495e"}
                    ),
                   dmc.Accordion(
                        chevronPosition="left",
                        variant="contained",
                        children=[
                            dmc.AccordionItem(
                                [
                                    dmc.AccordionControl(
                                        dmc.Group(
                                        [
                                            dmc.Text("Header Title"),
                                        ]
                                        )
                                    ),
                                    dmc.AccordionPanel(
                                        dmc.Text("This is the body content of the dropdown.", size="sm")
                                    ),
                                ],
                                value="header",
                            )
                        ],
                        multiple=True
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
