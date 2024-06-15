import datetime as dt
import streamlit as st

from modules.experience import Experience
from modules.translator import Translator

start_date = dt.date(2022, 2, 1) # PeakSys start date
today = dt.date.today()

delta = today - start_date
years = delta.days // 365
months = (delta.days % 365) // 30

translator = Translator()

def get_experiences() -> list[Experience]:
    """Set the experiences of the user

    Returns:
        list[Experience]: list of experiences
    """
    translator_experiences = translator.get_translation("home.professional_experience.experiences")

    experiences = list()

    for exp in translator_experiences:
        experience = Experience(
            entreprise=exp.get("company"),
            poste=exp.get("title"),
            date=exp.get("date"),
            description=exp.get("description"),
            competences=", ".join(exp.get("skills"))
        )
        experiences.append(experience)

    return experiences

def format_description(description: str) -> str:
    """Adjust the description to include HTML indentation

    Args:
        description (str): description of the experience

    Returns:
        str: formatted description
    """
    lines = description.strip().split("\n")
    formatted_lines = [f"&nbsp;"*12 + line.strip() for line in lines]
    return "<br>".join(formatted_lines)

def display_experiences() -> None:
    st.header(translator.get_translation("home.professional_experience.title"))
    st.text("\n")

    experiences = get_experiences()

    experiences[0].date = experiences[0].date.format(years=years, months=months)

    for experience in experiences:
        st.header(f"{experience.poste}")
        st.markdown(f"🏢 **{experience.entreprise}**")
        st.markdown(f"📅 {experience.date}")
        st.markdown(f"📝**{translator.get_translation('home.professional_experience.description')}**")
        st.markdown(format_description(experience.description), unsafe_allow_html=True)
        st.markdown(f"🔧 {experience.competences}")
        st.markdown("")