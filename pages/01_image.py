import streamlit as st

st.write("st.version:", st.__version__)

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



st.html('''
<style>
.kipure_btn {
    width: 90%;
    max-width: 300px;
    display: block;
    cursor: pointer;
    text-align: center;
    margin: 0 auto 20px;
    padding: 10px 10px;
    font-size: 14px;
    color: #FFF;
    background-color: #C00;
    border-radius: 5px;
    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.4);
</style>
        

<a class="kipure_btn" href="https://www.kipure.com/article/449/" target="_blank">解説ページへ</a>

        
''')






