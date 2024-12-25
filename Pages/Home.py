import streamlit as st
from PIL import Image

class Home:
    def __init__(self):
        pass
    def app(self):
        st.write(st.__version__)
        name = "Elise Typhon, the Spectator"
        description = """
        Junior Magician, temporarily unemployed
        """
        email = "elise_typhon@email.com"
        social_media = {
            "YouTube": "https://youtube.com",
            "LinkedIn": "https://linkedin.com",
            "GitHub": "https://github.com",
            "Twitter": "https://twitter.com",
        }

        image = Image.open("img/magic.png")

        col1, col2 = st.columns(2, gap="small")
        with col1:
            st.image(image, width=230)

        with col2:
            st.title(name)
            st.write(description)
            st.write("📫", email)

        # --- SOCIAL LINKS ---
        st.write('\n')
        cols = st.columns(len(social_media))
        for index, (platform, link) in enumerate(social_media.items()):
            cols[index].write(f"[{platform}]({link})")

        # --- EXPERIENCE & QUALIFICATIONS ---
        st.write('\n')
        st.subheader("Experience & Qualifications")
        st.write(
            """
        - ✔️ 100+ Years experience extracting actionable insights from data
        - ✔️ An ever-growing knowledge of natural languages, C2 Russian, C1 English, B2 French, B2 Kazakh, B1 Latin, A1 Sumerian
        - ✔️ Effective management skills, academic literacy and a strong sense of initiative on tasks
        """
        )

        # --- SKILLS ---
        st.write('\n')
        st.subheader("Hard Skills")
        st.write(
            """
        - 👩‍💻 Programming: Python, Java
        - 📊 Data Visualization: MS Excel, Streamlit
        - 📚 Web-programming: HTML, CSS, Javascript
        - 🗄️ Databases: MySQL
        """
        )

        # --- WORK HISTORY ---
        st.write('\n')
        st.subheader("Work History")
        st.write("---")

        # --- JOB 1
        st.write("🚧", "**Unemployed**")
        st.write("02/1920 - Present")
        st.write(
            """
        - ► For some reason, noone is eager to hire a young and prospective sorcerer that is yours truly :(
        - ► I have been sitting in my mind-dungeon for over a century and am still locked insideth  
        - ► Maybe programming will bring upon more benefits than sorcery did...
        """
        )

        # --- Projects & Accomplishments ---
        st.write('\n')
        st.subheader("Projects & Accomplishments")
        st.write("---")
        st.write("""
        - 🏆 IELTS 7.5 - Passed the paper-based version of IELTS by British Council
        - 🏆 Data Analysis Using Python on Coursera - Working with Numpy and Pandas
        - 🏆 AI Capstone Project with Deep Learning on Coursera - Working with PyTorch and configuring pre-trained models
        - 🏆 Project Management Project on Coursera - A Thermal Power Plant Modernization Project
        """)

        st.markdown("""<style>
        a {
        text-decoration: none;
        color: white !important;
        font-weight: 500;
        }
        a: hover {
        color:  # d33682 !important;
        text-decoration: none;
        }
        ul {
        list-style-type: none;
        }
        </style>""", unsafe_allow_html=True)