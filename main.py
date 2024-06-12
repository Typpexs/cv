import streamlit as st

from src.constants import (
    ADO_LOGO, BASH_LOGO, FASTAPI_LOGO, FORMATEUR_LOGO, HELM_LOGO, JUPYTER_LOGO,
    LINUX_LOGO, MLFLOW_LOGO, PYTHON_LOGO, DOCKER_LOGO, KUBE_LOGO, AZUREML_LOGO,
    SNOWFLAKE_LOGO, STREAMLIT_LOGO
)
from src.css import CUSTOM_COLUMN_4, CUSTOM_COLUMN_5, HIDE_IMG_FS
from src.image_data import ImageData
from src.experiences import experiences
from src.certifications import certifications

st.set_page_config(
    page_title="Accueil",
    page_icon="🏠",
)

#TODO : Revoir le logo, par ma PP et faire un bon link dessus
st.logo('./static/python_logo.png', link="https://streamlit.io/gallery", icon_image='./static/python_logo.png')

st.title("Bienvenue sur mon CV ! 👋")

st.markdown(
    """
    Je suis Martin Majo, **lead dev**, **MLOps Engineer**.

    Avec bientot 6 ans d'expérience professionelles dans le développement de logiciels, j'ai acquis des compétences en développement de logiciels, en gestion de projet et intelligence artificielle.

    **👈 Selectionner mes experiences dans le menu** pour voir mon expertise !
    """
)
st.divider()

def display_images_with_captions(image_data: list[ImageData]) -> None:
    """Display images with captions in Streamlit columns.

    Args:
        images_data (list[ImageData]): List of ImageData instances containing image and its properties.
    """
    for data in image_data:
        data.column.image(data.image, caption=data.caption, **(data.kwargs or {}))
        data.column.markdown(data.custom_column, unsafe_allow_html=True)

st.header("Compétences clés :")

columns_1 = st.columns(4)
image_data_1 = [
    ImageData(columns_1[0], PYTHON_LOGO, "Python", CUSTOM_COLUMN_4, {}),
    ImageData(columns_1[1], DOCKER_LOGO, "Docker", CUSTOM_COLUMN_4, {}),
    ImageData(columns_1[2], KUBE_LOGO, "Kubernetes", CUSTOM_COLUMN_4, {}),
    ImageData(columns_1[3], ADO_LOGO, "Azure DevOps", CUSTOM_COLUMN_4, {}),
]
display_images_with_captions(image_data_1)


st.subheader("Autres compétences :")

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


st.markdown(
    """
    <p style='font-size:12px'>
    Cette liste n'est pas exhaustive et ne reflète que les domaines où j'ai le plus d'affinités et d'expertise.
    </p>
    """,
    unsafe_allow_html=True
)


# Adjust the description to include HTML indentation
def format_description(description: str) -> str:
    lines = description.strip().split("\n")
    formatted_lines = [f"&nbsp;"*12 + line.strip() for line in lines]
    return "<br>".join(formatted_lines)

st.divider()
st.header("Expériences :")
st.text("\n")

for experience in experiences:
    st.header(f"{experience.poste}")
    st.markdown(f"🏢 **{experience.entreprise}**")
    st.markdown(f"📅 {experience.date}")
    st.markdown("📝**Description :**")
    st.markdown(format_description(experience.description), unsafe_allow_html=True)
    st.markdown(f"🔧 {experience.competences}")
    st.markdown("")

st.divider()
st.header("Formation :")
st.text("\n")

st.subheader("Master en informatique")
st.markdown(
    """
    🏢 [Epitech](https://www.epitech.eu/) - Bordeaux, France  
    📅 2019
    """
)

st.divider()
st.header("Certifications :")
st.text("\n")

for certification in certifications:
    st.markdown(f"""[{certification.titre}]({certification.link}) - {certification.ecole} - {certification.date}""")

st.markdown(HIDE_IMG_FS, unsafe_allow_html=True)
