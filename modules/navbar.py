import streamlit as st

from modules.translator import Translator

translator = Translator()

def change_lang() -> None:
    st.session_state["EN"] = not st.session_state["EN"]
    st.session_state["lang"] = "EN" if st.session_state["EN"] else "FR"

def set_lang() -> None:
    if "EN" not in st.session_state:
        st.session_state["EN"] = False
        st.session_state["lang"] = "FR"

    #TODO: Change le label du toggle pour mettre un drapeau
    st.toggle(label="EN", value=st.session_state["EN"], on_change=change_lang)

def navbar() -> None:
    with st.sidebar:
        set_lang()
        st.page_link("main.py", label=translator.get_translation("home.home"), icon="🏠")
        st.page_link("pages/jupyterhub.py", label="JupyterHub", icon="🚀")