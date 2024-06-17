import streamlit as st
st.set_page_config(page_title="TGI - Text Generation Inference", page_icon="🤗")

from modules.init_page import default_init_page
from modules.translator import Translator

translator = Translator()

def main():
    default_init_page()
    
    st.title(translator.get_translation("tgi.title"))

    st.markdown(translator.get_translation("tgi.introduction_text"))

    st.header(translator.get_translation("tgi.gestion_modeles_title"))
    st.markdown(translator.get_translation("tgi.gestion_modeles_text"))

    st.header(translator.get_translation("tgi.ai_gateway_title"))
    st.markdown(translator.get_translation("tgi.ai_gateway_text"))

    st.header(translator.get_translation("tgi.technologies_title"))
    st.markdown(translator.get_translation("tgi.technologies_text"))

    st.divider()
    st.markdown(translator.get_translation("tgi.conclusion_text"))

if __name__ == "__main__":
    main()