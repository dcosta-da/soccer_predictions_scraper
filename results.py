import streamlit as st

st.set_page_config(page_title="Golden goal", page_icon="⚽", layout="wide")

st.title("🫰 Profit/loss")

st.header("Strategy betting", divider="red")

st.markdown("""
In my betting strategy, I obviously **don't foolishly play all the bets displayed**, despite the filters already applied. 

The choice of bets therefore depends on two main factors :
- **Existing knowledge** of the championship concerned 
- Really **high probability or Expected Value** when the championship seems more exotic.

Other informations about the strategy :
- In general, I **prefer to bet on the Over market or the Both team to score market**. Quite simply because the probabilities 
of winning are basically higher.          
- The **amount bet is always 1€**. 

The platform I bet on is Edge, offered by broker [Madmarket](https://madmarket.io). It provides access to the best odds on the market, with a choice
of several bookmakers.
            
*NB : It is possible that sometimes the bookmaker does not accept the amount bet of 1€ but a lower amount. This is why the number of 
bets in the results below is not strictly equal to the total turnover.* 
""")

st.header("Monthly results", divider="red")

st.markdown("*Last update : 2024-02-18*")

st.image("images/profit-loss.png")