import dash_mantine_components as dmc
from dash_iconify import DashIconify

# define the style of the header bar shown across all pages
# create a hamburger menu that when clicked will show the page options to navigate to on the left side of the header
def create_header(pages):
    hamburger_menu = dmc.Menu(
        id="hamburger-menu",
        children=[
            # utilize a hamburger icon for the button
            dmc.MenuTarget(dmc.Button("☰", color="#2c3e50", variant="light", size="md")), 
            # set up the dropdown options for the hamburger menu
            dmc.MenuDropdown(
                children=[
                    dmc.NavLink(label=f"{page['name']}", href=page["relative_path"]) 
                    for page in pages.values()
                ]
            
            ),
        ],
    )

    # Middle of header with website name
    header_title = dmc.Group(
        children=[
            dmc.Text("Mind the Gap", style={"fontSize": "36px", "fontWeight": "bold", "color": '#2c3e50', "lineHeight": "1.2", "textAlign": "center"}),
            dmc.Text("Bridging Data on Substance Abuse and Mental Health", style={"fontSize": "18px", "fontStyle": "italic", "color": '#7f8c8d', "lineHeight": "1.2", "textAlign": "center"}),
        ],
        style={"display": "flex", "flexDirection": "column", "alignItems": "center"},
    )

    # a what do I do button that points the user to the documentation page for a further explanation
    what_to_do = dmc.HoverCard(
        id="nav-to-documentation",
        shadow="md",
        width = 500,
        withArrow = True,
        children=[
            dmc.HoverCardTarget(
                DashIconify(icon="mingcute:question-line", width=30, color="#2c3e50"),
            ),
            dmc.HoverCardDropdown(
                [
                    dmc.Text("Not sure what to do? Click the button below to go to the documentation page to learn more."),
                    dmc.NavLink(
                        id="navlink-documentation",
                        label="Click here",
                        active = True, 
                        variant = "filled",
                        href="/documentation",
                    )
                ]
            ),
        ]
    )
    # return all components of the header with the designated stylizing
    layout = dmc.Box(
        style={"padding": "10px", "borderBottom": "1px solid #ccc", "backgroundColor": "#f8f9fa", "display": "flex", "alignItems": "center", "justifyContent": "space-between"},
        children=[
            # Use flex to position items properly
            dmc.Group(
                style={
                    "flex": 1,
                    "display": "flex",
                    "alignItems": "center",
                    "justifyContent": "flex-start",  # Align hamburger to the left
                },
                children=[hamburger_menu],
            ),
            dmc.Group(
                style={
                    "flex": 1,
                    "display": "flex",
                    "alignItems": "center",
                    "justifyContent": "center",  # Center the text
                },
                children=[header_title],
            ),
            dmc.Group(
                style={
                    "flex": 1,
                    "display": "flex",
                    "alignItems": "center",
                    "justifyContent": "flex-end",  # Right-align other potential elements
                },
                children=[what_to_do],  # Placeholder for additional elements like settings
            ),
        ],
    )
    return layout
