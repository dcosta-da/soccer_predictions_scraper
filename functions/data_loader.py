import streamlit as st
import matplotlib 
import pandas as pd

file_path = "scraper/data/betclever_predictions.xlsx"


def display_proba_dataframe(sheet_name, prob_col, title):
    st.header(title, divider="red")
    
    col1, col2 = st.columns(2)
    
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    
    championships_selection = sorted((df["Country"] + " - " + df["Championship"]).unique())
    min_proba, max_proba = df[prob_col].min(), df[prob_col].max()
    
    with col1:
        selected_championships = st.multiselect("Choose one or many championship(s)", championships_selection, placeholder="Championships available")
    
    with col2:
        selected_proba = st.slider('Choose the minimum probability', min_value=min_proba, max_value=max_proba)
    
    st.write("")
    
    if selected_championships:
        df = df[(df["Country"] + " - " + df["Championship"]).isin(selected_championships)]
    
    if selected_proba != min_proba:
        df = df[df[prob_col] >= selected_proba]
    
    st.dataframe(df.style.background_gradient(subset=[prob_col], cmap='Reds'))


def display_ev_dataframe(sheet_name, ev_filter_col, ev_value, title):
    st.header(title, divider="red")

    df = pd.read_excel(file_path, sheet_name=sheet_name)
    df_filtered = df[df[ev_filter_col] >= ev_value]

    col1, col2 = st.columns(2)

    championships_selection = sorted((df_filtered["Country"] + " - " + df_filtered["Championship"]).unique())
    min_ev, max_ev = df_filtered[ev_filter_col].min(), df_filtered[ev_filter_col].max()

    with col1:
        selected_championships = st.multiselect("Choose one or many championship(s)", championships_selection, placeholder="Championships available")

    with col2:
        selected_proba = st.slider('Choose the minimum EV', min_value=min_ev, max_value=max_ev)

    st.write("")

    if selected_championships:
        df_filtered = df_filtered[(df_filtered["Country"] + " - " + df_filtered["Championship"]).isin(selected_championships)]

    if selected_proba != min_ev:
        df_filtered = df_filtered[df_filtered[ev_filter_col] >= selected_proba]

    st.dataframe(df_filtered.style.background_gradient(subset=[ev_filter_col], cmap="Reds"))