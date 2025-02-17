import streamlit as st

home_page = st.Page("home/home.py", title="Golden Goal", icon=":material/home:")

predictions_probabilities_page = st.Page("predictions/predictions_probabilities.py", title="Probabilities", icon=":material/bar_chart:")

predictions_ev_page = st.Page("predictions/predictions_expected_values.py", title="Expected values", icon=":material/trending_up:")

results_page = st.Page("results.py", title="Profit/loss", icon=":material/euro:")

pg = st.navigation(
    {
        "Home": [home_page],
        "Predictions": [predictions_probabilities_page, predictions_ev_page],
        "Results": [results_page]
    }
)

pg.run()