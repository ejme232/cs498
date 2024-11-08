from dash import html, register_page, Input, Output, callback, no_update
from dash_mantine_components import Container, Text, Button
import dash_ag_grid as dag
import pandas as pd
import time

register_page(__name__)

df = pd.read_csv("../NSDUH_2022_Tab.tsv")

# Set the first row as the column names
df.columns = df.iloc[0]  
# remove the first row from the data as it's being used as the table header
df = df[1:]  

#define the default column properties for AgGrid
defaultColDef = {
    # allows the columns to resize proportionally
    "flex": 1,
    # set the minimum width of each column
    "minWidth": 150,
    # set ability to be sorted 
    "sortable": True,
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
    Output("export-data-grid", "exportDataAsTsv"),
    Input("tsv-button", "n_clicks"),
)
#define how the export data as a tsv will be handled
def export_data_as_tsv(n_clicks):
    if n_clicks:
        return True
    return False

#define the layout of the page
layout = html.Div(
        id="data-page-content",
        children=[
            #insert the container that has the Ag-Grid
           data_page_container
        ]
)