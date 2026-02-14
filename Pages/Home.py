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
			"Telegram": "https://t.me/second_nikon",
			"LinkedIn": "https://linkedin.com/in/nikon-veremeichik-44055b361"
		}

		image = Image.open("img/me_docs.png")

		col1, col2, col3 = st.columns([0.2, 0.2, 0.6], gap="small")
		with col1:
			st.image(image, use_column_width=True)
			
		with col2:
			st.image("img/me_2020.jpg", use_column_width=True)

		with col3:
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
		- ✔️ Обладаю грамотной письменной и устной речью. Увлекаюсь искусством, культурой и музыкой. В свободное время совершенствую профессиональные навыки, программирую, рисую, и изучаю языки.
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
		- 📚 Веб-Программирование: HTML, Tailwinds CSS, JavaScript/TypeScript, Nuxt, React/Vite
		- 🗄️ Работа с Базами Данных: PostgreSQL, REST API, Prisma ORM
		- 🐧 Работа с GNU/Linux: ArchLinux, Ubuntu
		- 🌐 Администрирование Компьютера: установка ОС, замена комплектующих, изменение параметров BIOS, редактирование реестра Windows, настройка локальных политик безопасности, Event Viewer, Schedulers
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
		st.write("07/09/2005 - 22/04/2025")
		st.write(
			"""
		- ► Учусь и продолжаю учиться
		"""
		)

		# --- JOB 2
		st.write('\n')
		st.write("🚧", "**Рабочая практика в ИП Бухонин Иван Игоревич**")
		st.write("22/04/2025 - 26/06/2025")
		st.write(
			"""
		- ► Прошел стажировку в качестве разработчика приложений с полным стеком во фреймворке React + Vite, используя Express.js для серверной логики, в рамках моей университетской программы.
			Работал в команде с семью другими стажерами-студентами. Главная цель нашей команды состояла в создании веб -приложения для управления сессиями DND.
			Я был ответственным за менеджмент проекта, напрямую участвовал в его планировании, определял подходящий стек технологий и техническое направление.
		"""
		)

		# --- Projects & Accomplishments ---
		st.write('\n')
		st.subheader("Проекты и Достижения")
		st.write("---")
		st.markdown("""
		<ul>
		<li>- 🏆 IELTS 7.5 - Прохождение бумажной версии теста IELTS от British Council</li>
		<li>- 🏆 Data Analysis Using Python on Coursera - Работа с Numpy и Pandas</li>
		<li>- 🏆 AI Capstone Project with Deep Learning on Coursera - Работа с PyTorch и конфигурация pre-trained моделей</li>
		<li>- 🏆 Project Management Project on Coursera - Разработка плана реализации проекта <a href="https://github.com/vnikonv/streamlit_app/blob/main/Pages/project.docx" download="project.docx">Модернизации Тепловой Электростанции</a> с точки зрения менеджмента</li>
		<li>- 🏆 Личный проект по обучению LoRA модели через Transformers на чекпоинте Pythia-6.9b</li>
		<li>- 🏆 Создание антифрод модели</a> с помощью XGBoost в рамках конкурса от КБТУ</li>
		<li>- 🏆 Личный проект по инференсу .gguf моделей с помощью CLI LLama.cpp</li>
		</ul>
		""", unsafe_allow_html=True)
		
		# --- Explanation ---
		st.write('\n')
		st.subheader("Об этом сайте")
		st.write("---")
		st.write("""
		Изначально, здесь хостились только мои проекты по визуализации данных и работе с медиа-потоками на Стримлите.
		На данный момент домашняя страница была преобразована в визитку, а проекты всё ещё доступны в других вкладках.
		Обновление: Этот сайт больше не будет обновляться, так как я намерен сделать новую, более грамотную, визитку.
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
		img {
		border-radius: 15px;
		margin: auto;
		aspect-ratio: 3/4;
		}
		</style>""", unsafe_allow_html=True)
