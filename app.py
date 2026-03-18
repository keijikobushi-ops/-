import streamlit as st

st.set_page_config(page_title="系列選択",page_icon="🎓")

st.title("🎓 新入生のための系列選択ナビ")
st.write("質問に答えて、あなたにぴったりの系列を見つけよう！")

if 'step' not in st.session_state:
    st.session_state.step = 'start'

if  st.session_state.step == 'start':
     st.subheader("Q1. 北神戸総合高校に興味はありますか？")
     col1 = st.columns(1)
     with col1[0]: # Changed from 'with col1:' to 'with col1[0]:'
         if st.button("はい"):
          st.session_state.step = 'YES'
          st.rerun()
elif st.session_state.step == 'YES':
    st.subheader("Q2. 暗記が得意ですか？思考判断が得意ですか？")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("暗記"):
            st.session_state.step = 'rikei'
            st.rerun()
    with col2:
        if st.button("思考判断"):
            st.session_state.step = 'bunnkei'
            st.rerun()

elif st.session_state.step == 'rikei':
    st.subheader("Q3.どっちの方が好きですか？")
    col1, col2,col3, col4 =st.columns(4)
    with col1:
        if st.button("宇宙・気象"):
            st.session_state.result = "宇宙気象系列"
            st.session_state.step = 'goal'
            st.rerun()
    with col2:
        if st.button("プログラミング・ゲーム"):
            st.session_state.result = "DX系列"
            st.session_state.step = 'goal'
            st.rerun()
    with col3:
        if st.button("両方興味はない"):
            st.session_state.result = "リベラルアーツ理系系列"
            st.session_state.step = 'goal'
            st.rerun()
    with col4:
        if st.button("暗記が得意ではなかった"):
            st.session_state.step = 'bunnkei'
            st.rerun

elif st.session_state.step == 'bunnkei':
    st.subheader("あなたが興味を持ったのはどれですか")
    col1, col2, col3 =st.columns(3)
    with col1:
        if st.button("観光・防災") :
            st.session_state.step = 'tinomanabi'
            st.rerun()
    with col2:
        if st.button("言語・文化・歴史"):
            st.session_state.step = 'zinnnomanabi'
            st.rerun()
    with col3:
        if st.button("暗記は得意だった"):
            st.session_state.step = 'rikei'
            st.rerun()

elif st.session_state.step == 'tinomanabi':
    st.subheader("あなたが身につけたい能力は？")
    col1, col2, col3, col4 =st.columns(4)
    with col1:
        if st.button('マーケティング'):
            st.session_state.result = "兵庫からスタートアップ系列"
            st.session_state.step = 'goal'
            st.rerun()
    with col2:
        if st.button('スポーツ・アウトドア'):
            st.session_state.result = "スポーツアウトドアと防災系列"
            st.session_state.step = 'goal'
            st.rerun()
    with col3:
        if st.button('自分に興味を持ったのは'):
            st.session_state.step = 'bunnkei'
            st.rerun()
    with col4:
        if st.button('暗記は得意だった'):
            st.session_state.step = 'rikei'
            st.rerun()

elif st.session_state.step == 'zinnnomanabi':
    st.subheader("芸術や外国語に興味はありますか？")
    col1, col2, col3, col4 =st.columns(4)
    with col1:
        if st.button('はい'):
            st.session_state.result = "ダイバーシティー&インクルージョン系列"
            st.session_state.step = 'goal'
            st.rerun()
    with col2:
        if st.button('いいえ'):
            st.session_state.result = "リベラルアーツ文系系列"
            st.session_state.step = 'goal'
            st.rerun()
    with col3:
        if st.button('自分が興味を持ったのは言語・文化・歴史だった'):
            st.session_state.step = 'bunkei'
            st.rerun()
    with col4:
        if st.button('暗記は得意だった'):
            st.session_state.step = 'rikei'
            st.rerun()

elif st.session_state.step == 'goal':
    st.balloons()
    st.success(f"あなたにおすすめなのは…\n\n## **【{st.session_state.result}】**")

    if "宇宙気象系列" in st.session_state.result:
        st.write("")
    elif "DX系列" in st.session_state.result:
        st.write("")
    elif "リベラルアーツ理系系列" in st.session_state.result:
        st.write("")
    elif "兵庫からスタートアップ系列" in st.session_state.result:
        st.write("")
    elif "スポーツアウトドアと防災系列" in st.session_state.result:
        st.write("")
    elif "ダイバーシティー&インクルージョン系列" in st.session_state.result:
        st.write("")
    elif "リベラルアーツ文系系列" in st.session_state.result:
        st.write("")

    if st.button("最初からやり直す"):
        st.session_state.step = 'start'
        st.session_state.result = ""
        st.rerun()
