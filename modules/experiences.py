import datetime as dt
import streamlit as st

from modules.experience import Experience

start_date = dt.date(2022, 2, 1) # PeakSys start date
today = dt.date.today()

delta = today - start_date
years = delta.days // 365
months = (delta.days % 365) // 30

peaksys = Experience(
    entreprise="Peaksys (Cdiscount)",
    poste="MLOps Engineer",
    date=f"Février 2022 - Aujourd'hui ({years} ans et {months} mois)",
    description="""
    Industrialisation des processus de déploiement des modèles de machine Learning.  
    Conception, architecture et développement de logiciel Python (librairies, modules).  
    Conception et animations de formations auprès des Data Scientists.  
    Débogage et assistance auprès des équipes DataScience.  
    Automatisation des tests fonctionnels.  
    Optimisation de code.  
    """,
    competences="Python, Docker, Kubernetes, Azure DevOps, Datascience"
)

journee_de_chasse = Experience(
    entreprise="Journée de chasse",
    poste="Project Lead Developer",
    date="Mars 2020 - Septembre 2021 (1 an et 6 mois)",
    description="""
    Création et management d'une équipe (2 devs & 1 ui/ux). Création des nouvelles
    features de la platform. Être en charge des serveurs, de l'optimization de la
    platform et tous le coté IT de l'entreprise (factures, SEO, AWS, ...). 
    """,
    competences="Angular, NodeJS, AWS, SEO, IT, Management, Python, Stripe"
)

thales = Experience(
    entreprise="Thales",
    poste="Développeur logiciel",
    date="Août 2019 - Mars 2020 (8 mois)",
    description="""
    Création d'une plateforme permettant de gérer plusieurs bancs
    d'essais directement depuis son navigateur plutôt que de devoir rester dans la
    salle des bancs.  
    Création de rapport dynamiques sur tous les matériels de Thales France.
    """,
    competences="Python, Birt, React"
)

share_your_trip = Experience(
    entreprise="ShareYourTrip",
    poste="Développeur full-stack",
    date="fevrier 2018 - mars 2019 (1 an et 1 mois)",
    description="""
    Développeur Full Stack pour shareyourtrip.fr
    """,
    competences="Symfony, Elasticsearch, AWS, Nginc, Python"
)

office_toner = Experience(
    entreprise="Office Toner",
    poste="Développeur Back End",
    date="avril 2017 - septembre 2017 (5 mois)",
    description="""
    Optimisation et refactoring du site internet OfficeToner
    """,
    competences="Python, MongoDB, MySQL, PHP"
)

technicolor = Experience(
    entreprise="Technicolor",
    poste="Développeur logiciel",
    date="juillet 2015 - janvier 2016 (6 mois)",
    description="""
    Création d'un logiciel permettant le tri automatique des rushes (vidéos produite
    lors de tournage de films) du disque dur externe des clients au serveur interne qui
    permet une optimisation du temps des monteurs et étalonneurs.
    """,
    competences="Python, Qt, MySQL"
)

experiences = [peaksys, journee_de_chasse, thales, share_your_trip, office_toner, technicolor]

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