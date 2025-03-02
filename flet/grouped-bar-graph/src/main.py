import flet as ft
import pandas as pd
import plotly.express as px
from flet.plotly_chart import PlotlyChart
from os import path

df = pd.read_csv(path.join(path.dirname(__file__), "../../../data.csv"))


def create_plot(num_trimesters):
  selected_columns = ["Produto"] + [
    f"Trimestre {i}" for i in range(1, num_trimesters + 1)
  ]
  df_filtered = df[selected_columns]

  df_melted = df_filtered.melt(
    id_vars="Produto", var_name="Trimestre", value_name="Vendas"
  )

  fig = px.bar(
    df_melted,
    x="Produto",
    y="Vendas",
    color="Trimestre",
    barmode="group",
    title="Sales by Product and Quarter",
  )
  return fig


def main(page: ft.Page):
  page.title = "Sales Data App"
  page.scroll = "auto"
  page.padding = 20
  page.margin = 20

  trimester_dropdown = ft.Dropdown(
    label="Select Number of Trimesters",
    options=[
      ft.dropdown.Option(key=str(i), text=f"{i} Trimesters") for i in range(1, 5)
    ],
    value="4",
  )

  plot_chart = PlotlyChart(create_plot(int(trimester_dropdown.value)))

  def update_plot(_):
    num_trimesters = int(trimester_dropdown.value)
    plot_chart.figure = create_plot(num_trimesters)
    plot_chart.update()

  trimester_dropdown.on_change = update_plot

  page.add(ft.Column([trimester_dropdown, plot_chart], spacing=10))


ft.app(target=main)
