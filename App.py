import streamlit as st
from Pages import Home, Project1, Project2, Project3
from streamlit_navigation_bar import st_navbar as navbar
from PIL import Image

image = Image.open("img/magic.png")
st.set_page_config(page_title="The Work", initial_sidebar_state="collapsed", page_icon=image)

pages = ["Home", "Project1", "Project2", "Project3"]

styles = {
    "nav": {
        "background-color": "rgb(123, 209, 146)",
        "display": "flex",
        "justify-content": "center",
        "align-items": "center",
        "height": "30px",
    },

    "img": {
        "bottom": "0.5px",
        "height": "30px",
    },

    "div": {
        "max-width": "32rem",
    },

    "span": {
        "display": "block",
        "border-radius": "0.15rem",
        "padding": "0.2rem 0.725rem",
        "color": "white",
        "font-size": "18px",
    },

    "active": {
        "background-color": "black",
        "font-weight": "normal",
    },

    "hover": {
        "background-color": "rgba(0, 0, 0, 0.35)",
    }
}

page = navbar(pages, logo_path="img/magic.svg", styles=styles)

if page == "Home":
    Home.Home().app()
elif page == "Project1":
    Project1.Project1().app()
elif page == "Project2":
    Project2.Project2().app()
elif page == "Project3":
    Project3.Project3().app()
else:
    Home.Home().app()