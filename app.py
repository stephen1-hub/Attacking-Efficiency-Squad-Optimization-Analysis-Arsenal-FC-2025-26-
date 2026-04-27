import streamlit as st
import pandas as pd
from src.metrics import add_metrics

df = pd.read_csv("data/arsenal_players_2025_26.csv")
df = add_metrics(df)

st.title("Arsenal 2025/26 Performance Dashboard")

st.subheader("Top Threat Players")
st.dataframe(df.sort_values("threat_score", ascending=False).head(10))

st.subheader("Best Finishers")
st.dataframe(df.sort_values("finishing_efficiency", ascending=False).head(10))

st.subheader("Best Creators")
st.dataframe(df.sort_values("creativity_efficiency", ascending=False).head(10))
