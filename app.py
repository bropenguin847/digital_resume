import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="Lim's Digital Resume", page_icon=":ninja:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#insert CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

#animation and pics
lottie_hacking = load_lottieurl("https://lottie.host/e4a1071a-f712-42c5-a96f-8158ac157cfd/aacTeQvv3q.json")
useless_machine = Image.open("images\pngwing.com.png")
image_gen = Image.open("images\image_gen.png")

with st.container():#header
    st.header("Hello there,")
    st.subheader("""**I am LIM YEOW SHENG** :wave:""")
    st.title("This is my digital resume")
    st.write("I am a JMTI student studying Electronics Engineering Course, I am currently looking for internship opportunity.")

#what i do
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do:")
        st.write("###")
        st.write(
            """
            During my course, I have learned a great deal of stuff

            - add more stuff

            - qualifications
            """
        )
        st.header("👇")
        st.write("[My YouTube Channel](https://www.youtube.com/@bropenguin4582/featured)")
    
    with right_column:
        st_lottie(lottie_hacking, height=300, key="hacking")

#my projects
with st.container():
    st.write("---")
    st.subheader("🦾My Projects🧑‍💻")
    st.write("##")
    image_column, text_column = st.columns((1,2))   #text column is twice as big as image column
    with image_column:      # upload an image
        st.image(useless_machine)
    with text_column:
        st.subheader("Useless machine")
        st.write(
            """
            Learned how to create useless machine

            This project is dedicated for my lecturer / FYP Supervisor
            """
        )

with st.container():
    st.write("---")
    st.write("##")
    text_column, image_column = st.columns((2,1))   #image column is twice as big as text column
    with image_column:
        st.image(image_gen)
    with text_column:
        st.subheader("Self-hosted Image Generator")
        st.write(
            """
            Learned how to host image generator for my own

            This project is made to produce custom image for my own use

            Hosted on Google collab
            """
        )

#find me
with st.container():
    st.divider()
    st.header("Reach out to me!")
    st.write("#")
    st.write(
            """
            Gmail: yeowsheng847@gmail.com

            Telephone: 0174270979

            LinkedIn: ...
            """
        )
    st.write("[Here is my github page:](https://github.com/bropenguin847)")