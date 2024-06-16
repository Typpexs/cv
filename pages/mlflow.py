import streamlit as st
st.set_page_config(page_title="MLflow", page_icon="♾️")

from modules.init_page import default_init_page
from modules.translator import Translator

translator = Translator()

def main():
    default_init_page()
    
    st.title(translator.get_translation("mlflow.title"))

    st.markdown(translator.get_translation("mlflow.introduction_text"))

    st.header(translator.get_translation("mlflow.deployment_title"))
    st.markdown(translator.get_translation("mlflow.deployment_text"))

    st.header(translator.get_translation("mlflow.library_title"))
    st.markdown(translator.get_translation("mlflow.library_text"))

    st.divider()
    st.markdown(translator.get_translation("mlflow.conclusion_text"))


if __name__ == "__main__":
    main()
