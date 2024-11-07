from dash import html
import dash_mantine_components as dmc
from dash_iconify import DashIconify  # Import DashIconify for icons

# define the style of the header bar shown across all pages
def create_header():
    # create a hamburger menu that when clicked will show the page options to navigate to on the left side of the header
    hamburger_menu = dmc.Menu(
        id="hamburger-menu",
        children=[
            # utilize a hamburger icon for the button
            dmc.MenuTarget(dmc.Button("☰", variant="light", size="sm")), 
            # set up the dropdown options for the hamburger menu
            dmc.MenuDropdown(
                children=[
                    dmc.NavLink(label="Home", href="/home"),
                    dmc.NavLink(label="Data", href="/data"),
                    dmc.NavLink(label="Documentation", href="/documentation"),
                    dmc.NavLink(label="About", href="/about"),
                ]
            ),
        ],
    )

    ## Settings dropdown menu for the right side of the header
    settings_menu = dmc.Menu(
        id="settings-menu",
        children=[
            dmc.MenuTarget(
                dmc.ActionIcon(
                    DashIconify(icon="ep:setting", width=24),
                    variant="light",
                    size="md",
                )
            ),
        ],
    )

    # Middle of header with website name
    header_title = dmc.Text(
        "Website Name", style={"fontSize": "24px", "fontWeight": "bold", "color": '#2c3e50'}
    )

    #return all components of the header with the designated stylizing
    return dmc.Group(
        justify="space-between",
        style={"padding": "10px", "borderBottom": "1px solid #ccc", "backgroundColor": "#f8f9fa"},
        children=[hamburger_menu, header_title, settings_menu],
    )
