from pathlib import Path

import dash
from dash import html

ROOT_DIR = Path(__file__).resolve().parents[2]
ASSETS_DIR = ROOT_DIR / "assets"


app = dash.Dash(__name__, assets_folder=str(ASSETS_DIR))
server = app.server  # 👈 REQUIRED for Render


# add swiss_roll.png to show in div
layout = html.Div(
    [
        # title
        html.H1("PAGOZA - A Python Library for Topological Data Analysis"),
        html.Img(
            src=app.get_asset_url("swiss_roll.png"), style={"width": "50%", "height": "auto"}
        ),
    ]
)
app.layout = layout

if __name__ == "__main__":
    app.run(debug=True)
