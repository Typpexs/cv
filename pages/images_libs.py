import streamlit as st
st.set_page_config(page_title="Images & Libs Python", page_icon="🛠️")

from modules.init_page import default_init_page
from modules.translator import Translator

translator = Translator()

def main():
    default_init_page()

    st.title(translator.get_translation("tools.title"))

    st.header(translator.get_translation("tools.docker_header"))
    st.markdown(translator.get_translation("tools.docker_text"))

    st.header(translator.get_translation("tools.libraries_header"))
    st.markdown(translator.get_translation("tools.libraries_text"))

    st.divider()
    st.markdown(translator.get_translation("tools.conclusion_text"))

if __name__ == "__main__":
    main()