from dash import html, register_page, dcc, Input, Output, State, callback, callback_context
import pandas as pd
import pathlib
from dash_mantine_components import Container, Group, Title, BarChart, ScatterChart, Text, Popover, MultiSelect, Button,PopoverTarget, PopoverDropdown

file_path = str(pathlib.Path(__file__).parents[2]) + "/NSDUH_2022.tsv"
df = pd.read_csv(file_path, sep='\t')

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
                            data=[],  # Data will be dynamically updated via callback
                            #label the x and y axis
                            xAxisLabel="County Type",
                            yAxisLabel="Average # of Days of Alcohol Usage",
                            series=[
                                {"name": "Average # of Days of Alcohol Usage", "color": "blue.6"}
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
                                        dcc.Checklist(
                                            options=[{'label': 'Select All', 'value': 'all'}],
                                            value=['all'],
                                            id='county-type-select-all'
                                        ),
                                        dcc.Checklist(
                                            options=[{'label': i, 'value': i} for i in df['COUTYP4'].unique()],
                                            value=df['COUTYP4'].unique().tolist(),
                                            id='county-type-filter'
                                        )
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

@callback(
    Output('county-type-filter', 'value'),
    Output('county-type-select-all', 'value'),
    Input('county-type-filter', 'value'),
    Input('county-type-select-all', 'value'),
    State('county-type-filter', 'options'),
    prevent_initial_call=True,
)
def sync_center_checklist(county_type_selected, all_selected, all_county_type):
    all_county_type = [item['value'] for item in all_county_type]
    ctx = callback_context
    input_id = ctx.triggered[0]['prop_id'].split('.')[0]
    if input_id == 'county-type-filter':
        all_selected = ['all'] if set(county_type_selected) == set(all_county_type) else []
    else:
        county_type_selected = all_county_type if all_selected else []
    return county_type_selected, all_selected

@callback(
    Output('alcohol-by-county-bar', 'data'),
    Input('county-type-filter', 'value')
)
def update_bar_chart_data(selected_county_types):
    # Filter the DataFrame based on selected county types
    filtered_df = df[df['COUTYP4'].isin(selected_county_types)]
    
    # Group by 'COUTYP4' (county type) and calculate the average of 'ALCYRTOT'
    grouped_data = (
        filtered_df.groupby('COUTYP4')['ALCYRTOT']
        .apply(lambda x: x.astype(int).mean())  # Ensure numeric and calculate average
        .reset_index()
    )
    
    # Rename columns for better clarity
    grouped_data.columns = ['county-type', 'Average # of Days of Alcohol Usage']
    
    # Convert DataFrame to the list of dictionaries format required for the Bar Chart
    bar_data = grouped_data.to_dict('records')
    
    return bar_data
