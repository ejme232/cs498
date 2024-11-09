from dash import html, register_page, Input, Output, callback, no_update, dcc
from dash_mantine_components import Container, Text, Button
import dash_ag_grid as dag
import pandas as pd
import time
import dash_bootstrap_components as dbc
import io
import pathlib

register_page(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

tsv_file = str(pathlib.Path(__file__).parents[2]) + "/NSDUH_2022_Tab.tsv"
print(tsv_file)

df = pd.read_csv(tsv_file)

# Set the first row as the column names
df.columns = df.iloc[0]  
# remove the first row from the data as it's being used as the table header
df = df[1:]  

columnDefs = [{"field": col, "headerName": col} for col in df.columns]


#define the default column properties for AgGrid
defaultColDef = {
    # allows the columns to resize proportionally
    "flex": 1,
    # set the minimum width of each column
    "minWidth": 150,
    # set ability to be sorted 
    "sortable": False,
    # set ability for columns to be resized
    "resizable": True,
}

#container to hold data page elements
data_page_container =  Container(
    id="data-page-container",
    children=[
        #title for data page
        Text("Data Page", id="data-page-title", style={
            "fontSize": "22px", 
            "fontWeight": "bold", 
            "marginBottom": "10px", 
            "color": "#34495e"
        }),

        #set up AgGrid in order to display data used in a table format 
        dag.AgGrid(
            id="infinite-row-data-grid",
            columnDefs = columnDefs,
            defaultColDef=defaultColDef,
            # set the grid to load data utilizing infinite scrolling (helps with page loading for large data sets)
            rowModelType="infinite",
            #specify aspects of the grid
            dashGridOptions={
                # the number of rows rendered outside of the viewable area
                "rowBuffer": 0,
                # limits the blocks stored in the cache
                "maxBlocksInCache": 2,
                # sets the cache block to contain 100 rows
                "cacheBlockSize": 100,
                #allows up to 2 blocks overflowthe cache size
                "cacheOverflowSize": 2,
                # limit the number of concurrent data requests
                "maxConcurrentDatasourceRequests": 2,
                #inital row count to display
                "infiniteInitialRowCount": 1,
                #enable multiple row selection
                "rowSelection": "multiple",
                #enable pagination
                "pagination": True,
                # auto-size the page when using pagination
                "paginationAutoPageSize": True,
            }
        ),

        #include a button to download as a TSV
        Button(
            "Download TSV",
            id = "download-tsv-button",
            n_clicks=0
        ),
        
        Text("Accessible headers and quick-loading data table coming soon", style={"fontSize": "14px", "fontStyle": "italic"}),

        #Download component
        dcc.Download(id="download-tsv"),
    ],
    #add padding around the container for visibility/spacing
    style={"padding": "20px"}
)

# create a callback that handles the infinite scrolling feature of AgGrid
@callback(
    Output("infinite-row-data-grid", "getRowsResponse"),
    Input("infinite-row-data-grid", "getRowsRequest"),
)

# define the infinite scroll feature so the table loads properly
def infinite_scroll(request):
    # simulates a delay to represent slower data retrieval/processing
    time.sleep(2)

    #if no request then return no update
    if request is None:
        return no_update
    
    #sets up retrieval of only the set of rows requested by the grid
    partial = df.iloc[request["startRow"]: request["endRow"]]
    return {"rowData": partial.to_dict("records"), "rowCount": len(df.index)}

#create a callback to handle exporting the data into a TSV file
@callback(
    Output("download-tsv", "data"),
    Input("download-tsv-button", "n_clicks"),
    prevent_initial_call=True
)
#define how the export data as a tsv will be handled
def export_data_as_tsv(n_clicks):
    if n_clicks > 0:
        #Replace with your actual data to be exported
        tsv_buffer = io.StringIO()
        df.to_csv(tsv_buffer, sep='\t', index=False)
        tsv_buffer.seek(0)
        return dcc.send_data_frame(df.to_csv, "data.tsv", sep='\t', index=False)


#define the layout of the page
layout = html.Div(
        id="data-page-content",
        children=[
            #insert the container that has the Ag-Grid
           data_page_container
        ]
)