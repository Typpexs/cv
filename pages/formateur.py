import streamlit as st
st.set_page_config(page_title="Training Provided", page_icon="📚")

from modules.init_page import default_init_page
from modules.translator import Translator

translator = Translator()

def main():
    default_init_page()
    
    st.title(translator.get_translation("formations.title"))
    
    st.markdown(translator.get_translation("formations.introduction_text"))

    st.header(translator.get_translation("formations.sujets_title"))
    st.markdown(translator.get_translation("formations.sujets_text"))

    st.header(translator.get_translation("formations.objectifs_title"))
    st.markdown(translator.get_translation("formations.objectifs_text"))

    st.header(translator.get_translation("formations.pipeline_title"))
    st.markdown(translator.get_translation("formations.pipeline_text"))

    st.header(translator.get_translation("formations.support_title"))
    st.markdown(translator.get_translation("formations.support_text"))

    st.divider()
    st.markdown(translator.get_translation("formations.conclusion_text"))


if __name__ == "__main__":
    main()