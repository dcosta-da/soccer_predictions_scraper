import streamlit as st
import matplotlib 
import pandas as pd
from datetime import date, timedelta

#st.set_page_config(page_title='Predictions', layout="wide", page_icon='🎯')

st.title('Predictions')

today = date.today()
tomorrow = today + timedelta(1)
st.text(f"Predictions for {today} and {tomorrow}")

# Home win

st.header('Home win', divider="blue")

home_win = pd.read_excel('scraper/data/betclever_predictions.xlsx', sheet_name='Home win')

st.dataframe(home_win.style.background_gradient(subset=["Home Win (%)"]))

# Btts

st.header('Both team to score', divider="blue")

btts = pd.read_excel('scraper/data/betclever_predictions.xlsx', sheet_name='Btts')

st.dataframe(btts.style.background_gradient(subset=["Btts (%)"]))

# Over

st.header('Over goals', divider="blue")

over = pd.read_excel('scraper/data/betclever_predictions.xlsx', sheet_name='Over_Under')

st.dataframe(over.style.background_gradient(subset=["Over 2.5 (%)", "Over 3.5 (%)"]))

# Away win

st.header('Away win', divider="blue")

away_win = pd.read_excel('scraper/data/betclever_predictions.xlsx', sheet_name='Away Win')

st.dataframe(away_win.style.background_gradient(subset=["Away Win (%)"]))

