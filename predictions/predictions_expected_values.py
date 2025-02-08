import streamlit as st
from datetime import date, timedelta
from functions.data_loader import display_ev_dataframe

st.title('Expected value based predictions')

today = date.today()
tomorrow = today + timedelta(1)
st.text(f"Predictions for {today} and {tomorrow}")

# Home win
display_ev_dataframe('EV Home win', "Home Win (%)", 50, 'EV home win', 0.4, "Home win")

# Both team to score
display_ev_dataframe('EV Btts', "Btts (%)", 70, 'EV btts', 0.4, "Both team to score")

# Over 2.5 goals
display_ev_dataframe('EV Over 2.5', "Over 2.5 (%)", 70, 'EV over 2.5', 0.4, "Over 2.5 goals")

# Away win
display_ev_dataframe('EV Away win', "Away Win (%)", 50, 'EV away win', 0.4, "Away win")

