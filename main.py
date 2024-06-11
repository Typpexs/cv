import streamlit as st

from src.constants import PYTHON_LOGO, DOCKER_LOGO, KUBE_LOGO, AZUREML_LOGO

st.set_page_config(
    page_title="Accueil",
    page_icon="🏠",
)

#TODO : Revoir le logo, par ma PP et faire un bon link dessus
st.logo('./static/python_logo.png', link="https://streamlit.io/gallery", icon_image='./static/python_logo.png')

st.title("Bienvenue sur mon CV ! 👋")

# st.sidebar.success("Select a demo above.")

st.markdown(
    """
    Je suis Martin Majo, **lead dev**, **MLOps Engineer**.

    Avec plus de 5 ans d'expérience dans le développement de logiciels, j'ai acquis des compétences en développement de logiciels, en gestion de projet et intelligence artificielle.

    **👈 Selectionner mes experiences dans le menu** pour voir mon expertise !
    """
#     ### Compétences clés :
#     - Check out [streamlit.io](https://streamlit.io)
#     - Jump into our [documentation](https://docs.streamlit.io)
#     - Ask a question in our [community
#         forums](https://discuss.streamlit.io)
#     ### See more complex demos
#     - Use a neural net to [analyze the Udacity Self-driving Car Image
#         Dataset](https://github.com/streamlit/demo-self-driving)
#     - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
# """
)

st.subheader("Compétences clés :")

st.markdown("""
    <style>
    .centered-image {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)
# st.image("")
col1.image(PYTHON_LOGO, caption="Python")
col2.image(DOCKER_LOGO, caption="Docker")
col3.image(KUBE_LOGO, caption="Kubernetes")
col4.image(AZUREML_LOGO, caption="Azure ML")

