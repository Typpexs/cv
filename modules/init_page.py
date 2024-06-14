import streamlit as st

from modules.css import HIDE_IMG_FS
from modules.navbar import navbar

def default_init_page() -> None:
    """load the default init page.
    """
    navbar()

    #TODO : Revoir le logo, par ma PP et faire un bon link dessus
    st.logo('./static/python_logo.png', icon_image='./static/python_logo.png')

    st.markdown(HIDE_IMG_FS, unsafe_allow_html=True)

