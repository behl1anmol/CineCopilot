import streamlit as st

st.set_page_config(
    page_title="Cine Copilot",
    page_icon="🙋",
)

st.write("# Welcome to Cine Copliot! 👋")

st.sidebar.success("Select an app above.")

st.markdown(
    """
    Cine Copilot is an application built using Python and Streamlit
    which provides movies and songs recommendation to the user.
    **👈 Select an app from the sidebar** for recommendations 
    of what Streamlit can do!
    ### Want to learn more?
    - Check out [Gthub@//CIneCopilot](https://github.com/behl1anmol/CineCopilot))
"""
)