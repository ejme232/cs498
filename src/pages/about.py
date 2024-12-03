from dash import html, register_page
import dash_mantine_components as dmc

register_page(__name__)

about_page_container = dmc.Container(
    id="about-page-container",
    children=[
        dmc.Text("About", style={"fontSize": "32px", "fontWeight": "bold", "marginBottom": "10px", "color": "#2c3e50", "textAlign": "left"}),
        dmc.Divider(style={"marginBottom": "20px"}),

        dmc.Text("Purpose", id="purpose-heading", style={"fontSize": "24px", "fontWeight": "bold", "marginBottom": "15px", "color": "#2c3e50", "maxWidth": "800px"}),
        dmc.Text("The goal of this project is to bring together data on mental health and substance abuse in order to bring awareness and information to the public.", style={"fontSize": "16px", "lineHeight": "1.5", "marginBottom": "30px", "maxWidth": "800px", "color": "#34495e"}),  
                    
        dmc.Text("What's Next", id="whats-next-heading", style={"fontSize": "24px", "fontWeight": "bold", "marginBottom": "15px", "color": "#2c3e50", "maxWidth": "800px"}),
        # create a coming soon section stylized as a timeline of sorts
        dmc.Timeline(
            id = "timeline",
            active = 0,
            bulletSize = 20,
            lineWidth = 5,
            style={"maxWidth": "800px", "marginTop": "10px"},
            children = [
                dmc.TimelineItem(
                    id = "timeline-item-1",
                    title="Further Enhance Homepage",
                    children=[
                        dmc.Text(
                            "Add more visualizations and key data to the homepage",
                            c="dimmed",
                            size="sm",
                        ),
                    ],
                ),
                dmc.TimelineItem(
                    id = "timeline-item-2",
                    title="Add More Data",
                    children=[
                        dmc.Text(
                            "Pull in more mental health data from previous years and other sources.",
                            c="dimmed",
                            size="sm",
                        ),
                    ],
                ),
                dmc.TimelineItem(
                    id = "timeline-item-3",
                    title="Enhance Data Filtering",
                    children=[
                        dmc.Text(
                            "Add better filtering to the Data page to allow for more detailed and specified analysis.",
                            c="dimmed",
                            size="sm",
                        ),
                    ],
                ),
            ],
        ),
    ],
    style={"padding": "20px", "margin": "auto", "maxWidth": "900px", "textAlign": "left"},
)

layout = html.Div(
    id="about-page-content",  
    children=[
        about_page_container
    ],
    style={"backgroundColor": "#f8f9fa", "minHeight": "100vh"},
)

