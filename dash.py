import streamlit as st      # BIBLIOTECA CONSTRUIR OS DASHBOARD
import pandas as pd         # BIBLIOTECA MANIPULAÇÃO DE DADOS
import plotly.express as px # BIBLIOTECA CONSTRUIR OS GRAFICOS

st.set_page_config(layout="wide")

df = pd.read_csv("supermarket_sales.csv", sep=";", decimal=",")
df
