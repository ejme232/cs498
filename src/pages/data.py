from dash import html, register_page, Input, Output, callback, no_update, dcc
from dash_iconify import DashIconify
import dash_mantine_components as dmc
import dash_ag_grid as dag
import pandas as pd
import pathlib
import io
import time


file_path = str(pathlib.Path(__file__).parents[2]) + "/NSDUH_2022.tsv"
df = pd.read_csv(file_path, sep='\t')

register_page(__name__)

columnDefs = [{"field": col, "headerName": col, "minWidth": 150, "flex": 1} for col in df.columns]

defaultColDef = {
    "resizable": True,
    "sortable": True,
    "filter": True,
    "floatingFilter": True,
    "flex": 1,
    "autoSize": True,
}

#container to hold data page elements
data_page_container =  dmc.Container(
    id="data-page-container",
    children=[
        #title for data page
        dmc.Text("Data", style={"fontSize": "32px", "fontWeight": "bold", "marginBottom": "10px", "color": "#2c3e50", "textAlign": "left"}),
        dmc.Divider(style={"marginBottom": "20px"}),
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
            },
            style={"height": "700px", "marginBottom": "20px", "width": "100%"},
        ),

        dmc.Button(
            "Download CSV",
            id="csv-download-button",
            n_clicks=0,
            style={"marginBottom": "20px"},
            ),
            dcc.Download(id="csv-download"),
        
        dmc.HoverCard(
            id="nav-to-codebook",
            shadow="md",
            width = 500,
            withArrow = True,
            children=[
                dmc.HoverCardTarget(
                    dmc.Button("To learn more about the data", color="blue", size="sm"),
                ),
                dmc.HoverCardDropdown(
                    [
                        dmc.Text("To access the data codebook, and learn more about the column headings, click the button below."),
                        dmc.NavLink(
                            id="navlink-codebook",
                            label="Click here",
                            active = True, 
                            variant = "filled",
                            target="_blank",
                            href="https://www.samhsa.gov/data/system/files/media-puf-file/NSDUH-2022-DS0001-info-codebook.pdf",        
                        ),
                                   
                    ]
                ),
            ]
        ),
    ],
    #add padding around the container for visibility/spacing
    style={"padding": "20px"},
)

# create a callback that handles the infinite scrolling feature of AgGrid
@callback(
    Output("infinite-row-data-grid", "getRowsResponse"),
    Input("infinite-row-data-grid", "getRowsRequest"),
)

# define the infinite scroll feature so the table loads properly
def infinite_scroll(request):
    # simulates a delay to represent slower data retrieval/processing
    time.sleep(1)

    #if no request then return no update
    if request is None:
        return no_update
    
    start_row = request["startRow"]
    end_row = request["endRow"]
    
    #sets up retrieval of only the set of rows requested by the grid
    partial_data = df.iloc[start_row:end_row]
    return {"rowData": partial_data.to_dict("records"), "rowCount": len(df)}

@callback(
    Output("csv-download", "data"),
    Input("csv-download-button", "n_clicks"),
    prevent_initial_call=True
)
def download_full_csv(n_clicks):
    if n_clicks > 0:
        return dcc.send_data_frame(df.to_csv, "NSDUH_2022.csv", index=False)


# Define the layout of the page
layout = html.Div(
    id="data-page-content",
    children=[data_page_container],
    style={"backgroundColor": "#f8f9fa", "minHeight": "100vh"},
)
