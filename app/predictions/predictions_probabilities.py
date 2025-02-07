import streamlit as st
import matplotlib 
import pandas as pd
from datetime import date, timedelta
import os

st.title('Probability based predictions')

today = date.today()
tomorrow = today + timedelta(1)
st.text(f"Predictions for {today} and {tomorrow}")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
file_path = os.path.join(BASE_DIR, "scraper/data/betclever_predictions.xlsx")


# Home win

st.header('Home win', divider="red")

home_win = pd.read_excel(file_path, sheet_name='Home win')

st.dataframe(home_win.style.background_gradient(subset=["Home Win (%)"], cmap='Reds'))


# Btts

st.header('Both team to score', divider="red")

btts = pd.read_excel(file_path, sheet_name='Btts')

st.dataframe(btts.style.background_gradient(subset=["Btts (%)"], cmap='Reds'))


# Over

st.header('Over goals', divider="red")

over = pd.read_excel(file_path, sheet_name='Over_Under')

st.dataframe(over.style.background_gradient(subset=["Over 2.5 (%)", "Over 3.5 (%)"], cmap='Reds'))


# Away win

st.header('Away win', divider="red")

away_win = pd.read_excel(file_path, sheet_name='Away win')

st.dataframe(away_win.style.background_gradient(subset=["Away Win (%)"], cmap='Reds'))

