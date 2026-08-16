import streamlit as st
import pandas as pd
from datetime import datetime
import os

st.set_page_config(page_title="Khảo sát trải nghiệm với Vinh", page_icon="🎮")

FILE_PATH = "danh_gia_vinh.csv"

st.title("🎮 Phiếu khảo sát trải nghiệm")
st.image("6a1821c9-ea31-4281-88eb-a2d1c2cea51a.jpg", caption="Đánh giá Pen Pen", use_container_width=True)
with st.form("khao_sat_form", clear_on_submit=True):
    import base64

# Hàm hỗ trợ tự động phát nhạc từ file local
def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio autoplay loop style="display:none;">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(md, unsafe_allow_html=True)

# Gọi hàm phát nhạc (Thay "sound.mp3" bằng đúng tên file nhạc của bạn)
autoplay_audio("Pen Pen Lurk Bait.mp3")
    ten_khach = st.text_input("Tên của bạn")
    
    hai_long_choi = st.slider(
        "Mức độ hài lòng khi chơi với Vinh", 1, 5, 3,
        help="1 = Rất không hài lòng, 5 = Rất hài lòng"
    )
    
    danh_gia_an_uong = st.slider(
        "Đánh giá sự ăn uống trên pad", 1, 5, 3,
        help="1 = Rất tệ, 5 = Rất ngon"
    )
    
    submitted = st.form_submit_button("Gửi đánh giá")
