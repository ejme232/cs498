from dash import html, register_page, Input, Output, State, callback, dcc, ctx
from dash_mantine_components import Container
import dash_ag_grid as dag
import pandas as pd
import pathlib

file_path = str(pathlib.Path(__file__).parents[2]) + "/NSDUH_2022.tsv"
df = pd.read_csv(file_path, sep='\t')
register_page(__name__)

default_grid_options = {
    'pagination': True,
    'paginationPageSize': 10,
    'defaultColDef': {
        'sortable': True,
        'filter': True,
        'resizable': True,
        'minWidth': 100,
        'floatingFilter': True
    },
    'enableRangeSelection': True,
    'animateRows': True,
}

about_page_container = Container(
    id="about-page-container",
    children=[
        html.H1("TSV Data Viewer and Multi-Column Filter"),

        # Multi-select dropdown for columns
        dcc.Dropdown(
            id='column-selector',
            options=[{"label": col, "value": col} for col in df.columns],
            value=[df.columns[0]],
            multi=True,
            placeholder="Select columns to display"
        ),
        
        # AG Grid component
        dag.AgGrid(
            id='grid',
            columnDefs=[
                {"field": col, "headerName": col} for col in df.columns
            ],
            rowData=[],
            columnSize="sizeToFit",
            defaultColDef={
                "resizable": True,
                "sortable": True,
                "filter": True,
                "minWidth": 100,
            },
            dashGridOptions=default_grid_options,
            style={"height": "600px", "width": "100%"}
        ),

        html.Button("Download Selected Data", id="download-button", n_clicks=0),
        dcc.Download(id="download-data"),
    ],
    style={"padding": "20px"}
)

@callback(
    Output('grid', 'columnDefs'),
    Output('grid', 'rowData'),
    Input('column-selector', 'value')
)
def update_grid(selected_columns):
    if not selected_columns:
        selected_columns = [df.columns[0]]

    filtered_df = df[selected_columns]
    
    column_defs = [
        {
            "field": col,
            "headerName": col,
            "filter": "agTextColumnFilter",
            "filterParams": {
                "buttons": ["reset", "apply"],
                "closeOnApply": True
            }
        } for col in selected_columns
    ]
    row_data = filtered_df.to_dict('records')
    
    return column_defs, row_data

@callback(
    Output("download-data", "data"),
    Input("download-button", "n_clicks"),
    State('column-selector', 'value'),
    prevent_initial_call=True
)
def download_filtered_data(n_clicks, selected_columns):
    if not selected_columns:
        selected_columns = [df.columns[0]]
    
    filtered_df = df[selected_columns]
    return dcc.send_data_frame(filtered_df.to_csv, "filtered_data.tsv", sep='\t', index=False)

layout = html.Div(
    id="about-page-content",  
    children=[
        about_page_container
    ]
)