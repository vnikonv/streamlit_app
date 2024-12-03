import streamlit as st
from PIL import Image

class Home:
    def __init__(self):
        pass
    def app(self):
        st.write(st.__version__)
        page_title = "Digital CV | John Doe"
        page_icon = ":wave:"
        name = "John Doe"
        description = """
        Senior Data Analyst, assisting enterprises by supporting data-driven decision-making.
        """
        email = "johndoe@email.com"
        social_media = {
            "YouTube": "https://youtube.com/c/codingisfun",
            "LinkedIn": "https://linkedin.com",
            "GitHub": "https://github.com",
            "Twitter": "https://twitter.com",
        }
        projects = {
            "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
            "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
            "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
            "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
        }

        st.set_page_config(page_title=page_title, page_icon=page_icon)

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
        - ✔️ 7 Years experience extracting actionable insights from data
        - ✔️ Strong hands on experience and knowledge in Python and Excel
        - ✔️ Good understanding of statistical principles and their respective applications
        - ✔️ Excellent team-player and displaying strong sense of initiative on tasks
        """
        )

        # --- SKILLS ---
        st.write('\n')
        st.subheader("Hard Skills")
        st.write(
            """
        - 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, VBA
        - 📊 Data Visualization: PowerBi, MS Excel, Plotly
        - 📚 Modeling: Logistic regression, linear regression, decision trees
        - 🗄️ Databases: Postgres, MongoDB, MySQL
        """
        )

        # --- WORK HISTORY ---
        st.write('\n')
        st.subheader("Work History")
        st.write("---")

        # --- JOB 1
        st.write("🚧", "**Senior Data Analyst | Ross Industries**")
        st.write("02/2020 - Present")
        st.write(
            """
        - ► Used PowerBI and SQL to redeﬁne and track KPIs surrounding marketing initiatives, and supplied recommendations to boost landing page conversion rate by 38%
        - ► Led a team of 4 analysts to brainstorm potential marketing and sales improvements, and implemented A/B tests to generate 15% more client leads
        - ► Redesigned data model through iterations that improved predictions by 12%
        """
        )

        # --- JOB 2
        st.write('\n')
        st.write("🚧", "**Data Analyst | Liberty Mutual Insurance**")
        st.write("01/2018 - 02/2022")
        st.write(
            """
        - ► Built data models and maps to generate meaningful insights from customer data, boosting successful sales eﬀorts by 12%
        - ► Modeled targets likely to renew, and presented analysis to leadership, which led to a YoY revenue increase of $300K
        - ► Compiled, studied, and inferred large amounts of data, modeling information to drive auto policy pricing
        """
        )

        # --- JOB 3
        st.write('\n')
        st.write("🚧", "**Data Analyst | Chegg**")
        st.write("04/2015 - 01/2018")
        st.write(
            """
        - ► Devised KPIs using SQL across company website in collaboration with cross-functional teams to achieve a 120% jump in organic traﬃc
        - ► Analyzed, documented, and reported user survey results to improve customer communication processes by 18%
        - ► Collaborated with analyst team to oversee end-to-end process surrounding customers' return data
        """
        )

        # --- Projects & Accomplishments ---
        st.write('\n')
        st.subheader("Projects & Accomplishments")
        st.write("---")
        for project, link in projects.items():
            st.write(f"[{project}]({link})")