import streamlit as st


pages = {
    "menu": [
        st.Page("pages/00_top.py", title="top"),
        st.Page("pages/01_image.py", title="画像"),
    ],
}

pg = st.navigation(pages)
pg.run()