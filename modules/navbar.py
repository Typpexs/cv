import streamlit as st

from modules.translator import Translator, set_lang

translator = Translator()

def navbar() -> None:
    with st.sidebar:
        set_lang()
        st.page_link("main.py", label=translator.get_translation("home.home"), icon="🏠")
        st.page_link("pages/formateur.py", label="Formations dispensées", icon="📚")
        st.page_link("pages/jupyterhub.py", label="JupyterHub", icon="🚀")

        # formation
        # Text Generation Inference (TGI Hugging Face)
        # jupyterhub
        # mlflow
        # argo workflow
        # image docker python
        # librairie python
