Danhgiapenpen
import streamlit as st
import pandas as pd
from datetime import datetime
import os

st.set_page_config(page_title="Khảo sát trải nghiệm với Vinh", page_icon="🎮")

FILE_PATH = "danh_gia_vinh.csv"

st.title("🎮 Phiếu khảo sát trải nghiệm")

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

    gop_y = st.text_area("Cần góp ý gì thêm")

    loi_nhan = st.text_area("Ghi chú đôi lời gửi tới Vinh")

    submitted = st.form_submit_button("Gửi đánh giá")

    if submitted:
        new_row = pd.DataFrame([{
            "Thời gian": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Tên khách": ten_khach,
            "Hài lòng khi chơi với Vinh": hai_long_choi,
            "Đánh giá ăn uống trên pad": danh_gia_an_uong,
            "Góp ý thêm": gop_y,
            "Lời nhắn gửi Vinh": loi_nhan,
        }])

        if os.path.exists(FILE_PATH):
            new_row.to_csv(FILE_PATH, mode="a", header=False, index=False, encoding="utf-8-sig")
        else:
            new_row.to_csv(FILE_PATH, index=False, encoding="utf-8-sig")

        st.success("Cảm ơn bạn đã gửi đánh giá! 🙌")

st.divider()
st.subheader("📊 Danh sách đánh giá")

if os.path.exists(FILE_PATH):
    df = pd.read_csv(FILE_PATH)
    st.dataframe(df, use_container_width=True)

    col1, col2 = st.columns(2)
    col1.metric("Điểm hài lòng chơi TB", round(df["Hài lòng khi chơi với Vinh"].mean(), 2))
    col2.metric("Điểm ăn uống TB", round(df["Đánh giá ăn uống trên pad"].mean(), 2))

    st.download_button(
        "Tải file CSV",
        data=df.to_csv(index=False).encode("utf-8-sig"),
        file_name="danh_gia_vinh.csv",
        mime="text/csv",
    )
else:
    st.info("Chưa có đánh giá nào.")
