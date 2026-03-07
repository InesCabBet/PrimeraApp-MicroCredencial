import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("bike_dataset_hour.csv")

st.markdown("## Datos Crudos del dataset")
st.dataframe(df.head(500))

st.markdown("## Datos sobre el dataset")
st.dataframe(df.describe().T)

st.markdown("## Estadísticos Básicos")
st.dataframe(df[['dteday', 'temp', 'windspeed', 'hum','cnt']].describe().T[['count', 'std', 'mean']])

st.markdown("## Distribución de las variables")

st.markdown("## Matriz de correlación")

