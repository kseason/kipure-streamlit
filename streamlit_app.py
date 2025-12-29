import streamlit as st


pages = {
    "menu": [
        st.Page("pages/00_top.py", title="top"),
        st.Page("pages/01_image.py", title="画像"),
        st.Page("pages/01_link.py", title="リンク"),
        st.Page("pages/02_write.py", title="書き込み"),
        st.Page("pages/02_formatted_text.py", title="フォーマットテキスト"),
    ],
}

pg = st.navigation(pages)
pg.run()

with st.sidebar:
    st.write("st.version:", st.__version__)

st.logo(
    image="media/image/common/logo_g.png",
    link="https://www.kipure.com/",
    size="large",
)
