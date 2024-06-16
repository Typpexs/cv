import streamlit as st
st.set_page_config(page_title="JupyterHub", page_icon="🪐")

from modules.init_page import default_init_page
from modules.translator import Translator

translator = Translator()

def main():
    default_init_page()
    
    st.title(translator.get_translation("jupyterhub.title"))
    
    st.markdown(translator.get_translation("jupyterhub.introduction_text"))

    st.header(translator.get_translation("jupyterhub.mise_en_place_title"))
    st.markdown(translator.get_translation("jupyterhub.mise_en_place_text"))

    st.header(translator.get_translation("jupyterhub.creation_images_title"))
    st.markdown(translator.get_translation("jupyterhub.creation_images_text"))

    st.header(translator.get_translation("jupyterhub.gestion_stockage_title"))
    st.markdown(translator.get_translation("jupyterhub.gestion_stockage_text"))

    st.header(translator.get_translation("jupyterhub.maintenance_title"))
    st.markdown(translator.get_translation("jupyterhub.maintenance_text"))

    st.divider()
    st.markdown(translator.get_translation("jupyterhub.conclusion_text"))


if __name__ == "__main__":
    main()

# TODO: Peut etre regarder ça pour plus tard
# st.sidebar.header("Plotting Demo")
