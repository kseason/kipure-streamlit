import streamlit as st
import time
import pandas as pd

st.title("st.write と st.write_stream の比較")

# タブで表示を分けます
tab1, tab2 = st.tabs(["🖊️ st.write (通常)", "🌊 st.write_stream (ストリーミング)"])

# --- st.write の例 ---
with tab1:
    st.header("st.write の特徴")
    st.markdown("データやテキストを**一度に**表示します。")
    
    if st.button("st.write を実行"):
        # テキスト
        st.write("これは通常のテキストです。一瞬でレンダリングされます。")
        
        # データフレーム（st.writeは何でも表示できる万能関数です）
        df = pd.DataFrame({
            '名前': ['Alice', 'Bob', 'Charlie'],
            '点数': [85, 90, 78]
        })
        st.write("データフレームも表示できます：", df)

# --- st.write_stream の例 ---
with tab2:
    st.header("st.write_stream の特徴")
    st.markdown("ジェネレータを受け取り、**タイプライターのように**文字を流して表示します（ChatGPT風）。")

    # ストリーミング用のジェネレータ関数
    # 文字を少しずつ「yield（生成）」して返すのがポイントです
    def stream_data():
        response_text = """
        こんにちは！
        st.write_streamを使うと、このようにAIチャットのような演出が可能です。
        
        テキストだけでなく、データの一部を少しずつ渡すこともできますが、
        主にLLM（大規模言語モデル）の応答を表示するのによく使われます。
        """
        for word in response_text:
            yield word
            time.sleep(0.05)  # 表示速度の調整用ウェイト

    if st.button("ストリーミングを開始"):
        # ここでジェネレータ関数を渡します
        st.write_stream(stream_data)
