import streamlit as st

from modules.translator import Translator, set_lang

translator = Translator()

def navbar() -> None:
    with st.sidebar:
        set_lang()
        st.page_link("main.py", label=translator.get_translation("home.home"), icon="🏠")
        st.page_link("pages/formateur.py", label=translator.get_translation("formations.page_title"), icon="📚")
        st.page_link("pages/TGI.py", label=translator.get_translation("tgi.page_title"), icon="🤗")
        st.page_link("pages/jupyterhub.py", label="JupyterHub", icon="🪐")
        st.page_link("pages/mlflow.py", label="MLflow", icon="♾️")
        st.page_link("pages/argo.py", label="Argo Workflow", icon="🐙")
        st.page_link("pages/images_libs.py", label=translator.get_translation("tools.page_title"), icon="🛠️")


        # Text Generation Inference (TGI Hugging Face) / ALMOST DONE -> 1 TODO
        # argo workflow / ALMOST DONE -> 1 TODO
    
    # TODO : Rajouter ma PP, mes infos, mes liens, pouvoir DL mon CV