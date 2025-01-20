import streamlit as st
import pandas as pd
import plotly.express as px
from os import path

df = pd.read_csv(path.join(path.dirname(__file__), "../../../data.csv"))

num_trimesters = st.selectbox(
  "Selecione o número de trimestres",
  options=["1 trimestre", "2 trimestres", "3 trimestres", "4 trimestres"],
  index=3,
)
num_trimesters = int(num_trimesters.split()[0])

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

st.title("Sales Data")
st.plotly_chart(fig)
