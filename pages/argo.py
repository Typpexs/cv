import streamlit as st
st.set_page_config(page_title="Argo Worflow", page_icon="🐙")

from modules.init_page import default_init_page
from modules.translator import Translator

translator = Translator()

def main():
    default_init_page()
    
    st.title(translator.get_translation("argo.title"))

    st.markdown(translator.get_translation("argo.introduction_text"))

    #TODO : CHECK SI C'EST BIEN CA
    st.header(translator.get_translation("argo.pipeline_title"))
    st.markdown(translator.get_translation("argo.pipeline_text"))

    st.header(translator.get_translation("argo.orchestration_title"))
    st.markdown(translator.get_translation("argo.orchestration_text"))

    st.divider()
    st.markdown(translator.get_translation("argo.conclusion_text"))


if __name__ == "__main__":
    main()