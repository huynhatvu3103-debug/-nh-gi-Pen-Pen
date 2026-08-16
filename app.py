import streamlit as st
import pandas as pd
from datetime import datetime
import os
import base64

st.set_page_config(page_title="Khảo sát trải nghiệm với Vinh", page_icon="🎮")

# Khai báo biến đường dẫn file csv
FILE_PATH = "danh_gia_vinh.csv"

st.audio("Pen Pen Lurk Bait.mp3")

st.title("🎮 Phiếu khảo sát trải nghiệm")

# Chèn ảnh (Thay tên file ảnh nếu cần)
if os.path.exists("6a1821c9-ea31-4281-88eb-a2d1c2cea51a.jpg"):
    st.image("6a1821c9-ea31-4281-88eb-a2d1c2cea51a.jpg", caption="Chào mừng bạn đến với buổi khảo sát!", use_container_width=True)

# Form khảo sát
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
    
    if submitted:
        new_data = pd.DataFrame([{
            "Thời gian": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Tên khách": ten_khach,
            "Đánh giá chơi": hai_long_choi,
            "Đánh giá ăn uống": danh_gia_an_uong
        }])
        
        if not os.path.isfile(FILE_PATH):
            new_data.to_csv(FILE_PATH, index=False)
        else:
            new_data.to_csv(FILE_PATH, mode='a', header=False, index=False)
            
        st.success("Cảm ơn bạn đã gửi đánh giá!")

# Tạo phần ẩn bảng bằng mật khẩu
st.write("---")
admin_pass = st.text_input("🔐 Nhập mật khẩu Admin để xem kết quả:", type="password")

if admin_pass == "123456":  # Thay 123456 thành mật khẩu của bạn
    if os.path.exists(FILE_PATH):
        st.subheader("📊 Kết quả khảo sát")
        df = pd.read_csv(FILE_PATH)
        st.dataframe(df)
