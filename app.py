import streamlit as st
import matplotlib 
import pandas as pd


st.set_page_config(page_title='Betclever predictions', layout="wide", page_icon='🎯')

st.title('Betclever predictions')

# Home win

st.header('Home win')

home_win = pd.read_excel('betclever_predictions.xlsx', sheet_name='Home win')

st.dataframe(home_win.style.background_gradient(subset=["Home Win (%)"]))

# Btts

st.header('Both team to score')

btts = pd.read_excel('betclever_predictions.xlsx', sheet_name='Btts')

st.dataframe(btts.style.background_gradient(subset=["Btts (%)"]))

# Over

st.header('Over goals')

over = pd.read_excel('betclever_predictions.xlsx', sheet_name='Over_Under')

st.dataframe(over.style.background_gradient(subset=["Over 2.5 (%)", "Over 3.5 (%)"]))

# Away win

st.header('Away win')

away_win = pd.read_excel('betclever_predictions.xlsx', sheet_name='Away Win')

st.dataframe(away_win.style.background_gradient(subset=["Away Win (%)"]))

