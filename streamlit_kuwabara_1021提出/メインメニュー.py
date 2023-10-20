import streamlit as st
from PIL import Image

st.set_page_config(
    page_title='トカイナカLIFE',
    page_icon='🍊',
    layout="wide",
    initial_sidebar_state="auto"
)

# ロゴ＆ポエム
st.image('tokainakahome.png', use_column_width=True)
st.divider()


# 和歌山市エリアマップ
st.subheader("和歌山で理想のトカイナカを見つけよう！")
st.image('wakayamacity_map.png', caption='和歌山市の７つのエリア', use_column_width=True)
st.divider()

# 中心部　説明
st.subheader('①中心部')
st.write('和歌山市のシンボルである和歌山城を中心に、ぶらくり丁をはじめとするまちなかエリアがあります。古くから城下町として栄えてきた地域で、現在の街並みの骨格は城下町時代から受け継がれてきたものです。')

# 中心部　画像
col1, col2, col3 = st.columns(3)
with col1:
    st.link_button('和歌山城', 'http://wakayamajo.jp/index.html')
    st.image("area1_wakayamajyo.jpg", use_column_width=True)

with col2:
    st.link_button("ぶらくり丁", 'https://kitabura.jp/')
    st.image("area1_burakuri_resize.jpg", use_column_width=True)
    
with col3:
    st.link_button("和歌山県立近代美術館", 'https://www.momaw.jp/')
    st.image("area1_museum.jpg", use_column_width=True)
st.divider()

# 北西部　説明
st.subheader('②北西部')
st.write('アニメやゲームの世界観を彷彿とさせる友ヶ島やサーフィンのメッカ・磯ノ浦など、若者に人気のスポットがあります。海岸の風景も美しいですが、住宅地が並ぶ山麓の高台からの眺望も素晴らしいものです。')

# 北西部　画像
col1, col2, col3 = st.columns(3)
with col1:
    st.link_button('ラピュタの島・友ヶ島', 'https://www.wakayamakanko.com/sightseeing/nature2.html')
    st.image("area2_tomogashima_resize.jpg", use_column_width=True)

with col2:
    st.link_button("磯の浦海水浴場", 'https://www.isonoura-w.jp/')
    st.image("area2_isonoura.jpg", use_column_width=True)
    
with col3:
    st.link_button("無人島・沖ノ島", 'https://select.mujinto.jp/island/okinoshima_arida/')
    st.image("area2_okinoshima_resize.jpg", use_column_width=True)
st.divider()

# 北部　説明
st.subheader('③北部')
st.write('和歌山大学があり、大学を中心に住宅地や大規模商業施設が誕生し、新駅も設置されました。この周辺はまさに「新しい街」と言えるでしょう。新興住宅地として新たな住民を受け入れています。')

# 北部　画像
col1, col2, col3 = st.columns(3)
with col1:
    st.link_button('和歌山大学', 'https://www.wakayama-u.ac.jp/')
    st.image("area3_ wakayamauniv.jpg", use_column_width=True)

with col2:
    st.link_button("新駅・和歌山大学前駅", 'http://web.wakayama-u.ac.jp/station/')
    st.image("area3_wakayamaunivsta.jpg", use_column_width=True)
    
with col3:
    st.link_button("学園城郭都市ふじと台", 'https://www.fujitodai.com/')
    st.image("area3_fujitodai_resize.png", use_column_width=True)
st.divider()

# 北東部　説明
st.subheader('④北東部')
st.write('山から紀の川に向けた斜面では田園風景が広がり、のどかな農業地域の風景が広がっています。また、エリア中央部を熊野古道が通っており、古来から多くの人が往来した地域として栄えていたことがうかがわれます。')

# 北東部　画像
col1, col2, col3 = st.columns(3)
with col1:
    st.link_button('田園風景', 'http://www.city.wakayama.wakayama.jp/ijuteiju/1033810/1033763.html')
    st.image("area4_denen.png", use_column_width=True)

with col2:
    st.link_button("熊野古道", 'https://kinokawa-ryuiki.com/spot/rikishi-shrine/?course_id=74')
    st.image("area4_kumanokodou.jpg", use_column_width=True)
    
with col3:
    st.link_button("山口神社", 'https://momijiaoi.net/yamaguchi-ki/')
    st.image("area4_yamaguchishrine.jpg", use_column_width=True)
st.divider()

# 東部　説明
st.subheader('⑤東部')
st.write('紀の川の南側に位置する東西に長く平坦な地域です。熊野古道が地域を南北に貫き、街道沿いには集落があります。また古墳群なども発見されており、4世紀頃から人々の営みがあったと考えられています。')

# 東部　画像
col1, col2, col3 = st.columns(3)
with col1:
    st.link_button('松下幸之助生誕の地・松下公園', 'http://www.wakayama.tv/spot/matsushitapark/')
    st.image("area5_matsusitapark.jpg", use_column_width=True)

with col2:
    st.link_button("岩崎千塚古墳", 'http://wakayama-rekishi100.jp/story/004.html')
    st.image("area5_kofun.jpg", use_column_width=True)
    
with col3:
    st.link_button("水路", 'https://www.maff.go.jp/kinki/wakayamaheiya/wakayamaheiya03.html')
    st.image("area5_suiro.jpg", use_column_width=True)
st.divider()

# 南東部　説明
st.subheader('⑥南東部')
st.write('昔ながらの農村の風景が残る南東部。立派な家構えの民家や青石で作られた石垣など、昔ながらの豊かな農村の雰囲気が漂います。地域の神様や仏様も丁寧に祭られており、「古き良き時代のニッポン」を彷彿とさせます。')

# 南東部　画像
col1, col2, col3 = st.columns(3)
with col1:
    st.link_button('道の駅・四季の郷公園', 'https://fh-park.jp/')
    st.image("area6_shikinogokoen.jpg", use_column_width=True)

with col2:
    st.link_button("伊太祁曽神社", 'https://itakiso-jinja.net/')
    st.image("area6_itakiso.jpg", use_column_width=True)
    
with col3:
    st.link_button("山東まちづくり会", 'http://sandomachikai.ikora.tv/')
    st.image("area6_machiokoshi.jpg", use_column_width=True)
st.divider()


# 南部　説明
st.subheader('⑦南部')
st.write('南部エリアは、和歌の浦や雑賀崎といった海岸や漁港が主体となっているエリアです。万葉の時代からその美しさを称えられている和歌の浦はなんとも風光明媚。漁港のある雑賀崎なども特徴的な街並みが見られます。また、リゾート地であるマリーナシティなどもあります。')

# 南部　画像
col1, col2, col3 = st.columns(3)
with col1:
    st.link_button('日本のアマルフィ・雑賀崎', 'http://www.city.wakayama.wakayama.jp/kankou/kankouspot/1044909.html')
    st.image("area7_amalfi.png", use_column_width=True)

with col2:
    st.link_button("和歌の浦", 'https://wakanoura-nihonisan.jp/')
    st.image("area7_wakanoura.jpg", use_column_width=True)
    
with col3:
    st.link_button("浜の宮ビーチ", 'http://www.city.wakayama.wakayama.jp/kankou/nenkangyoji/1006624.html')
    st.image("area7_hamanomiya.jpg", use_column_width=True)
st.divider()