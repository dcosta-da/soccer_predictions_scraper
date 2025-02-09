import streamlit as st

st.set_page_config(page_title="Golden goal", page_icon="⚽")

st.title("🏠 Home")

##########
# Part 1 #
##########

st.header("What's Golden Goal ?", divider="red")

st.markdown(
"""
**Golden Goal** is a streamlit application that displays some of the predictions offered for free on Betclever website 
on different football match outcomes. 

Betclever is a serious site that offers free daily predictions on a very large number of majors and minor football 
championships.

This app was created for **personal betting strategies** and share an use case on how to optimise the data shared 
on Betclever. 

⚠️ **Disclaimer** 
- *Golden Goal is by no means a replacement site for Betclever, so feel free to visit the site daily and follow it on its social networks.*
- *Golden Goal is not an incentive to bet. We will in no way be held responsible for any potential financial losses linked to betting*. 
""")

##########
# Part 2 #
##########

st.header("What predictions are displayed ?", divider="red")

# Part 2a
st.subheader('Probability based predictions')

st.markdown("""
Golden Goal displays predictions based on the **probabilities provided by Betclever's algorithm**. We don't know exactly how 
it is developed, but we do know :
> - *An advanced football predictions algorithm that has been developed over a period of ten years 
by some of the best football betting experts and professional gamblers - it contains data from over 20 years 
of football matches all over the world.*

> - *The BetClever algorithm analyses statistics, form, and other trends to provide the best tips possible.
We consider head-to-head games, team trends and form, injuries, and more to predict not only full-time result bets 
but also over/under, both teams to score, and others.*

> - *Our experts research extensively and track all data points and predictions over time to refine our betting tip 
algorithm to make it more and more accurate over time.*
""")

st.markdown("""##### Home & Away win""")

st.text("Some text")
st.markdown("""
            - item 1
            - item 2
            """)
st.write("Some text")

st.markdown("""##### Both teams to score""")

st.markdown("""##### Over 2.5 goals""")

# Line break
st.write("")

# Part 2b
st.subheader("Expected value based predictions")

st.markdown("""
Golden Goal also displays predictions based on the **Expected Value** (EV) that we have calculated ourselves 
using Betclever data.

In the context of sports betting, the EV is a calculation that **estimates the average 
gain or loss of a bet in the long run**. It takes into account the estimated probabilities of an event 
as well as the odds offered by bookmakers to **determine whether a bet is profitable or not in the long term**.

The expected value is then calculated as follows :
""")

st.latex(r"""\text{EV = } (P_\text{win} \times (\text{Odds} - 1) \times \text{Stake}) - ((1 - P_{win}) \times \text{Stake})""")

st.markdown(r"""
$Where$
- $P_\text{win} = \text{Estimated probability of winning (e.g. 70\% = 0.70)}$
- $\text{Odds} = \text{Betting odds (decimal format)}$
- $\text{Stake} = \text{Amount wagered}$
- $(\text{Odds} - 1) \times \text{Stake} = \text{Net profit if the bet wins}$
- $(1 - P_{\text{win}}) \times \text{Stake} = \text{Total loss if the bet loses}$
        
""")

st.text("")
st.markdown("""
In the predictions page based on expected value, the estimated probabilities as well as the odds are provided 
by Betclever data. The stake is based on a flat bet of 1€.
""")



