import streamlit as st

from modules.certification import Certification
from modules.translator import Translator

translator = Translator()


def get_certifications() -> list[Certification]:
    """Set the certifications of the user

    Returns:
        list[Certification]: list of certifications
    """
    translator_certifications = translator.get_translation("home.certification.certifications")

    certifications = list()

    for cert in translator_certifications:
        certification = Certification(
            title=cert.get("title"),
            school=cert.get("school"),
            date=cert.get("date"),
            link=cert.get("link")
        )
        certifications.append(certification)

    return certifications

def display_certifications() -> None:
    """Display certifications in Streamlit columns.
    """

    st.header(translator.get_translation("home.certification.title"))
    st.text("\n")

    certifications = get_certifications()
    for certification in certifications:
        st.markdown(f"""[{certification.title}]({certification.link}) - {certification.school} - {certification.date}""")
