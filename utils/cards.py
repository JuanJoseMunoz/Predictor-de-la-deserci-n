import streamlit as st


def prediction_card(prediction, probability):

    if prediction == 1:

        st.success("No Dropout")

    else:

        st.error("Dropout")

    st.progress(float(probability))