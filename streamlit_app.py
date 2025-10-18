import streamlit as st


pages = {
    "カテゴリー１": [
        st.Page("pages/sample.py", title="サンプル"),
    ],
}

pg = st.navigation(pages)
pg.run()