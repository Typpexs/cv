import streamlit as st

st.set_page_config(
    page_title="Accueil",
    page_icon="🏠",
)

from modules.init_page import default_init_page
from modules.educations import display_educations
from modules.experiences import display_experiences
from modules.certifications import display_certifications
from modules.skills import display_skills
from modules.translator import Translator

translator = Translator()


def display_CV_intro() -> None:
    st.title(translator.get_translation("home.welcome"))
    st.markdown(translator.get_translation("home.about"))


def main():
    default_init_page()
    
    display_CV_intro()
    st.divider()
    
    display_skills()
    st.divider()
    
    display_experiences()
    st.divider()

    display_educations()
    st.divider()

    display_certifications()

if __name__ == "__main__":
    main()