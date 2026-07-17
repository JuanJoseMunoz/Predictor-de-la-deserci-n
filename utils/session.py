import streamlit as st


def initialize():

    defaults = {

        "prediction": None,
        "probability": None,
        "selected_model": "Original"

    }

    for key, value in defaults.items():

        if key not in st.session_state:

            st.session_state[key] = value