import streamlit as st
from modules.navbar import navbar

st.set_page_config(page_title="Plotting Demo", page_icon="📈")

navbar()

st.markdown("# Plotting Demo")
st.sidebar.header("Plotting Demo")
st.write(
    """This demo illustrates a combination of plotting and animation with
Streamlit. We're generating a bunch of random numbers in a loop for around
5 seconds. Enjoy!"""
)