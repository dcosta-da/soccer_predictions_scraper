import streamlit as st
from datetime import date, timedelta
from functions.data_loader import display_proba_dataframe

st.set_page_config(page_title="Golden goal", page_icon="⚽", layout="wide")

st.title("📊 Probability based predictions")

today = date.today()
tomorrow = today + timedelta(1)
st.text(f"Predictions for {today} and {tomorrow}")

# Home win
display_proba_dataframe("Home win", "Home Win (%)", "Home win")

# Both team to score
display_proba_dataframe("Btts", "Btts (%)", "Both team to score")

# Over goals
display_proba_dataframe("Over_Under", "Over 2.5 (%)", "Over 2.5 goals")

# Away win
display_proba_dataframe("Away win", "Away Win (%)", "Away win")
