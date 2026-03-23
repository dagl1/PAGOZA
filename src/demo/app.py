import dash
from dash import html

app = dash.Dash(__name__)
server = app.server  # 👈 REQUIRED for Render

app.layout = html.Div("Hello from PAGOZA!")

if __name__ == "__main__":
    app.run(debug=True)
