from dash import html, register_page
from dash_mantine_components import Container, Text
import dash_mantine_components as dmc

register_page(__name__)

data_gathering_string="Our data was gathered by the Substance Abuse and Mental Health Services Administration (SAMHSA) for the 2022 National Survey on Drug Use and Health (NSDUH).\nAdditional information about this database can be found at https://www.samhsa.gov/data/data-we-collect/nsduh/datafiles?data_collection=1124&year=2015, and information about how this data was collected can be viewed at https://www.samhsa.gov/data/sites/default/files/reports/rpt44477/2022-nsduh-mrb-dcfr.pdf."

documentation_page_container = Container(
    id="documentation-page-container",
    children=[
        Text(
            "Documentation Page", 
            id="documentation-page-title",
            style={"fontSize": "22px", "fontWeight": "bold", "marginBottom": "10px", "color": "#34495e"}
        ),
        Text(
            "Author: Substance Abuse and Mental Health Services Administration (SAMHSA) Center for Behavioral Health Statistics and Quality", 
            id="documentation-citation",
            style={"fontSize": "18px", "marginBottom": "10px"}
        ),
        Text(
            "Date of publication: October 25, 2023", 
            id="documentation-citation",
            style={"fontSize": "18px", "marginBottom": "10px"}
        ),
        Text(
            "Title: 2022 National Survey on Drug Use and Health (NSDUH)", 
            id="documentation-citation",
            style={"fontSize": "18px", "marginBottom": "10px"}
        ),
        Text(
            "Publisher: SAMHSA", 
            id="documentation-citation",
            style={"fontSize": "18px", "marginBottom": "10px"}
        ),
        dmc.Anchor(
            "URL: https://www.samhsa.gov/data/data-we-collect/nsduh/datafiles?year=2022&data_collection=1186", 
            href="https://www.samhsa.gov/data/data-we-collect/nsduh/datafiles?year=2022&data_collection=1186",
            style={"fontSize": "18px", "marginBottom": "10px"}
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
                        dmc.Text(data_gathering_string, size="sm"),
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
