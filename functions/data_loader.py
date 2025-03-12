import streamlit as st
import matplotlib 
import pandas as pd
from datetime import datetime, date

file_path = "scraper/data/betclever_predictions.xlsx"


def display_proba_dataframe(sheet_name, prob_col, title):
    st.header(title, divider="red")
    
    col1, col2, col3 = st.columns(3)
    
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    
    #df['Date'] = pd.to_datetime(df['Date']) 
    df['Date'] = pd.to_datetime(df['Date'], format="%d-%m-%Y %H:%M", errors="coerce")

    min_date, max_date = df['Date'].min().date(), df['Date'].max().date()
    championships_selection = sorted((df["Country"] + " - " + df["Championship"]).unique())
    min_proba, max_proba = df[prob_col].min(), df[prob_col].max()

    if min_proba == max_proba:
        max_proba += 1
    
    with col1:
        selected_date = st.date_input("Choose a date", value=min_date, format="YYYY-MM-DD", min_value=min_date, max_value=max_date, key=f"date_input_{sheet_name}")
    
    with col2:
        selected_championships = st.multiselect("Choose one or many championship(s)", championships_selection, placeholder="Championships available", key=f"select_champ_{sheet_name}")

    with col3:
        selected_proba = st.slider("Choose the minimum probability", min_value=min_proba, max_value=max_proba, key=f"slider_proba_{sheet_name}")
    
    st.write("")

    if selected_date:
        df = df[df['Date'].dt.date == selected_date]  

    if selected_championships:
        df = df[(df["Country"] + " - " + df["Championship"]).isin(selected_championships)]
    
    if selected_proba != min_proba:
        df = df[df[prob_col] >= selected_proba]

    st.dataframe(df.style.background_gradient(subset=[prob_col], cmap='Reds'))


def display_ev_dataframe(sheet_name, ev_filter_col, ev_value, title):
    st.header(title, divider="red")

    df = pd.read_excel(file_path, sheet_name=sheet_name)
    #df['Date'] = pd.to_datetime(df['Date'])
    df['Date'] = pd.to_datetime(df['Date'], format="%d-%m-%Y %H:%M", errors="coerce")

    df_filtered = df[df[ev_filter_col] >= ev_value]

    col1, col2, col3 = st.columns(3)

    min_date, max_date = df['Date'].min().date(), df['Date'].max().date()
    championships_selection = sorted((df_filtered["Country"] + " - " + df_filtered["Championship"]).unique())
    min_ev, max_ev = df_filtered[ev_filter_col].min(), df_filtered[ev_filter_col].max()

    if min_ev == max_ev:
        max_ev += 0.1

    with col1:
        selected_date = st.date_input("Choose a date", value=min_date, format="YYYY-MM-DD", min_value=min_date, max_value=max_date, key=f"date_input_{sheet_name}")
    
    with col2:
        selected_championships = st.multiselect("Choose one or many championship(s)", championships_selection, placeholder="Championships available", key=f"select_champ_{sheet_name}")

    with col3:
        selected_proba = st.slider('Choose the minimum EV', min_value=min_ev, max_value=max_ev, key=f"slider_proba_{sheet_name}")

    st.write("")

    if selected_date:
        df_filtered = df_filtered[df_filtered['Date'].dt.date == selected_date]  

    if selected_championships:
        df_filtered = df_filtered[(df_filtered["Country"] + " - " + df_filtered["Championship"]).isin(selected_championships)]

    if selected_proba != min_ev:
        df_filtered = df_filtered[df_filtered[ev_filter_col] >= selected_proba]

    st.dataframe(df_filtered.style.background_gradient(subset=[ev_filter_col], cmap="Reds"))