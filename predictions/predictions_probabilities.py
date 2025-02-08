import streamlit as st
import matplotlib 
import pandas as pd
from datetime import date, timedelta

st.title('Probability based predictions')

today = date.today()
tomorrow = today + timedelta(1)
st.text(f"Predictions for {today} and {tomorrow}")

file_path = "scraper/data/betclever_predictions.xlsx"

############
# Home win #
############

st.header('Home win', divider="red")

col1, col2 = st.columns(2)

home_win = pd.read_excel(file_path, sheet_name="Home win")
championships_selection = sorted((home_win["Country"] + " - " + home_win["Championship"]).unique())
min_proba, max_proba = home_win["Home Win (%)"].min(),home_win["Home Win (%)"].max(),

with col1:
    selected_championship = st.multiselect("Choose one or many championship(s)", championships_selection)

with col2:
    selected_proba = st.slider('Choose minimum probability', min_value=min_proba, max_value=max_proba)

st.write("")

if selected_championship:  
    home_win = home_win[(home_win["Country"] + " - " + home_win["Championship"]).isin(selected_championship)]

if selected_proba != min_proba :  
    home_win = home_win[home_win["Home Win (%)"] >= selected_proba]

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

