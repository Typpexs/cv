import streamlit as st

from modules.translator import Translator

translator = Translator()


def display_educations() -> None:
    """Display formations in Streamlit columns.
    """

    st.header(translator.get_translation("home.education.title"))
    st.text("\n")

    for education in translator.get_translation("home.education.educations"):
        st.subheader(education.get("degree"))
        st.markdown(
            f"""
            🏢 [{education.get("school")}]({education.get("link")}) - {education.get("location")}  
            🎓 {education.get("graduated_on")}
            """
        )
        st.text("\n")
