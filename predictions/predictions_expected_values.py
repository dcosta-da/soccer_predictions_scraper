import streamlit as st
import matplotlib 
import pandas as pd
from datetime import date, timedelta

st.title('Expected value based predictions')

today = date.today()
tomorrow = today + timedelta(1)
st.text(f"Predictions for {today} and {tomorrow}")

file_path = "scraper/data/betclever_predictions.xlsx"


# Home win

st.header('Home win', divider="red")

home_win_ev = pd.read_excel(file_path, sheet_name='EV Home win')
home_win_ev_filtered = home_win_ev[(home_win_ev['Home Win (%)'] >= 50) & (home_win_ev['EV home win'] >= 0.4)]

st.dataframe(home_win_ev_filtered.style.background_gradient(subset=["EV home win"], cmap="Reds"))


# Btts

st.header('Both team to score', divider="red")

btts_ev = pd.read_excel(file_path, sheet_name='EV Btts')
btts_ev_filtered = btts_ev[(btts_ev['Btts (%)'] >= 70) & (btts_ev['EV btts'] >= 0.4)]

st.dataframe(btts_ev_filtered.style.background_gradient(subset=["EV btts"], cmap="Reds"))


# Over

st.header('Over goals', divider="red")

over_ev = pd.read_excel(file_path, sheet_name='EV Over 2.5')
over_ev_filtered = over_ev[(over_ev['Over 2.5 (%)'] >= 70) & (over_ev['EV over 2.5'] >= 0.4)]

st.dataframe(over_ev_filtered.style.background_gradient(subset=["EV over 2.5"], cmap="Reds"))


# Away win

st.header('Away win', divider="red")

away_win_ev = pd.read_excel(file_path, sheet_name='EV Away win')
away_win_ev_filtered = away_win_ev[(away_win_ev['Away Win (%)'] >= 50) & (away_win_ev['EV away win'] >= 0.4)]

st.dataframe(away_win_ev_filtered.style.background_gradient(subset=["EV away win"], cmap="Reds"))

