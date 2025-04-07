import streamlit as st
from PIL import Image

class Home:
    def __init__(self):
        pass
    def app(self):
        st.write(st.__version__)
        name = "Никон Веремейчик, 19 лет"
        description = """
        Студент второго курса по специальности "Информационные Системы в Управлении" в Северо-Казахстанском Университете имени Манаша Козыбаева
        """
        email = "thesecondnikon@gmail.com"
        social_media = {
            "Coursera": "https://www.coursera.org/learner/nikon-veremeichik",
            "GitHub": "https://github.com/vnikonv",
			"Telegram": "t.me/second_nikon"
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
        st.subheader("Личные Качества и Квалификации")
        st.write(
            """
        - ✔️ Активно участвую в командных проектах. Вежлив, доброжелателен. Серьёзно отношусь к выполнению поставленных задач.
        - ✔️ Прекрасно знаю Русский (С2) и Английский (С1); знаю Французский и Казахский на среднем уровне (B2).
        - ✔️ Обладаю грамотной письменной и устной речью. Увлекаюсь искусством, культурой и музыкой. В свободное время совершенствую профессиональные навыки, программирую и изучаю языки. 
		- ✔️ В особенности люблю системно организовывать информацию и поддерживать порядок в рабочих процессах.
		 """
        )

        # --- SKILLS ---
        st.write('\n')
        st.subheader("Профессиональные Навыки")
        st.write(
            """
        - 👩‍💻 Программирование: Python, Java, C++
        - 📊 Визуализация Данных: MS Excel, Streamlit
        - 📚 Веб-Программирование: HTML, Tailwinds CSS, JavaScript/TypeScript, Nuxt
        - 🗄️  Работа с Базами Данных: PostgreSQL
		- 🐧💻 Работа с Линуксом: ArchLinux
		- 🤖 Машинное Обучение: Transformers, PyTorch
        """
        )

        # --- WORK HISTORY ---
        st.write('\n')
        st.subheader("Опыт работы")
        st.write("---")

        # --- JOB 1
        st.write("🚧", "**Безработный**")
        st.write("02/2005 - Present")
        st.write(
            """
        - ► Заинтересован в прохождении рабочей практики на Вашем предприятии.
        """
        )

        # --- Projects & Accomplishments ---
        st.write('\n')
        st.subheader("Проекты и Достижения")
        st.write("---")
        st.write("""
        - 🏆 IELTS 7.5 - Прошёл бумажную версию теста IELTS by British Council
        - 🏆 Data Analysis Using Python on Coursera - Работа с Numpy и Pandas
        - 🏆 AI Capstone Project with Deep Learning on Coursera - Работа с PyTorch и конфигурация pre-trained моделей
        - 🏆 Project Management Project on Coursera - Проект по Модернизации Термальной Электростанции
		- 🏆 Личный проект по обучению LoRA модели через Transformers на основе Pythia-6.9b
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
