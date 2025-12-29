import streamlit as st
import time

st.title("Streamlit テキスト・フォーマット表示サンプル")

# 1. st.text: シンプルなプレーンテキスト
st.subheader("st.text")
st.text("これは st.text を使用したプレーンテキストです。")
st.text("プロポーショナルなフォントで表示されます。等幅フォントは st.code を使用してください。")

st.divider()  # 区切り線

# 2. st.caption: キャプション（注釈）
st.subheader("st.caption")
st.write("補足説明のテキストです。")
st.caption("これは st.caption です。補足説明や注釈に使用される、小さくグレーのテキストです。")

st.divider()

# 3. st.code: コードブロック
st.subheader("st.code")
code_body = '''
def hello_world():
    print("Hello, Streamlit!")
    return True
'''
st.code(code_body, language='python')
st.caption("language引数を指定することでシンタックスハイライトが適用されます。")

st.divider()

# 4. st.latex: 数式
st.subheader("st.latex")
st.write("LaTeX形式で数式を正確に表示します。個人的には使いません。")
st.latex(r'''
    f(x) = \int_{-\infty}^\infty
    \hat f(\xi)\,e^{2 \pi i \xi x}
    \,d\xi
''')

st.divider()

# 5. st.echo: コードと実行結果の同時表示
st.subheader("st.echo")
st.write("withブロックの中身の「コード」と「実行結果」の両方を表示します。")

with st.echo():
    # ここに書いたコードはそのまま画面に表示され、実行もされます
    def calculate_area(radius):
        return 3.14 * radius ** 2
    
    answer = calculate_area(10)
    st.write(f"計算結果: {answer}")

st.divider()

st.subheader("st.badge")
st.write("バッジを表示します。")
st.badge("New!" , icon=":material/new_releases:", color="red")
st.badge("Success", icon=":material/check:", color="green")

st.divider()

