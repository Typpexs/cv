from dataclasses import dataclass
import streamlit as st

@dataclass
class Experience:
    entreprise: str
    poste: str
    date: str
    description: str
    competences: str
