import streamlit as st
from datetime import date, timedelta
from functions.data_loader import display_ev_dataframe

st.set_page_config(page_title="Golden goal", page_icon="⚽", layout="wide")

st.title('📈 Expected value based predictions')

today = date.today()
tomorrow = today + timedelta(1)
st.text(f"Predictions for {today} and {tomorrow}")

# Home win
display_ev_dataframe("EV Home win", "EV home win", 0.4, "Home win")

# Both team to score
display_ev_dataframe("EV Btts", "EV btts", 0.4, "Both team to score")

# Over 2.5 goals
display_ev_dataframe("EV Over 2.5", "EV over 2.5", 0.4, "Over 2.5 goals")

# Away win
display_ev_dataframe("EV Away win", "EV away win", 0.4, "Away win")

