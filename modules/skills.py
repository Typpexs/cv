import streamlit as st
from modules.css import CUSTOM_COLUMN_4, CUSTOM_COLUMN_5
from modules.image_data import ImageData
from modules.constants import (
    ADO_LOGO, BASH_LOGO, FASTAPI_LOGO, FORMATEUR_LOGO, HELM_LOGO, JUPYTER_LOGO,
    LINUX_LOGO, MLFLOW_LOGO, PYTHON_LOGO, DOCKER_LOGO, KUBE_LOGO, AZUREML_LOGO,
    SNOWFLAKE_LOGO, STREAMLIT_LOGO
)
from modules.images import display_images_with_captions
from modules.translator import Translator

translator = Translator()

def display_primary_skills() -> None:
    """Display primary skills in Streamlit columns.
    """
    columns_1 = st.columns(4)
    image_data_1 = [
        ImageData(columns_1[0], PYTHON_LOGO, "Python", CUSTOM_COLUMN_4, {}),
        ImageData(columns_1[1], DOCKER_LOGO, "Docker", CUSTOM_COLUMN_4, {}),
        ImageData(columns_1[2], KUBE_LOGO, "Kubernetes", CUSTOM_COLUMN_4, {}),
        ImageData(columns_1[3], ADO_LOGO, "Azure DevOps", CUSTOM_COLUMN_4, {}),
    ]
    display_images_with_captions(image_data_1)

def display_additional_skills() -> None:
    """Display additional skills in Streamlit columns.
    """
    columns_2 = st.columns(5)
    image_data_2 = [
        ImageData(columns_2[0], AZUREML_LOGO, "Azure ML", CUSTOM_COLUMN_5, {"width": 50}),
        ImageData(columns_2[1], BASH_LOGO, "Bash", CUSTOM_COLUMN_5, {}),
        ImageData(columns_2[2], LINUX_LOGO, "Linux", CUSTOM_COLUMN_5, {}),
        ImageData(columns_2[3], SNOWFLAKE_LOGO, "Snowflake", CUSTOM_COLUMN_5, {"width": 50}),
        ImageData(columns_2[4], FASTAPI_LOGO, "FastAPI", CUSTOM_COLUMN_5, {}),
    ]
    display_images_with_captions(image_data_2)

    columns_3 = st.columns(5)
    image_data_3 = [
        ImageData(columns_3[0], FORMATEUR_LOGO, "Formateur", CUSTOM_COLUMN_5,  {"width": 50}),
        ImageData(columns_3[1], HELM_LOGO, "Helm", CUSTOM_COLUMN_5),
        ImageData(columns_3[2], JUPYTER_LOGO, "Jupyterhub", CUSTOM_COLUMN_5, {"width": 50}),
        ImageData(columns_3[3], STREAMLIT_LOGO, "Streamlit", CUSTOM_COLUMN_5, {"width": 50}),
        ImageData(columns_3[4], MLFLOW_LOGO, "Mlflow", CUSTOM_COLUMN_5),
    ]
    display_images_with_captions(image_data_3)

def display_skills() -> None:
    """Display skills in Streamlit columns.
    """
    
    st.header(translator.get_translation("home.skills.primary"))
    display_primary_skills()
    
    st.subheader(translator.get_translation("home.skills.other"))
    display_additional_skills()
    
    st.markdown(
        translator.get_translation("home.skills.bonus"),
        unsafe_allow_html=True
    )