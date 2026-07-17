import streamlit as st


def page_title(title):

    st.title(title)

    st.divider()


def metric_card(title, value, help_text=""):

    st.metric(
        label=title,
        value=value,
        help=help_text
    )


def section(title):

    st.subheader(title)

    st.write("")