import streamlit as st
import pandas as pd
from datetime import datetime
import os
import base64
st.set_page_config(page_title="Khảo sát trải nghiệm với Vinh", page_icon="🎮")

st.title("🎮 Phiếu khảo sát trải nghiệm")

# Chèn ảnh và nhạc chào mừng ở đầu trang
st.image("6a1821c9-ea31-4281-88eb-a2d1c2cea51a.jpg", caption="Chào mừng bạn đến với buổi khảo sát!", use_container_width=True)
autoplay_audio("Pen Pen Lurk Bait.mp3")
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
    # Kiểm tra nếu file dữ liệu đã tồn tại thì hiển thị ra
if os.path.exists(FILE_PATH):
    st.subheader("📊 Danh sách kết quả đã gửi")
    df = pd.read_csv(FILE_PATH)
    st.dataframe(df)
