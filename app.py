import streamlit as st

# -- タイトル、見出し、テキスト表示 --
st.title('タイトル')
st.header('見出し1')
st.subheader('見出し2')
st.write('これは文字列')
st.write(12345)

# -- テキストボックス --
text = st.text_input('名前を入力してください:')
st.write(f'こんにちは、{text}さん！')

# -- チェックボックス --
if st.checkbox('表示しますか？'):
    st.write('なにもないよ')

# セレクトボックス
option = st.selectbox(
    '何にする？', 
    ('ごはん', 'お風呂', '私')
)
if option == "私":
    st.write(f'あなたは {option} を選びました！お楽しみください。')
else:
    st.error("私にしなさい")

# -- ラジオボタン --
gakka = st.radio("学科を選択してください",('物理','化学','数学'))
if gakka != '化学':
    st.warning("センスないわ")
else:
    st.write("素晴らしい")
# -- ナンバーインプット --
weight = st.number_input('体重を入力してください',min_value=0,step=1,help='正直に入力しましょう')
if weight < 50:
    st.write("痩せすぎです。もっと食べましょう")
else:
    st.write("太り過ぎです。")  

# -- ボタン --
btn = st.button('自爆', type="primary")
if btn:
    st.write('自爆スイッチが押されました')

# -- 画像表示 --
st.image('https://www.aoyama.ac.jp/wp-content/uploads/2018/02/visual_identity_img_02-1.png', caption='イーゴ君')

