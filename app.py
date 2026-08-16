import streamlit as st
import pandas as pd
from datetime import datetime
import os

st.set_page_config(page_title="Khảo sát trải nghiệm với Vinh", page_icon="🎮")

FILE_PATH = "danh_gia_vinh.csv"

st.title("🎮 Phiếu khảo sát trải nghiệm")
6a1821c9-ea31-4281-88eb-a2d1c2cea51a.jpg
with st.form("khao_sat_form", clear_on_submit=True):
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
