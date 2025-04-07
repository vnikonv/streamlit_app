import streamlit as st
import cv2
import tempfile
import numpy as np
from pathlib import Path
from yt_dlp import YoutubeDL
from streamlit_webrtc import webrtc_streamer, WebRtcMode

class Project2:
    def __init__(self):
        self.cap = None

    def app(self):
        st.title("Стриминг Видео в Streamlit")

        source_option = st.selectbox(
            "Выберите источник потока видео",
            ("Мобильная камера", "YouTube ссылка", "Локальное хранилище", "Веб-камера", "RTSP")
        )

        video_url = None

        if source_option == "Мобильная камера":
            img_file = st.camera_input("Снимите фото")
            if img_file is not None:
                file_bytes = np.asarray(bytearray(img_file.read()), dtype=np.uint8)
                frame = cv2.imdecode(file_bytes, 1)
                st.image(frame, channels="BGR")

        elif source_option == "Youtube ссылка":
            youtube_url = st.text_input("Вставьте ссылку")
            if youtube_url:

                with st.spinner("Видео сейчас загружается"):
                    try:
                        ydl_opts = {"format": "best[ext=mp4]/best", "noplaylist": True}
                        with YoutubeDL(ydl_opts) as ydl:
                            info_dict = ydl.extract_info(youtube_url, download=False)
                            video_url = info_dict.get("url", None)
                    except Exception as e:
                        st.error(f"Произошла ошибка: {e}")

                if video_url:
                    st.video(video_url)

        elif source_option == "Локальное хранилище":
            video_file = st.file_uploader("Загрузите видео", type = ["mp4", "avi", "mov"])
            if video_file:
                temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=Path(video_file.name).suffix)
                temp_file.write(video_file.read())
                video_url = temp_file.name
                st.video(video_url)


        elif source_option == "Веб-камера":
            st.write("Веб-камера сейчас загружается. . .")
            webrtc_streamer(key="webcam", mode=WebRtcMode.SENDRECV)

        elif source_option == "RTSP":
            rtsp_url = st.text_input("Вставьте RTSP ссылку")
            if rtsp_url:
                video_url = rtsp_url

        run_button = st.button("Запустить")
        frame_place = st.empty()


        if run_button and video_url is not None and source_option in ["Локальное хранилище", "RTSP"]:
            self.cap = cv2.VideoCapture(video_url)


            if not self.cap.isOpened():
                st.error("Ошибка открытия видео")
            else:
                stop_button = st.button("Стоп!")
                while self.cap.isOpened() and not stop_button:
                    ret, frame = self.cap.read()
                    if not ret:
                        st.write("В доступе отказано")
                        break

                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    frame_place.image(frame, channels="RGB")

                    if stop_button:
                        break

                self.cap.release()
                cv2.destroyAllWindows()

