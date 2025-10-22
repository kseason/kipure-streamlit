import streamlit as st

st.write("st.version:", st.__version__)

st.subheader("リンクのサンプル：st.link_button")

st.link_button("解説のページはこちら", "https://www.kipure.com/article/450/")


st.subheader("リンクのサンプル：st.markdown")

st.markdown(
    """    
    - [解説のページはこちら](https://www.kipure.com/article/450/)
    """
)

st.write("st.markdownは、記載時のバージョンでは、target属性を指定できないため、新しいタブで開きません。")
st.write("そのため、このページのようなstreamlit app galleryでは、正しく遷移しない可能性があります。")
st.write("また、class属性も指定できないため、スタイルのカスタマイズもできません。")

st.subheader("リンクのサンプル：st.html")
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
        

<a class="kipure_btn" href="https://www.kipure.com/article/449/" target="_blank">リンクのサンプル</a>

<a class="kipure_btn" href="https://www.kipure.com/article/449/" target="_blank">解説ページはこちら</a>
        ''')






