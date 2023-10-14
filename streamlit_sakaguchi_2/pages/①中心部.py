import streamlit as st
from streamlit_folium import st_folium
import folium
import pandas as pd

st.title("①中心部から探す")

# 表示するデータを読み込み
original_df = pd.read_csv('20231012_SUUMO_和歌山市賃貸_最寄り施設_詳細_改訂.csv')
df = original_df[original_df['地区_ブロック'] == '中心部地域']

# 地図の基本設定⇒locationを地区ブロックごとに調整する
m = folium.Map(
    location=[34.22294511274448, 135.18994329478005],
    tiles='OpenStreetMap',
    zoom_start=14
)

# 地図表示のサイドバー
with st.sidebar:
    st.header('地図の表示')
    # チェックボックスを作成
    show_schools = st.sidebar.checkbox('小学校を表示する', value=True)
    show_parks = st.sidebar.checkbox('公園を表示する', value=True)
    show_homes = st.sidebar.checkbox('物件を表示する', value=True)

# 検索条件のサイドバー
with st.sidebar:
    st.header('検索条件')

    st.subheader('アソビ')
    park = st.checkbox('公園')
    if park:
        min_distance_park, max_distance_park = st.sidebar.slider(
            '公園からの距離 (m)', 
            int(df['公園_最寄り_距離_m'].min()), 
            int(df['公園_最寄り_距離_m'].max()),
            (0, 1500)
            )
    else:
        # parkのチェックがない場合は、公園の距離フィルターを無視するための最大と最小値を設定
        min_distance_park = 0
        max_distance_park = float('inf')

    st.subheader('マナビ')
    school = st.checkbox('小学校')
    if school:
        min_distance_school, max_distance_school = st.sidebar.slider(
            '小学校からの距離 (m)', 
            int(df['小学校_最寄り_距離_m'].min()), 
            int(df['小学校_最寄り_距離_m'].max()),
            (0, 1200)
            )
        min_students, max_students = st.sidebar.slider(
            '小学校の生徒数',
            int(df['小学校_生徒数_人'].min()), 
            int(df['小学校_生徒数_人'].max()),
            (0, 800)
            )
    else:
        # schoolのチェックがない場合は、公園の距離フィルターを無視するための最大と最小値を設定
        min_distance_school = 0
        max_distance_school = float('inf')
        min_students = 0
        max_students = float('inf')
    
    st.subheader('物件')
    
    type = st.checkbox('タイプ')
    if type:
        # 使用されている全てのタイプの一覧を取得
        unique_type = df['物件_カテゴリ'].unique().tolist()
        # それらのタイプをStreamlitのサイドバーにマルチセレクトボックスとして表示
        selected_type = st.sidebar.multiselect(
            'タイプを選択',
            unique_type,
            default=unique_type
            )
    else:
        selected_type = df['物件_カテゴリ'].unique().tolist()
        
    layout = st.checkbox('間取り')
    if layout:
        # 使用されている全ての間取りの一覧を取得
        unique_layouts = df['物件_間取'].unique().tolist()
        # それらの間取りをStreamlitのサイドバーにマルチセレクトボックスとして表示
        selected_layouts = st.sidebar.multiselect(
            '間取りを選択',
            unique_layouts,
            default=unique_layouts
            )
    else:
        selected_layouts = df['物件_間取'].unique().tolist()
        
    size = st.checkbox('広さ')
    if size:
        min_size, max_size = st.sidebar.slider(
            '物件の広さを設定',
            float(df['物件_面積_m2'].min()), 
            float(df['物件_面積_m2'].max()),
            (80.0, 160.0),
            step=0.1   # stepをfloat型にする
            )
    else:
        min_size = 0
        max_size = float('inf')
        
    years = st.checkbox('築年数')
    if years:
        min_years, max_years = st.sidebar.slider(
            '築年数を設定',
            float(df['物件_築年数_年'].min()), 
            float(df['物件_築年数_年'].max()),
            (0.0,30.0),
            step=0.1
            )
    else:
        min_years = 0
        max_years = float('inf')
    
    rent = st.checkbox('家賃')
    if rent:
        min_rent, max_rent = st.sidebar.slider(
            '家賃を設定',
            float(df['物件_家賃_万円'].min()), 
            float(df['物件_家賃_万円'].max()),
            (0.0,15.0),
            step=0.1
            )
    else:
        min_rent = 0
        max_rent = float('inf')

              
        

# チェックボックスの状態に応じて小学校を地図上に表示
if show_schools:
    for i, row in df.iterrows():
        pop_content = f"{row['小学校_最寄り']}<br>生徒数：{row['小学校_生徒数_人']}<br><a href='{row['小学校_URL']}' target='_blank'>School Website</a>"
        folium.Marker(
            location=[row['小学校_緯度'], row['小学校_経度']],
            tooltip=row['小学校_最寄り'],
            popup=folium.Popup(pop_content, max_width=300),
            icon=folium.Icon(icon="pencil", icon_color="white", color="blue")
        ).add_to(m)

# チェックボックスの状態に応じて公園を地図上に表示
if show_parks:
    for i, row in df.iterrows():
        pop = f"{row['公園_最寄り']}<br>{row['公園_設備']}"
        folium.Marker(
            location=[row['公園_緯度'], row['公園_経度']],
            tooltip=row['公園_最寄り'],
            popup=folium.Popup(pop, max_width=300),
            icon=folium.Icon(icon="tree-conifer", icon_color="white", color="green")
        ).add_to(m)


# フィルタリング (物件のみ)
filtered_df = df[(df['小学校_最寄り_距離_m'] >= min_distance_school) & (df['小学校_最寄り_距離_m'] <= max_distance_school)]
filtered_df = filtered_df[(filtered_df['小学校_生徒数_人'] >= min_students) & (filtered_df['小学校_生徒数_人'] <= max_students)]
filtered_df = filtered_df[(filtered_df['公園_最寄り_距離_m'] >= min_distance_park) & (filtered_df['公園_最寄り_距離_m'] <= max_distance_park)]
filtered_df = filtered_df[(filtered_df['物件_面積_m2'] >= min_size) & (filtered_df['物件_面積_m2'] <= max_size)]
filtered_df = filtered_df[(filtered_df['物件_築年数_年'] >= min_years) & (filtered_df['物件_築年数_年'] <= max_years)]
filtered_df = filtered_df[(filtered_df['物件_家賃_万円'] >= min_rent) & (filtered_df['物件_家賃_万円'] <= max_rent)]

# 選択された間取りを使用してデータフレームをフィルタリング
filtered_df = filtered_df[filtered_df['物件_間取'].isin(selected_layouts)]
filtered_df = filtered_df[filtered_df['物件_カテゴリ'].isin(selected_type)]

# チェックボックスの状態に応じて物件を地図上に表示
if show_homes:
    for i, row in filtered_df.iterrows():
        pop_content = f"{row['物件_物件名']}<br>築年数：{row['物件_築年数_年']}<br>間取り：{row['物件_間取']}<br>広さ：{row['物件_面積_m2']}<br>家賃：{row['物件_家賃_万円']}<br><a href='{row['物件_URL']}' target='_blank'>物件Website</a>"
        folium.Marker(
            location=[row['物件_緯度'], row['物件_経度']],
            tooltip=row['物件_物件名'],
            popup=folium.Popup(pop_content, max_width=300),
            icon=folium.Icon(icon="home", icon_color="white", color="red")
        ).add_to(m)

# 完成したマップをStreamlitに表示
st_folium(m, width=800, height=800)
