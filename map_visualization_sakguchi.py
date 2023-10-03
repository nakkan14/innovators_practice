import streamlit as st
from streamlit_folium import st_folium
import folium
import pandas as pd

# ページ設定
st.set_page_config(
    page_title = "map",
    page_icon = "🗾",
    layout = "wide"
)

# 地図の中心の緯度/経度、タイル、初期のズームサイズを指定します。
m = folium.Map(
    # 地図の中心位置を和歌山市に指定
    location = [34.23058133009892, 135.1719684167173], 
    # タイル、アトリビュートの指定
    tiles = 'https://cyberjapandata.gsi.go.jp/xyz/pale/{z}/{x}/{y}.png',
    attr = 'Title、Facility',
    # ズームを指定
    zoom_start = 6
)

# 表示するデータを読み込み
df = pd.read_csv('いこーよ公園.csv')

# 読み込んだデータ(緯度・経度、ポップアップ用文字、アイコンを表示)
for i, row in df.iterrows():
    # ポップアップの作成(都道府県名＋都道府県庁所在地＋人口＋面積)
    pop = f"{row['title']}<br>{row['facility']}"
    folium.Marker(
        # 緯度と経度を指定
        location=[row['緯度'], row['経度']],
        # ツールチップの指定(都道府県名)
        tooltip=row['title'],
        # ポップアップの指定
        popup=folium.Popup(pop, max_width=300),
        # アイコンの指定(アイコン、色)
        icon=folium.Icon(icon="tree-conifer",icon_color="white", color="green")
    ).add_to(m)

st_data = st_folium(m, width=1200, height=800)