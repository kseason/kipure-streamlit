import streamlit as st

st.markdown("""
width100% max704px
元のサイズ:	300 × 1536 px
""")

st.image("media/image/sunshain300.png", caption="朝日を浴びる")

st.image("media/image/sunshain300.png", caption="朝日を浴びる",width=200)

with st.container(width="stretch",border=True):
    st.image("media/image/sunshain300.png", caption="朝日を浴びる")

with st.container(width="stretch",border=True):
    st.image("media/image/sunshain300.png", caption="朝日を浴びる",width="stretch")

st.image("media/image/sunshain300.png", caption="朝日を浴びる",output_format="PNG")



