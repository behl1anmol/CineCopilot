import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Cine Copilot",
    page_icon="🙋",
    layout="wide"
)
st.markdown("<h1 style='text-align: center;'>Welcome to Cine Copliot! 🍿🎬🎸</h1>", unsafe_allow_html=True)

image = Image.open('Cine-Copilot.jpg')
image = image.resize((500, 500))

col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    st.image(image, caption='Old 1950s computer on a teal background')

with col3:
    st.write(' ')

st.sidebar.success("Select an app above.")

st.markdown(
    """
    Cine Copilot is an application built using Python and Streamlit
    which provides movies and songs recommendation to the user.
    **👈 Select an app from the sidebar** for recommendations 
    of what Streamlit can do!
    ### Want to learn more?
    - Check out [Github@//CineCopilot](https://github.com/behl1anmol/CineCopilot))
"""
)




