
import streamlit as st
import requests

# Find more emojis here:https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title='This Is My Beautiful webpage',page_icon=':tada',layout='wide')


uploaded_file = st.file_uploader("Choose a file", type=["jpg", "jpeg", "png", "webp"])
if uploaded_file is not None:
    st.image(uploaded_file)


# HEADER SECTION
st.subheader('Hi, I am Komal Saini '":wave:")
st.title("An AI Engineer Fresher From India")
st.write('I am Passionate about creating new websites and make models using python and machine learning that to be more efficient and effective in business.')
st.write("Learn More>](https://www.geeksforgeeks.org/python-programming-language-tutorial/)")

# What I Do

with st.container():
    st.write("----")
    left_column,right_column=st.columns(2)
    with left_column:
        st.header('What I Do')
        st.write('##')
        st.write()