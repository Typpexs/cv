import streamlit as st

from modules.css import HIDE_IMG_FS, HIDE_STREAMLIT_STYLE
from modules.navbar import navbar

def default_init_page() -> None:
    """load the default init page.
    """
    navbar()

    st.logo('./static/pp.jpg', icon_image='./static/pp.jpg', link="https://www.malt.fr/profile/martinmajo1")

    st.markdown(HIDE_IMG_FS, unsafe_allow_html=True)
    st.markdown(HIDE_STREAMLIT_STYLE, unsafe_allow_html=True)


