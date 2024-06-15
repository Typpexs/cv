import streamlit as st
st.set_page_config(page_title="Plotting Demo", page_icon="📈")

from modules.init_page import default_init_page
from modules.translator import Translator

translator = Translator()

def main():
    default_init_page()

    #TODO  Faire cette page
    
    st.markdown("# Plotting Demo")
    st.sidebar.header("Plotting Demo")
    st.write(
        """This demo illustrates a combination of plotting and animation with
    Streamlit. We're generating a bunch of random numbers in a loop for around
    5 seconds. Enjoy!"""
    )


if __name__ == "__main__":
    main()