import streamlit as st

st.set_page_config(page_title="系列選択",page_icon="🎓")

st.title("🎓 新入生のための系列選択ナビ")
st.write("質問に答えて、あなたにぴったりの系列を見つけよう！")

if 'step' not in st.session_state:
    st.session_state.step = 'start'

if  st.session_state.step == 'start':
     st.subheader("北神戸総合高校系列選択へようこそ！(始める場合は始めるを押してね)")
     col1, col2  = st.columns(2)
     with col1:
         if st.button("始める"):
          st.session_state.step = 'IE'
          st.rerun()
     with col2:
         if st.button("系列選択の説明を見る"):
          st.session_state.step = 'NO'
          st.rerun()
elif st.session_state.step == 'NO':
    st.subheader('KIKS系列説明')
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("天の学び"):
            st.session_state.step = 'tennkaisetu'
            st.rerun()
    with col2:
        if st.button("地の学び"):
            st.session_state.step = 'tikaisetu'
            st.rerun()
    with col3:
        if st.button("人の学び"):
            st.session_state.step = 'zinnkaisetu'
            st.rerun()
    with col4:
        if st.button("戻る"):
            st.session_state.step = 'start'
            st.rerun()
elif st.session_state.step == 'tennkaisetu':
    st.subheader('天の学びの解説'):
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("宇宙・気象系列の解説"):
            st.session_state.step = 'utyuukaisetu'
            st.rerun()
    with col2:
        if st.button("DX系列の解説"):
            st.session_state.step = 'DXkaisetu'
            st.rerun()
    with col3:
        if st.button('戻る', key="back_to_bunkei_2"):
            st.session_state.step = 'NO'
            st,rerun()
elif st.session_state.step == 'tikaisetu':
    st.subheader('地の学びの解説'):
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("兵庫からスタートアップ系列の解説"):
            st.session_state.step = 'utyuukaisetu'
            st.rerun()
    with col2:
        if st.button("スポーツアウトドアと防災系列の解説"):
            st.session_state.step = 'DXkaisetu'
            st.rerun()
    with col3:
        if st.button('戻る', key="back_to_bunkei_3"):
            st.session_state.step = 'NO'
            st,rerun()
elif st.session_state.step == 'zinnkaisetu':
    st.subheader('人の学びの解説'):
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("ダイバーシティ＆インクルージョン系列の解説"):
            st.session_state.step = 'daibakaisetu'
            st.rerun()
    with col2:
        if st.button("リベラルアーツ理系系列の解説"):
            st.session_state.step = 'riberikaisetu'
            st.rerun()
    with col3:
        if st.button("リベラルアーツ文系系列の解説"):
            st.session_state.step = 'ribebunnkaisetu'
            st.rerun()
    with col4:
        if st.button('戻る', key="back_to_bunkei_4"):
            st.session_state.step = 'NO'
            st,rerun()

elif st.session_state.step == 'IE':
    st.subheader("Q1. 北神戸総合高校は好きですか？")
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
        if st.button('戻る', key="back_to_bunkei_5"):
            st.session_state.step = 'bunnkei'
            st.rerun()
    with col4:
        if st.button('暗記が得意だった', key="back_to_rikei_2"):
            st.session_state.step = 'rikei'
            st.rerun()

elif st.session_state.step == 'zinnnomanabi':
    st.subheader("芸術や外国語に興味はありますか？")

    col1, col2, col3, col4 =st.columns(4)
    with col1:
        if st.button('はい', key="final_yes"):
            st.session_state.result = "ダイバーシティー&インクルージョン系列"
            st.session_state.step = 'goal'
            st.rerun()
    with col2:
        if st.button('いいえ', key="final_no"):
            st.session_state.result = "リベラルアーツ文系系列"
            st.session_state.step = 'goal'
            st.rerun()
    with col3:
        if st.button('戻る', key="back_to_bunkei_6"):
            st.session_state.step = 'bunnkei'
            st.rerun()
    with col4:
        if st.button('暗記が得意だった', key="back_to_rikei_3"):
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
