from dash import html, dcc, register_page, Input, Output, State, callback, callback_context
import pandas as pd
import pathlib
import dash_mantine_components as dmc
import plotly.graph_objects as go

file_path = str(pathlib.Path(__file__).parents[2]) + "/NSDUH_2022.tsv"
df = pd.read_csv(file_path, sep='\t')

#define the home page
register_page(__name__, path="/")

chart_one_container = dmc.Container(
    id="chart-one-container",
    children=[           
        dmc.Title("Days of Alcohol Usage by County Type", order=4, style={"marginBottom": "10px"}),
        dmc.Group(
            children=[
                dmc.Container(
                    id="bar-chart-container",
                    children=[
                        dmc.BarChart(
                            id="alcohol-by-county-bar",
                            # height of the chart
                            h=600,  
                            # field from the data dictionary for the x-axis
                            dataKey="county-type",  
                            # data field is empty as placeholder for actual data
                            data=[],  # Data will be dynamically updated via callback
                            #label the x and y axis
                            xAxisLabel="County Type",
                            yAxisLabel="Average # of Days of Alcohol Usage",
                            series=[
                                {
                                    "name": "Average # of Days of Alcohol Usage", 
                                    "color": "blue.6",
                                 }
                            ],

                            highlightHover=False,
                            tooltipProps={ 
                                    "wrapperStyle": {
                                        "backgroundColor": "rgba(255, 255, 255, 0.9)",
                                        "borderRadius": "8px",
                                        "padding": "10px",
                                        "boxShadow": "0 2px 8px rgba(0, 0, 0, 0.3)",
                                        "color": "#333"},
                            },
                            
                        ),
                    ],
                    style={"flex": "4", "paddingRight": "20px"},
                ),
                dmc.Container(
                    id="bar-chart-filter-sidebar",
                    children=[
                        dmc.Title("Filters", order=5, style={"fontSize": "14px", "marginBottom": "10px"}),
                        dmc.Popover(
                            id="bar-chart-popover",
                            position="bottom",
                            withArrow=True,
                            trapFocus=True,
                            children=[
                                dmc.PopoverTarget(dmc.Button("Toggle Filter")),
                                dmc.PopoverDropdown(
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
                        "flex": "1",
                        "borderLeft": "1px solid #ddd",
                        "marginLeft": "20px",
                        "boxSizing": "border-box",
                    },
                ),
            ],
            style={"display": "flex", "flexDirection": "row", "alignItems": "flex-start", "width": "100%"},
        ),
    ],
    style={"marginBottom": "30px", "padding": "20px", "borderBottom": "1px solid #ddd", "borderRadius": "5px", "maxWidth": "1200px", "margin": "auto"},
)

def create_heatmap(df):
    heatmap_figure = go.Figure(data=go.Histogram2d(
        x=df['ALCYRTOT'],
        y=df['KSSLR6MONED'],
        colorscale='Blues',
    ))
    heatmap_figure.update_layout(
        title="Alcohol Usage and KPI Score",
        xaxis_title="Days of Alcohol Usage",
        yaxis_title="KPI Score (Past Month)",
        height=500,
        margin={"l": 50, "r": 50, "t": 50, "b": 50},
    )
    return heatmap_figure

heatmap_figure = create_heatmap(df)

chart_two_container = dmc.Container(
    id="chart-two-container",
    children=[
        dmc.Title("Alcohol Usage and KPI Score (measures psychological distress)", order=4, style={"marginBottom": "10px"}),
        dmc.Group(
            children=[
                dmc.Container(
                    id="heatmap-container",
                    children=[
                        dcc.Graph(
                            id="alcohol-distress-heatmap",
                            figure=heatmap_figure,
                           config={"displayModeBar": False},
                           style={"height": "300px"}
                        ), 
                    ],
                    style={"flex": "4", "paddingRight": "20px"},
                ),
                dmc.Container(
                    id="heatmap-filter-sidebar",
                    children=[
                        dmc.Title("Filters", order=5, style={"fontSize": "14px", "marginBottom": "10px"}),
                        dmc.Popover(
                            id="heatmap-popover",
                            position="bottom",
                            withArrow=True,
                            trapFocus=True,
                            children=[
                                dmc.PopoverTarget(dmc.Button("Toggle Filter")),
                                dmc.PopoverDropdown(
                                    [
                                        dcc.Slider(
                                            id='alcohol-slider',
                                            min=0,
                                            max=365,
                                            step=1,
                                            value=365,
                                            marks={i: str(i) for i in range(0, 365, 30)},
                                            tooltip={"placement": "bottom"}
                                        )
                                    ],
                                    style={"width": "400px"}
                                ),
                            ],
                        ),     
                    ],
                    style={
                        "padding": "10px",
                        "flex": "1",
                        "borderLeft": "1px solid #ddd",
                        "marginLeft": "20px",
                        "boxSizing": "border-box",
                    },
                ),
                
            ],
            style={"display": "flex", "flexDirection": "row", "alignItems": "flex-start", "width": "100%"},

        )
    ],
    style={"marginBottom": "30px", "padding": "20px", "borderBottom": "1px solid #ddd", "borderRadius": "5px", "maxWidth": "1200px", "margin": "auto"},
)
                    
home_page_container = dmc.Container(
    id="home-page-container",
    children=[
        dmc.Text("Home", style={"fontSize": "32px", "fontWeight": "bold", "marginBottom": "10px", "color": "#2c3e50", "textAlign": "left"}),
        dmc.Divider(style={"marginBottom": "20px"}),        
        chart_one_container,
        chart_two_container,
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
@callback(
    Output('alcohol-distress-heatmap', 'figure'),
    Input('alcohol-slider', 'value')
)

def update_heatmap(selected_value):
    filtered_df = df[df['ALCYRTOT'] <= selected_value]
    return create_heatmap(filtered_df)