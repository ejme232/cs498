from dash import html
import dash_mantine_components as dmc
from dash_iconify import DashIconify  # Import DashIconify for icons

# Define the reusable header with the hamburger menu
def create_header():
    hamburger_menu = dmc.Menu(
        id="hamburger-menu",
        children=[
            dmc.MenuTarget(dmc.Button("☰", variant="light", size="sm")),  # Hamburger icon as a button
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

    header_title = dmc.Text(
        "Website Name", style={"fontSize": "24px", "fontWeight": "bold", "color": '#2c3e50'}
    )

    return dmc.Group(
        justify="space-between",
        style={"padding": "10px", "borderBottom": "1px solid #ccc", "backgroundColor": "#f8f9fa"},
        children=[hamburger_menu, header_title, settings_menu],
    )
