from dash import html, register_page
import dash_mantine_components as dmc

register_page(__name__)

data_gathering_string="Our data was gathered by the Substance Abuse and Mental Health Services Administration (SAMHSA) for the 2022 National Survey on Drug Use and Health (NSDUH). Additional information about this database can be found in the codebook at https://www.samhsa.gov/data/data-we-collect/nsduh/datafiles?year=2022&data_collection=1186, and information about how this data was collected can be viewed at https://www.samhsa.gov/data/sites/default/files/reports/rpt44477/2022-nsduh-mrb-dcfr.pdf."
data_processing_string="The dataset itself isn’t touched, and it is assumed that the user has access to the codebook to better understand the data. Due to the immense amount of data present in this dataset, we opted to use a smaller subset of it due to memory limitations, but our website should work with larger datasets, too."
using_website_string="The goal of this website is to easily manipulate and extract mental health data. To do this, click on the dropdown box in the top-left corner and click on the “Data” page. This will take you to a table where you can add filters on each column. To find details on the locations and contents of each column, please refer to the codebook linked in the above box."

documentation_page_container = dmc.Container(
    id="documentation-page-container",
    children=[
        dmc.Text("Documentation", style={"fontSize": "32px", "fontWeight": "bold", "marginBottom": "10px", "color": "#2c3e50", "textAlign": "left"}),
        dmc.Divider(style={"marginBottom": "20px"}),

        dmc.Accordion(
            chevronPosition="left",
            variant="contained",
            radius="sm",
            multiple=True,
            children=[
                dmc.AccordionItem(
                [
                    dmc.AccordionControl(
                        dmc.Group(
                            [
                                dmc.Text("Data Gathering", size="lg", fw=700),
                            ]
                        )
                    ),
                    dmc.AccordionPanel(
                        dmc.Text(data_gathering_string, size="md"),
                    ),
                ],
                value="dataGathering",
                ),

                dmc.AccordionItem(
                [
                    dmc.AccordionControl(
                        dmc.Group(
                            [
                                dmc.Text("Understanding the Data", size="lg", fw=700),
                            ]
                        )
                    ),
                    dmc.AccordionPanel(
                        dmc.Text(data_processing_string, size="md")
                    ),
                ],
                value="understandingData",
                ),

                dmc.AccordionItem(
                [
                    dmc.AccordionControl(
                        dmc.Group(
                            [
                                dmc.Text("How to use this website", size="lg", fw=700),
                            ]
                        )
                    ),
                    dmc.AccordionPanel(
                        dmc.Text(using_website_string, size="md")
                    ),
                ],
                value="usingWebsite",
                ),

                dmc.AccordionItem(
                [
                    dmc.AccordionControl(
                        dmc.Group(
                            [
                                dmc.Text("Additional Resources", size="lg", fw=700),
                            ]
                        )
                    ),
                    dmc.AccordionPanel(
                        dmc.Anchor(
                            "https://www.samhsa.gov/data/faq-nsduh", 
                            href="https://www.samhsa.gov/data/faq-nsduh",
                            style={"fontSize": "18px", "marginBottom": "10px"}
                        ),
                    ),
                ],
                value="mentalHealth",
                )
            ],
          style={"marginBottom": "20px"},
        ),
    
         dmc.Paper(
            children=[
                dmc.Text("Data Citation", td="underline", fw=700, style={"fontSize":"18px", "marginTop": "10px"}),
                dmc.Text(
                    "Author: Substance Abuse and Mental Health Services Administration (SAMHSA) Center for Behavioral Health Statistics and Quality", 
                    id="documentation-citation",
                    style={"fontSize": "12px", "marginBottom": "10px"}
                ),
                dmc.Text(
                    "Date of publication: October 25, 2023", 
                    id="documentation-citation",
                    style={"fontSize": "12px", "marginBottom": "10px"}
                ),
                dmc.Text(
                    "Title: 2022 National Survey on Drug Use and Health (NSDUH)", 
                    id="documentation-citation",
                    style={"fontSize": "12px", "marginBottom": "10px"}
                ),
                dmc.Text(
                    "Publisher: SAMHSA", 
                    id="documentation-citation",
                    style={"fontSize": "12px", "marginBottom": "10px"}
                ),
                dmc.Anchor(
                    "URL: https://www.samhsa.gov/data/data-we-collect/nsduh/datafiles?year=2022&data_collection=1186", 
                    href="https://www.samhsa.gov/data/data-we-collect/nsduh/datafiles?year=2022&data_collection=1186",
                    style={"fontSize": "12px", "marginBottom": "10px"}
                ),
            ],
            withBorder=True,
            p="lg"
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
