import streamlit as st
from Pages import Home, Project1, Project2, Project3
from streamlit_navigation_bar import st_navbar as navbar
from PIL import Image

image = Image.open("img/magic.png")
st.set_page_config(initial_sidebar_state="collapsed", page_icon=image)

pages = ["Home", "Project1", "Project2", "Project3"]

styles = {
    "nav": {
        "background-color": "rgb(123, 209, 146)",
        "display": "flex",
        "justify-content": "center",
        "font-size": "20px",
        "color": "white",
    },

    "img": {
        "position": "absolute",
        "left": "-20px",
        "top": "4px",
        "width": "100px",
        "height": "40px",
    },

    "div": {
        "max-width": "32rem",
    },

    "span": {
        "border-radius": "0.5rem",
        "color": "rgb(49, 51, 63)",
        "margin": "0 0.125rem",
        "padding": "0.4375rem 0.625rem",
    },

    "active": {
        "background-color": "rgba(105, 114, 255, 0.25)",
    },

    "hover": {
        "background-color": "rgba(255, 255, 255, 0.35)",
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