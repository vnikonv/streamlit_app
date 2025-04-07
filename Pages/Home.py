import streamlit as st
from PIL import Image

class Home:
	def __init__(self):
		pass
	def app(self):
		st.write(st.__version__)
		name = "Никон Веремейчик"
		age = "19 лет"
		description = """
		Студент второго курса по IT специальности "Информационные Системы в Управлении" в Северо-Казахстанском Университете имени Манаша Козыбаева
		"""
		email = "thesecondnikon@gmail.com"
		social_media = {
			"Coursera": "https://www.coursera.org/learner/nikon-veremeichik",
			"GitHub": "https://github.com/vnikonv",
			"Telegram": "https://t.me/second_nikon"
		}

		image = Image.open("img/me_docs.png")

		col1, col2 = st.columns(2, gap="small")
		with col1:
			st.image(image, width=230)

		with col2:
			st.title(name)
			st.write(age)
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
		- ✔️ Обладаю грамотной письменной и устной речью. Увлекаюсь искусством, культурой и музыкой. В свободное время совершенствую профессиональные навыки, программирую, рисую и изучаю языки.
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
		- 🗄️ Работа с Базами Данных: PostgreSQL, REST API
		- 🐧 Работа с Линуксом: ArchLinux, Ubuntu
		- 🌐 Администрирование Компьютера: установка ОС, замена комплектующих, изменение параметров BIOS, редактирование реестра Windows, настройка локальных политик безопасности
		- 🤖 Машинное Обучение и Искусственный Интеллект: Transformers, PyTorch, XGBoost
		- 💡 Базовые навыки Фотошопа
		"""
		)

		# --- WORK HISTORY ---
		st.write('\n')
		st.subheader("Опыт Работы")
		st.write("---")

		# --- JOB 1
		st.write("🚧", "**Безработный**")
		st.write("07/09/2005 - По настоящее время")
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
		- 🏆 IELTS 7.5 - Прохождение бумажной версии теста IELTS от British Council
		- 🏆 Data Analysis Using Python on Coursera - Работа с Numpy и Pandas
		- 🏆 AI Capstone Project with Deep Learning on Coursera - Работа с PyTorch и конфигурация pre-trained моделей
		- 🏆 Project Management Project on Coursera - Разработка плана реализации проекта Модернизации Тепловой Электростанции с точки зрения менеджмента
		- 🏆 Личный проект по обучению LoRA модели через Transformers на чекпоинте Pythia-6.9b
		- 🏆 Создание [антифрод модели](https://kbtunikon.streamlit.app/) с помощью XGBoost в рамках конкурса от КБТУ
		- 🏆 Личный проект по инференсу .gguf моделей с помощью CLI LLama.cpp
		""")
		
		# --- Explanation ---
		st.write('\n')
		st.subheader("Об этом сайте")
		st.write("---")
		st.write("""
		Изначально, здесь хостились только мои проекты по визуализации данных и работе с медиа-потоками на Стримлите.
		Сейчас домашняя страница была преобразована в визитку, а проекты всё ещё доступны в других вкладках.
		""")

		st.markdown("""<style>
		a {
		text-decoration: none;
		color: rgb(123, 209, 146) !important;
		font-weight: 1000;
		}
		a: hover {
		color:  # d33682 !important;
		text-decoration: none;
		}
		ul {
		list-style-type: none;
		}
		</style>""", unsafe_allow_html=True)
