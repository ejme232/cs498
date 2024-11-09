from dash import html, register_page
from dash_mantine_components import Container, Text
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
            radius="sm",
            children=[
                dmc.AccordionItem(
                [
                    dmc.AccordionControl(
                        dmc.Group(
                            [
                                dmc.Text("Data Gathering"),
                            ]
                        )
                    ),
                    dmc.AccordionPanel(
                        dmc.Text("Here is where we will detail how and where the data was gathered from.", size="sm"),
                    ),
                ],
                value="dataGathering",
                ),

                dmc.AccordionItem(
                [
                    dmc.AccordionControl(
                        dmc.Group(
                            [
                                dmc.Text("Data Processing"),
                            ]
                        )
                    ),
                    dmc.AccordionPanel(
                        dmc.Text("Here is where we will detail how the data was processed.", size="sm")
                    ),
                ],
                value="dataProcessing",
                ),

                dmc.AccordionItem(
                [
                    dmc.AccordionControl(
                        dmc.Group(
                            [
                                dmc.Text("Understanding the Data/How to use this website"),
                            ]
                        )
                    ),
                    dmc.AccordionPanel(
                        dmc.Text("Here is where we will detail important things to understand the data/how to use this website. This will help those who maybe aren't directly in the mental health field. ", size="sm")
                    ),
                ],
                value="usingWebsite",
                ),

                dmc.AccordionItem(
                [
                    dmc.AccordionControl(
                        dmc.Group(
                            [
                                dmc.Text("Mental Health Resources"),
                            ]
                        )
                    ),
                    dmc.AccordionPanel(
                        dmc.Text("Here is where we will include some important mental health resources", size="sm")
                    ),
                ],
                value="mentalHealth",
                )
            ],
          
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
