import streamlit as st

pg_intro = st.Page("intro.py", title="Introducción")

# Paginas EDA
pg_eda_intro = st.Page("seccion_eda/intro_eda.py", title="Primeros Pasos")


navigation_env = st.navigation(
    {
        "": [pg_intro],
        "EDA": [pg_eda_intro]

    }
)

navigation_env.run()
