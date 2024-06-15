import streamlit as st
from typing import Any
import yaml

@st.cache_resource
class Translator:
    """
    TranslationManager is responsible for loading and providing translations
    based on the current language set in the Streamlit session state.

    Attributes:
        translations (dict): A dictionary containing translations for supported languages.
    """

    def __init__(self):
        """Initialize the TranslationManager and load translations.
        """
        self.translations: dict = dict()
        self._load_translations()
    
    def _load_translations(self) -> None:
        """Load translations from YAML files.
        """
        with open('./static/translations_fr.yaml', 'r', encoding='utf-8') as file:
            self.translations['FR'] = yaml.safe_load(file)
        with open('./static/translations_en.yaml', 'r', encoding='utf-8') as file:
            self.translations['EN'] = yaml.safe_load(file)

    def get_translation(self, key: str, **kwargs: Any) -> str | dict:
        """
        Get the translation for the given key based on the current language.
        
        Supports nested keys using dot notation. Allows for string formatting.

        Args:
            key (str): The key for the translation.
            **kwargs: Arguments to format the string.

        Returns:
            str | dict : The translated string or dict.
        """
        lang = st.session_state.get("lang", "FR")
        keys = key.split('.')
        translation: dict = self.translations.get(lang, {})
        for k in keys:
            translation = translation.get(k, None)
            if translation is None:
                return key 
        if isinstance(translation, str):
            return translation.format(**kwargs)
        return translation