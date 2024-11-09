from dash import html, register_page
from dash_mantine_components import Container, Title, Text
import dash_mantine_components as dmc
#define the home page
register_page(__name__, path="/")

home_page_container = Container(
                id="home-page-container",
                children=[
                    Title(f"Home Page", id="home-page-title", order=2),
                    Text("Days of Alcohol Usage by County Type"),
                    dmc.BarChart(
                        id="alcohol-by-county-bar",
                        # height of the chart
                        h=300,  
                        # field from the data dictionary for the x-axis
                        dataKey="county-type",  
                        # data field is empty for now
                        data=[],
                        #label the x and y axis
                        xAxisLabel="County Type",
                        yAxisLabel="# of days of alcohol usage",
                        #give name and color to the three criteria
                        series=[
                            {"name": "Large Metro", "color": "violet.6"},
                            {"name": "Small Metro", "color": "blue.6"},
                            {"name": "Nonmetro", "color": "teal.6"},
                        ]
                    ),

                    Text("Alcohol Usage and KPI Score (measures psychological distress)"),
                    dmc.ScatterChart(
                        id="alcohol-distress-scatter",
                        # height of the chart
                        h=300,
                        #field for x and y axis
                        dataKey={"x": "alcohol", "y":"KPI"},
                        #data field is empty for now
                        data=[],
                        #label the x and y axis
                        xAxisLabel="# of days of alcohol usage",
                        yAxisLabel="KPI Score",
                    ),

                    Text("More charts and data to be added", style={"fontSize": "14px", "fontStyle": "italic"}),
                ],
                style={"padding": "40px", "maxWidth": "800px", "margin": "auto"}
            )
layout = html.Div(
        id="home-page-content",
        children=[
            home_page_container
        ]
    )
