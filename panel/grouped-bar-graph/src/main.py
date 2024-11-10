import pandas as pd
import plotly.express as px
import panel as pn
from os import path

pn.extension("plotly")

df = pd.read_csv(path.join(path.dirname(__file__), "../../../data.csv"))


class SalesDataDashboard:
  def __init__(self):
    self.df = df

    self.num_trimesters_select = pn.widgets.Select(
      name="Number of Trimesters",
      options={
        "1 trimester": 1,
        "2 trimesters": 2,
        "3 trimesters": 3,
        "4 trimesters": 4,
      },
      value=4,
    )

    self.plot_pane = pn.pane.Plotly(
      self.create_plot(self.num_trimesters_select.value), sizing_mode="stretch_width"
    )

    self.num_trimesters_select.param.watch(self.update_plot, "value")

    self.dashboard = pn.Column(
      "# Sales Data", self.num_trimesters_select, self.plot_pane
    )

  def create_plot(self, num_trimesters):
    selected_columns = ["Produto"] + [
      f"Trimestre {i}" for i in range(1, num_trimesters + 1)
    ]
    df_filtered = self.df[selected_columns]

    df_melted = df_filtered.melt(
      id_vars="Produto", var_name="Trimestre", value_name="Valor"
    )

    fig = px.bar(
      df_melted,
      x="Produto",
      y="Valor",
      color="Trimestre",
      barmode="group",
      title="Sales by Product and Quarter",
    )
    return fig

  def update_plot(self, event):
    self.plot_pane.object = self.create_plot(event.new)

  def show(self):
    return self.dashboard


dashboard = SalesDataDashboard()

dashboard.show().servable()
