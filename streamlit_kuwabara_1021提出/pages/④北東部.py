import streamlit as st
from streamlit_folium import st_folium
import folium
import pandas as pd
import base64

st.set_page_config(
    page_title='トカイナカLIFE・④北東部',
    page_icon='🍊',
    layout="wide",
    initial_sidebar_state="auto"
)

st.title("④北東部から探す")

# 画像をBase64形式にエンコードする関数
def get_image_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# エンコード対象のアイコンとその名称
icons = ["物件", "公園", "小学校", "保育園", "幼稚園", "習い事", "スーパー", "コンビニ", "病院"]

# 各画像をBase64形式にエンコード
encoded_icons = {icon: get_image_base64(f"icon_{icon}.png") for icon in icons}

# 各テキストとアイコン画像をHTMLタグで作成して、連結
display_html = " ".join([f'<img src="data:image/png;base64,{encoded}" style="display:inline; vertical-align:middle; width:30px;"/> {icon}' for icon, encoded in encoded_icons.items()])

# 作成したHTMLを表示
st.markdown(display_html, unsafe_allow_html=True)

# 表示するデータを読み込み
df = pd.read_csv('物件.csv')
df_park = pd.read_csv('公園.csv')
df_school = pd.read_csv('小学校.csv')
df_nursery = pd.read_csv('保育園.csv')
df_kindergarten = pd.read_csv('幼稚園.csv')
df_lesson=pd.read_csv('習い事.csv')
df_supermarket = pd.read_csv('スーパー.csv')
df_store = pd.read_csv('コンビニ.csv')
df_hospital = pd.read_csv('病院.csv')

# 地区ブロックの設定
block_code = 4
dataframes = [df, df_park, df_school, df_nursery, df_kindergarten, df_lesson, df_store]
filtered_dataframes = [df[df['地区_コード'] == block_code] for df in dataframes]
df, df_park, df_school, df_nursery, df_kindergarten, df_lesson, df_store= filtered_dataframes

df_hospital = df_hospital[df_hospital['Block'] == '北東部地域']
df_supermarket = df_supermarket[df_supermarket['Block'] == '北東部地域']

# 地図の基本設定⇒locationを地区ブロックごとに調整する
m = folium.Map(
    location=[34.2620844809058, 135.23838779432683],
    tiles='OpenStreetMap',
    zoom_start=14
)

# 地図表示のサイドバー
with st.sidebar:
    st.header('地図の表示')
    # チェックボックスを作成
    show_parks = st.sidebar.checkbox('公園を表示する', value=True)
    show_schools = st.sidebar.checkbox('小学校を表示する', value=True)
    show_nurseries =st.sidebar.checkbox('保育園を表示する', value=False)
    show_kindergartens = st.sidebar.checkbox('幼稚園を表示する', value=False)
    show_lessons = st.sidebar.checkbox('習い事を表示する', value=False)
    if show_lessons:
    # df_lessonのカラムから'習い事_ジャンル_'というプレフィックスを持つカラム名を取得
        columns = [col for col in df_lesson.columns if '習い事_ジャンル_' in col]
    # 冗長な部分を取り除く
        shortened_names = [col.split('_')[-1] for col in columns]
    # Streamlitのマルチセレクトボックスに表示
        selected_lessons = st.sidebar.multiselect('ジャンルを選択してください:', shortened_names)
    
    show_supermarkets = st.sidebar.checkbox('スーパーを表示する', value=False)
    show_stores = st.sidebar.checkbox('コンビニを表示する', value=False)
    show_hospitals = st.sidebar.checkbox('病院を表示する', value=False)
    show_homes = st.sidebar.checkbox('物件を表示する', value=True)


# 検索条件のサイドバー
with st.sidebar:
    st.header('検索条件')

    st.subheader('アソビ')
    park = st.checkbox('公園')
    if park:
        min_distance_park, max_distance_park = st.sidebar.slider(
            '物件から公園までの距離 (m)', 
            int(df['公園_最寄り_距離_m'].min()), 
            int(df['公園_最寄り_距離_m'].max()),
            (0, 1500)
            )
    else:
        # 公園のチェックがない場合は、距離フィルターを無視するための最大と最小値を設定
        min_distance_park = 0
        max_distance_park = float('inf')

    st.subheader('マナビ')
    school = st.checkbox('小学校')
    if school:
        min_distance_school, max_distance_school = st.sidebar.slider(
            '物件から小学校までの距離 (m)', 
            int(df['小学校_最寄り_距離_m'].min()), 
            int(df['小学校_最寄り_距離_m'].max()),
            (0, 1200)
            )
        min_students, max_students = st.sidebar.slider(
            '最寄りの小学校の生徒数',
            int(df['小学校_生徒数_人'].min()), 
            int(df['小学校_生徒数_人'].max()),
            (0, 800)
            )
    else:
        # 小学校のチェックがない場合は、距離フィルターを無視するための最大と最小値を設定
        min_distance_school = 0
        max_distance_school = float('inf')
        min_students = 0
        max_students = float('inf')
    
    nursery = st.checkbox('保育園')
    if nursery:
        min_distance_nursery, max_distance_nursery = st.sidebar.slider(
            '物件から保育園までの距離 (m)', 
            int(df['保育園_最寄り_距離_m'].min()), 
            int(df['保育園_最寄り_距離_m'].max()),
            (0, 3800)
            )
    else:
        # 保育園のチェックがない場合は、距離フィルターを無視するための最大と最小値を設定
        min_distance_nursery = 0
        max_distance_nursery = float('inf')

    kindergarten = st.checkbox('幼稚園')
    if kindergarten:
        min_distance_kindergarten, max_distance_kindergarten = st.sidebar.slider(
            '物件から幼稚園までの距離 (m)', 
            int(df['幼稚園_最寄り_距離_m'].min()), 
            int(df['幼稚園_最寄り_距離_m'].max()),
            (0, 3800)
            )
    else:
        # 幼稚園のチェックがない場合は、距離フィルターを無視するための最大と最小値を設定
        min_distance_kindergarten = 0
        max_distance_kindergarten = float('inf')

    st.subheader('生活')
    supermarket = st.checkbox('スーパー')
    if supermarket:
        min_distance_supermarket, max_distance_supermarket = st.sidebar.slider(
            '物件からスーパーまでの距離 (m)', 
            int(df['スーパー_最寄り_距離_m'].min()), 
            int(df['スーパー_最寄り_距離_m'].max()),
            (0, 2000)
            )
    else:
        # スーパーのチェックがない場合は、距離フィルターを無視するための最大と最小値を設定
        min_distance_supermarket = 0
        max_distance_supermarket = float('inf')

    store = st.checkbox('コンビニ')
    if store:
        min_distance_store, max_distance_store = st.sidebar.slider(
            '物件からコンビニまでの距離 (m)', 
            int(df['コンビニ_最寄り_距離_m'].min()), 
            int(df['コンビニ_最寄り_距離_m'].max()),
            (0, 2000)
            )
    else:
        # コンビニのチェックがない場合は、距離フィルターを無視するための最大と最小値を設定
        min_distance_store = 0
        max_distance_store = float('inf')

    hospital = st.checkbox('病院')
    if hospital:
        min_distance_hospital, max_distance_hospital = st.sidebar.slider(
            '物件から病院までの距離 (m)', 
            int(df['病院_最寄り_距離_m'].min()), 
            int(df['病院_最寄り_距離_m'].max()),
            (0, 2000)
            )
    else:
        # 病院のチェックがない場合は、距離フィルターを無視するための最大と最小値を設定
        min_distance_hospital = 0
        max_distance_hospital= float('inf')

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
            (0.0,70.0),
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
            (0.0,25.0),
            step=0.1
            )
    else:
        min_rent = 0
        max_rent = float('inf')

# チェックボックスの状態に応じて公園を地図上に表示
if show_parks:
    for i, row in df_park.iterrows():
        pop = f"{row['公園_公園名']}<br>{row['公園_施設']}"
        folium.Marker(
            location=[row['公園_緯度'], row['公園_経度']],
            tooltip=row['公園_公園名'],
            popup=folium.Popup(pop, max_width=300),
            icon=folium.Icon(icon="tree-conifer", icon_color="white", color="green")
        ).add_to(m)

# チェックボックスの状態に応じて小学校を地図上に表示
if show_schools:
    for i, row in df_school.iterrows():
        pop_content = f"{row['小学校_学校名']}<br>生徒数：{row['小学校_生徒数']}<br><a href='{row['小学校_URL']}' target='_blank'>小学校 Website</a>"
        folium.Marker(
            location=[row['小学校_緯度'], row['小学校_経度']],
            tooltip=row['小学校_学校名'],
            popup=folium.Popup(pop_content, max_width=300),
            icon=folium.Icon(icon="pencil", icon_color="white", color="blue")
        ).add_to(m)

# チェックボックスの状態に応じて保育園を地図上に表示
if show_nurseries:
    for i, row in df_nursery.iterrows():
        pop_content = f"{row['保育園_園名']}<br><a href='{row['保育園_URL']}' target='_blank'>保育園 Website</a>"
        folium.Marker(
            location=[row['保育園_緯度'], row['保育園_経度']],
            tooltip=row['保育園_園名'],
            popup=folium.Popup(pop_content, max_width=300),
            icon=folium.Icon(icon="bell", icon_color="white", color="pink")
        ).add_to(m)

# チェックボックスの状態に応じて幼稚園を地図上に表示
if show_kindergartens:
    for i, row in df_kindergarten.iterrows():
        pop_content = f"{row['幼稚園_園名']}<br><a href='{row['幼稚園_URL']}' target='_blank'>保育園 Website</a>"
        folium.Marker(
            location=[row['幼稚園_緯度'], row['幼稚園_経度']],
            tooltip=row['幼稚園_園名'],
            popup=folium.Popup(pop_content, max_width=300),
            icon=folium.Icon(icon="bell", icon_color="white", color="purple")
        ).add_to(m)

# チェックボックスの状態に応じて習い事を地図上に表示
if show_lessons:
    # 選択されたジャンルのフルカラム名を取得
    selected_lessons_full_columns = ["習い事_ジャンル_" + genre for genre in selected_lessons]

    # 選択されたジャンルに応じてdf_lessonからデータをフィルタリング
    filtered_lesson_df = df_lesson[df_lesson[selected_lessons_full_columns].any(axis=1)]

    for i, row in filtered_lesson_df.iterrows():
        pop = f"{row['習い事_教室名']}<br><a href='{row['習い事_URL']}' target='_blank'>習い事 Website</a>"
        folium.Marker(
            location=[row['習い事_経度'], row['習い事_緯度']],
            tooltip=row['習い事_教室名'],
            popup=folium.Popup(pop, max_width=300),
            icon=folium.Icon(icon="dashboard", icon_color="white", color="orange")
        ).add_to(m)

# チェックボックスの状態に応じてスーパーマーケットを地図上に表示
if show_supermarkets:
    for i, row in df_supermarket.iterrows():
        pop_content = f"{row['title']}"
        folium.Marker(
            location=[row['longitude'], row['latitude']],
            tooltip=row['title'],
            popup=folium.Popup(pop_content, max_width=300),
            icon=folium.Icon(icon="shopping-cart", icon_color="white", color="lightred")
        ).add_to(m)

# チェックボックスの状態に応じてコンビニを地図上に表示
if show_stores:
    for i, row in df_store.iterrows():
        pop_content = f"{row['コンビニ_店舗']}"
        folium.Marker(
            location=[row['コンビニ_緯度'], row['コンビニ_経度']],
            tooltip=row['コンビニ_店舗'],
            popup=folium.Popup(pop_content, max_width=300),
            icon=folium.Icon(icon="inbox", icon_color="white", color="beige")
        ).add_to(m)

# チェックボックスの状態に応じて病院を地図上に表示
if show_hospitals:
    for i, row in df_hospital.iterrows():
        pop_content = f"{row['title']}"
        folium.Marker(
            location=[row['longitude'], row['latitude']],
            tooltip=row['title'],
            popup=folium.Popup(pop_content, max_width=300),
            icon=folium.Icon(icon="plus", icon_color="red", color="white")
        ).add_to(m)

# フィルタリング (物件のみ)
filtered_df = df[(df['公園_最寄り_距離_m'] >= min_distance_park) & (df['公園_最寄り_距離_m'] <= max_distance_park)]
filtered_df = filtered_df[(filtered_df['小学校_最寄り_距離_m'] >= min_distance_school) & (filtered_df['小学校_最寄り_距離_m'] <= max_distance_school)]
filtered_df = filtered_df[(filtered_df['小学校_生徒数_人'] >= min_students) & (filtered_df['小学校_生徒数_人'] <= max_students)]
filtered_df = filtered_df[(filtered_df['保育園_最寄り_距離_m'] >= min_distance_nursery) & (filtered_df['保育園_最寄り_距離_m'] <= max_distance_nursery)]
filtered_df = filtered_df[(filtered_df['幼稚園_最寄り_距離_m'] >= min_distance_kindergarten) & (filtered_df['幼稚園_最寄り_距離_m'] <= max_distance_kindergarten)]
filtered_df = filtered_df[(filtered_df['スーパー_最寄り_距離_m'] >= min_distance_supermarket) & (filtered_df['スーパー_最寄り_距離_m'] <= max_distance_supermarket)]
filtered_df = filtered_df[(filtered_df['コンビニ_最寄り_距離_m'] >= min_distance_store) & (filtered_df['コンビニ_最寄り_距離_m'] <= max_distance_store)]
filtered_df = filtered_df[(filtered_df['病院_最寄り_距離_m'] >= min_distance_hospital) & (filtered_df['病院_最寄り_距離_m'] <= max_distance_hospital)]
filtered_df = filtered_df[(filtered_df['物件_面積_m2'] >= min_size) & (filtered_df['物件_面積_m2'] <= max_size)]
filtered_df = filtered_df[(filtered_df['物件_築年数_年'] >= min_years) & (filtered_df['物件_築年数_年'] <= max_years)]
filtered_df = filtered_df[(filtered_df['物件_家賃_万円'] >= min_rent) & (filtered_df['物件_家賃_万円'] <= max_rent)]

# 選択された間取りを使用してデータフレームをフィルタリング
filtered_df = filtered_df[filtered_df['物件_間取'].isin(selected_layouts)]
filtered_df = filtered_df[filtered_df['物件_カテゴリ'].isin(selected_type)]

# 物件数を計算
property_count = len(filtered_df)

st.header(f"（物件数：{property_count}件）")

# チェックボックスの状態に応じて物件を地図上に表示
if show_homes:
    for i, row in filtered_df.iterrows():
        pop_content = f"{row['物件_物件名']}<br>種別：{row['物件_カテゴリ']}<br>築年数：{row['物件_築年数_年']}<br>間取り：{row['物件_間取']}<br>広さ：{row['物件_面積_m2']}<br>家賃：{row['物件_家賃_万円']}<br><a href='{row['物件_URL']}' target='_blank'>物件Website</a>"
        folium.Marker(
            location=[row['物件_緯度'], row['物件_経度']],
            tooltip=row['物件_物件名'],
            popup=folium.Popup(pop_content, max_width=300),
            icon=folium.Icon(icon="home", icon_color="white", color="red")
        ).add_to(m)

# 完成したマップをStreamlitに表示
st_folium(m, width=1200, height=800)
