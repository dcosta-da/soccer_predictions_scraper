import streamlit as st

st.title("Home")

# Part 1
st.header("What's Golden Goal ?", divider="blue")

# st.markdown(
# """
# Golden Goal is a streamlit application that displays some of the predictions offered on [Betclever](betclever.com) website 
# on different football match outcomes. 

# It was created for personal betting strategies and share an use case on how to optimise 
# the data shared on Betclever. 

# Betclever is a serious site that offers free daily predictions on a very large number of football championships. 

# This streamlit app is in no way a replacement site, so do not hesitate to visit the site daily and follow it on [Facebook](https://www.facebook.com/BCbetclever), 
# [Instagram](https://www.instagram.com/betclever_/), [X](https://x.com/betclever_) and [Telegram](https://t.me/+VrHDodda6ssyOGZk).

# ⚠️ **Disclaimer**
# - This is not an incentive to bet : this streamlit application will in no way be held responsible for any potential financial losses linked to betting. 
# """)

# Part 2
st.header("What predictions are displayed ?", divider="blue")

st.subheader('Probability based predictions')

st.markdown("""##### Home & Away win""")

st.text("Some text")
st.markdown("""
            - item 1
            - item 2
            """)
st.write("Some text")

st.markdown("""##### Both teams to score""")

st.markdown("""##### Over goals""")

st.write("")

st.subheader("Expected value based predictions")

st.latex(r"""EV = (P_\text{win} \times (\text{Odds} - 1) \times \text{Stake}) - ((1 - P_{win}) \times \text{Stake})""")

st.markdown(r"""
$Where$
- $P_\text{win} = \text{Estimated probability of winning (e.g. 70\% = 0.70)}$
- $\text{Odds} = \text{Betting odds (decimal format)}$
- $\text{Stake} = \text{Amount wagered}$
- $(\text{Odds} - 1) \times \text{Stake} = \text{Net profit if the bet wins}$
- $(1 - P_{\text{win}}) \times \text{Stake} = \text{Total loss if the bet loses}$
        
""")



