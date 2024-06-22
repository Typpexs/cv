import streamlit as st

from modules.translator import Translator, set_lang

translator = Translator()

def navbar() -> None:
    with st.sidebar:
        st.page_link("main.py", label=translator.get_translation("home.home"), icon="🏠")
        st.page_link("pages/formateur.py", label=translator.get_translation("formations.page_title"), icon="📚")
        st.page_link("pages/TGI.py", label=translator.get_translation("tgi.page_title"), icon="🤗")
        st.page_link("pages/jupyterhub.py", label="JupyterHub", icon="🪐")
        st.page_link("pages/mlflow.py", label="MLflow", icon="♾️")
        st.page_link("pages/argo.py", label="Argo Workflow", icon="🐙")
        st.page_link("pages/images_libs.py", label=translator.get_translation("tools.page_title"), icon="🛠️")

        st.divider()
        set_lang()

        st.markdown("**👤 Martin Majo**")
        st.markdown("**📧 : [martin.majo33@gmail.com](mailto:martin.majo33@gmail.com)**")
        st.markdown("**📞: [+33 6.85.86.74.79](tel:+33685867479)**")

        col1, col2, _, _, _ = st.columns(5)
        col1.markdown("[![Malt.fr](app/static/malt_logo_25.png)](https://www.malt.fr/profile/martinmajo1)")
        col2.markdown("[![Linkedin](app/static/linkedin_logo_25.png)](https://www.linkedin.com/in/martin-majo-967083a3/)")

        with open(translator.get_translation("home.navbar.path_cv"), "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.download_button(label=translator.get_translation("home.navbar.download"), data=PDFbyte, file_name="cv_martin_majo.pdf", mime='application/pdf')
