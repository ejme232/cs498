from dash import html, register_page, Input, Output, State, callback, dcc, ctx
from dash_mantine_components import Container
import dash_table
import pandas as pd
import pathlib

file_path = str(pathlib.Path(__file__).parents[2]) + "/NSDUH_2022.tsv"
df = pd.read_csv(file_path, sep='\t')
rows = len(df.index)
register_page(__name__)
current_page = 0

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
        
        # Table to display data with dynamic pagination
        dash_table.DataTable(
            id='table',
            columns=[{"name": col, "id": col} for col in df.columns],
            data=[],
            page_size=10,
            page_current=current_page,
            style_table={'overflowX': 'auto'},
            style_cell={
                'minWidth': '100px',
                'maxWidth': '300px',
                'overflow': 'hidden',
                'textOverflow': 'ellipsis'
            }
        ),

        # Button to download filtered data
        html.Button("Download Data", id="download-button", n_clicks=0),
        dcc.Download(id="download-data"),
        
        html.Div([
            html.Button("Previous", id="prev-page"),
            html.Button("Next", id="next-page"),
            html.Span(id="page-display", style={'margin-left': '10px'})
        ], style={'display': 'flex', 'gap': '10px', 'margin-top': '10px'})
    ],
    style={"padding": "20px"}
)

@callback(
    Output('table', 'columns'),
    Output('table', 'data'),
    Output('page-display', 'children'),
    [Input('column-selector', 'value'),
     Input('table', 'page_current'),
     Input('table', 'page_size'),
     Input('prev-page', 'n_clicks'),
     Input('next-page', 'n_clicks'),
    ],
    [State('table', 'page_current')]
)
def update_table(selected_columns, page_current, page_size, prev_clicks, next_clicks, page_number):
    global current_page
    if not selected_columns:
        selected_columns = [df.columns[0]]
    
    # Filter DataFrame by selected columns
    filtered_df = df[selected_columns]
    
    # Handle pagination
    if ctx.triggered_id == "prev-page" and current_page - 1 > 1:
        current_page = current_page - 1
    elif ctx.triggered_id == "next-page" and (current_page + 1) * page_size < len(filtered_df):
        current_page = current_page + 1
    
    # Calculate pagination
    start_row = current_page * page_size
    end_row = start_row + page_size
    paginated_df = filtered_df.iloc[start_row:end_row]
    
    # Prepare table data
    table_columns = [{"name": col, "id": col} for col in filtered_df.columns]
    table_data = paginated_df.to_dict('records')
    
    # Create page display text
    total_pages = -(-len(filtered_df) // page_size)  # Ceiling division
    page_text = f"Page {current_page} of {total_pages}"
    
    return table_columns, table_data, page_text

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