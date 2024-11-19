from  dash_mantine_components import Menu, Button, NavLink, MenuTarget, MenuDropdown, Text, Group, Box

# define the style of the header bar shown across all pages
# create a hamburger menu that when clicked will show the page options to navigate to on the left side of the header
def create_header(pages):
    hamburger_menu = Menu(
        id="hamburger-menu",
        children=[
            # utilize a hamburger icon for the button
            MenuTarget(Button("☰", variant="light", size="sm")), 
            # set up the dropdown options for the hamburger menu
            MenuDropdown(
                children=[
                    NavLink(label=f"{page['name']}", href=page["relative_path"]) 
                    for page in pages.values()
                ]
            
            ),
        ],
    )

    # Middle of header with website name
    header_title = Group(
        children=[
            Text("Mind the Gap", style={"fontSize": "36px", "fontWeight": "bold", "color": '#2c3e50', "lineHeight": "1.2", "textAlign": "center"}),
            Text("Bridging Data on Substance Abuse and Mental Health", style={"fontSize": "18px", "fontStyle": "italic", "color": '#7f8c8d', "lineHeight": "1.2", "textAlign": "center"}),
        ],
        style={"display": "flex", "flexDirection": "column", "alignItems": "center"},
    )

    # return all components of the header with the designated stylizing
    layout = Box(
        style={"padding": "10px", "borderBottom": "1px solid #ccc", "backgroundColor": "#f8f9fa", "display": "flex", "alignItems": "center", "justifyContent": "space-between"},
        children=[
            # Use flex to position items properly
            Group(
                style={
                    "flex": 1,
                    "display": "flex",
                    "alignItems": "center",
                    "justifyContent": "flex-start",  # Align hamburger to the left
                },
                children=[hamburger_menu],
            ),
            Group(
                style={
                    "flex": 1,
                    "display": "flex",
                    "alignItems": "center",
                    "justifyContent": "center",  # Center the text
                },
                children=[header_title],
            ),
            Group(
                style={
                    "flex": 1,
                    "display": "flex",
                    "alignItems": "center",
                    "justifyContent": "flex-end",  # Right-align other potential elements
                },
                children=[],  # Placeholder for additional elements like settings
            ),
        ],
    )
    return layout
