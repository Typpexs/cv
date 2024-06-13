import streamlit as st

def navbar() -> None:
    with st.sidebar:
        st.page_link("main.py", label="Accueil", icon="🏠")
        st.page_link("pages/jupyterhub.py", label="JupyterHub", icon="🚀")