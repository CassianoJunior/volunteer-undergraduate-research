from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from os import path

df = pd.read_csv(path.join(path.dirname(__file__), "../../../data.csv"))

app = Dash()

fig = go.Figure()

for trimester in df.columns[1:]:
  fig.add_trace(go.Bar(x=df["Produto"], y=df[trimester], name=trimester))

app.layout = [
  html.H1(children="Grouped Bar Graph", style={"textAlign": "center"}),
  html.Div(
    [
      html.H2("Grouped Bar Graph of Sales Data"),
      dcc.Dropdown(
        id="trimester-dropdown",
        options=[
          {"label": "1 Trimester", "value": 1},
          {"label": "2 Trimesters", "value": 2},
          {"label": "3 Trimesters", "value": 3},
          {"label": "4 Trimesters", "value": 4},
        ],
        value=4,
        clearable=False,
      ),
      dcc.Graph(id="bar-graph"),
    ]
  ),
]


@callback(Output("bar-graph", "figure"), Input("trimester-dropdown", "value"))
def update_graph(selected_trimester_count):
  fig = go.Figure()

  for trimester in df.columns[1 : selected_trimester_count + 1]:
    fig.add_trace(go.Bar(x=df["Produto"], y=df[trimester], name=trimester))

  fig.update_layout(
    title="Sales Data by Product and Trimester",
    xaxis_title="Produto",
    yaxis_title="Sales",
    barmode="group",
  )

  return fig


if __name__ == "__main__":
  app.run(debug=True)
