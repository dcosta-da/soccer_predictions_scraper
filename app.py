import streamlit as st

home_page = st.Page("home.py", title="Home", icon="🏠")
predictions_page = st.Page("predictions.py", title="Predictions", icon="🎯")

pg = st.navigation([home_page, predictions_page])
st.set_page_config(page_title="Golden goal", page_icon="⚽", layout="wide")
pg.run()


