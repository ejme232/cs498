from  dash_mantine_components import Menu, Button, NavLink, MenuTarget, MenuDropdown, ActionIcon,Text, Group
from dash_iconify import DashIconify  # Import DashIconify for icons

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

    # Settings dropdown menu for the right side of the header
    settings_menu = Menu(
        id="settings-menu",
        children=[
            MenuTarget(
                ActionIcon(
                    DashIconify(icon="ep:setting", width=24),
                    variant="light",
                    size="md",
                )
            ),
        ],
    )

    # Middle of header with website name
    header_title = Text(
        "Website Name", style={"fontSize": "24px", "fontWeight": "bold", "color": '#2c3e50'}
    )

    # return all components of the header with the designated stylizing
    layout = Group(
            style={"padding": "10px", "borderBottom": "1px solid #ccc", "backgroundColor": "#f8f9fa", "display": "flex", "alignItems": "center", "justifyContent": "space-between"},
            children=[hamburger_menu, header_title, settings_menu],
    )
    return layout
