import streamlit as st


pages = {
    "menu": [
        st.Page("pages/00_top.py", title="top"),
        st.Page("pages/01_image.py", title="画像"),
        st.Page("pages/01_link.py", title="リンク"),
    ],
}

pg = st.navigation(pages)
pg.run()