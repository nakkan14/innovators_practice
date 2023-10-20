import streamlit as st
from streamlit_folium import st_folium
import folium
import pandas as pd

# ページ設定
st.set_page_config(
    page_title="map",
    page_icon="🗾",
    layout="wide"
)

# チェックボックスを作成
show_schools = st.sidebar.checkbox('小学校を表示する', value=True)
show_parks = st.sidebar.checkbox('公園を表示する', value=True)

# 地図の基本設定
m = folium.Map(
    location=[34.23058133009892, 135.1719684167173],
    tiles='https://cyberjapandata.gsi.go.jp/xyz/pale/{z}/{x}/{y}.png',
    attr='国土地理院',
    zoom_start=12
)

# チェックボックスの状態に応じて小学校を地図上に表示
if show_schools:
    df_school = pd.read_csv('20231004_和歌山市小学校_スクレイピング_経度緯度追加.csv')
    for i, row in df_school.iterrows():
        pop_content = f"{row['School_Name']}<br>生徒数：{row['Stu_Number']}<br><a href='{row['url']}' target='_blank'>School Website</a>"
        folium.Marker(
            location=[row['longitude'], row['latitude']],
            tooltip=row['School_Name'],
            popup=folium.Popup(pop_content, max_width=300),
            icon=folium.Icon(icon="pencil", icon_color="white", color="blue")
        ).add_to(m)

# チェックボックスの状態に応じて公園を地図上に表示
if show_parks:
    df_park = pd.read_csv('いこーよ公園.csv')
    for i, row in df_park.iterrows():
        pop = f"{row['title']}<br>{row['facility']}"
        folium.Marker(
            location=[row['緯度'], row['経度']],
            tooltip=row['title'],
            popup=folium.Popup(pop, max_width=300),
            icon=folium.Icon(icon="tree-conifer", icon_color="white", color="green")
        ).add_to(m)

# 完成したマップをStreamlitに表示
st_folium(m, width=1200, height=800)
