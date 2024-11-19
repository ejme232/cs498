from dash import html, register_page
from dash_mantine_components import Container, Text, Timeline, TimelineItem, Divider

register_page(__name__)

about_page_container = Container(
    id="about-page-container",
    children=[
        Text("About", style={"fontSize": "32px", "fontWeight": "bold", "marginBottom": "10px", "color": "#2c3e50", "textAlign": "left"}),
        Divider(style={"marginBottom": "20px"}),

        Text("Purpose", id="purpose-heading", style={"fontSize": "24px", "fontWeight": "bold", "marginBottom": "15px", "color": "#2c3e50", "maxWidth": "800px"}),
        Text("The goal of this project is to bring together data on mental health and substance abuse in order to bring awareness and information to the public.", style={"fontSize": "16px", "lineHeight": "1.5", "marginBottom": "30px", "maxWidth": "800px", "color": "#34495e"}),  
                    
        Text("What's Next", id="whats-next-heading", style={"fontSize": "24px", "fontWeight": "bold", "marginBottom": "15px", "color": "#2c3e50", "maxWidth": "800px"}),
        # create a coming soon section stylized as a timeline of sorts
        Timeline(
            id = "timeline",
            active = 0,
            bulletSize = 20,
            lineWidth = 5,
            style={"maxWidth": "800px", "marginTop": "10px"},
            children = [
                TimelineItem(
                    id = "timeline-item-1",
                    title="Task 1",
                    children=[
                        Text(
                            "description of task 1",
                            c="dimmed",
                            size="sm",
                        ),
                    ],
                ),
                TimelineItem(
                    id = "timeline-item-2",
                    title="Task 2",
                    children=[
                        Text(
                            "description of task 2",
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

