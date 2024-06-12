from src.experience import Experience
import datetime as dt

start_date = dt.date(2022, 2, 1) # PeakSys start date
today = dt.date.today()

delta = today - start_date
years = delta.days // 365
months = (delta.days % 365) // 30

peaksys = Experience(
    entreprise="PeakSys (Cdiscount)",
    poste="MLOps Engineer",
    date=f"février 2022 - Aujourd'hui ({years} ans et {months} mois)",
    description="""
    Industrialisation des processus de déploiement des modèles de machine Learning.  
    Conception, architecture et développement de logiciel Python (librairies, modules).  
    Conception et animations de formations auprès des Data Scientists.  
    Débogage et assistance auprès des équipes DataScience.  
    Automatisation des tests fonctionnels.  
    Optimisation de code.  
    """,
    competences="Python, Docker, Kubernetes, Azure DevOps"
)

experiences = [peaksys]
