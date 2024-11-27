from dash import html, register_page, dcc
from dash_mantine_components import Container, Group, Title, BarChart, ScatterChart, Text, Popover, MultiSelect, Button,PopoverTarget, PopoverDropdown


#define the home page
register_page(__name__, path="/")

chart_one_container = Container(
    id="chart-one-container",
    children=[           
        Title("Days of Alcohol Usage by County Type", order=4, style={"marginBottom": "10px"}),
        Group(
            children=[
                Container(
                    id="bar-chart-container",
                    children=[
                        BarChart(
                            id="alcohol-by-county-bar",
                            # height of the chart
                            h=300,  
                            # field from the data dictionary for the x-axis
                            dataKey="county-type",  
                            # data field is empty as placeholder for actual data
                            data=[],
                            #label the x and y axis
                            xAxisLabel="County Type",
                            yAxisLabel="# of days of alcohol usage",
                            #give name and color to the three criteria
                            series=[
                                {"name": "Large Metro", "color": "violet.6"},
                                {"name": "Small Metro", "color": "blue.6"},
                                {"name": "Nonmetro", "color": "teal.6"},
                            ],
                        ),
                    ],
                    style={"flex": "3", "paddingRight": "20px"},
                ),
                Container(
                    id="bar-chart-filter-sidebar",
                    children=[
                        Title("Filters", order=5, style={"fontSize": "14px", "marginBottom": "10px"}),
                        Popover(
                            id="bar-chart-popover",
                            position="bottom",
                            withArrow=True,
                            trapFocus=True,
                            children=[
                                PopoverTarget(Button("Toggle Filter")),
                                PopoverDropdown(
                                    [
                                        MultiSelect(
                                            id="bar-chart-filter",
                                            data=["1", "2", "3"],  # Replace with dynamic data
                                            label="County Type",
                                            placeholder="Select county types",
                                        ),
                                        Button("Filter Bar Chart", id="bar-chart-filter-button"),
                                    ]
                                ),
                            ],
                        ),       
                    ],
                    style={
                        "padding": "10px",
                        "width": "250px",
                        "borderLeft": "1px solid #ddd",
                        "marginLeft": "20px",
                        "boxSizing": "border-box",
                    },
                ),
            ],
            style={"display": "flex", "flexDirection": "row", "alignItems": "flex-start", "width": "100%"},
        ),
    ],
    style={"marginBottom": "30px", "padding": "20px", "borderBottom": "1px solid #ddd", "borderRadius": "5px", "maxWidth": "800px", "margin": "auto"},
)
        
chart_two_container = Container(
    id="chart-two-container",
    children=[
        Title("Alcohol Usage and KPI Score (measures psychological distress)", order=4, style={"marginBottom": "10px"}),
        Group(
            children=[
                ScatterChart(
                    id="alcohol-distress-scatter",
                    # height of the chart
                    h=300,
                    #field for x and y axis
                    dataKey={"x": "alcohol", "y":"KPI"},
                    #data field is empty for now as placeholder for actual data
                    data=[],
                    #label the x and y axis
                    xAxisLabel="# of days of alcohol usage",
                    yAxisLabel="KPI Score",
                ), 
            ]
        )
    ],
    style={"padding": "20px", "margin": "auto", "maxWidth": "800px"}
)
                    
home_page_container = Container(
    id="home-page-container",
    children=[
        Title(f"Home Page", id="home-page-title", order=2, style={"marginBottom": "20px"}),
        chart_one_container,
        chart_two_container,
        Text("More charts and data to be added", style={"fontSize": "14px", "fontStyle": "italic"}),
    ],
    style={"padding": "20px", "margin": "auto", "maxWidth": "900px", "textAlign": "left"},
)


layout = html.Div(
    id="home-page-content",
    children=[
        home_page_container
    ],
)
