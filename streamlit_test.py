import streamlit as st
import pandas as pd
import altair as alt
import numpy as np

# st.button 생성#########################################
with st.container():
    st.header("1.st.button 생성")
    if st.button("Say hello"):
        st.write("Why hello there") # button 클릭 시 출력
    else:
        st.write("Goodbye") # button 미클릭 시 출력
st.markdown("---")
#########################################################

# st.write/text/markdown ################################
with st.container():
    st.header('2.st.write')
    st.write('Hello, *World!* :sunglasses:')
    st.write(1234)
    st.text("Hello, *World!* :sunglasses:")
    st.markdown("""
         # 제목 1
         ## **제목 2**
         ### *제목 3*
         > 이것은 인용문입니다.
         - [구글바로가기 링크](https://www.google.com)
         """)
st.markdown("---")
#########################################################

# st.write : DataFrame ##################################
with st.container():
    st.header("3.dataFrame")
    df = pd.DataFrame({
         '첫 번째 컬럼': [1, 2, 3, 4],
         '두 번째 컬럼': [10, 20, 30, 40]
         })
    st.write(df)
    st.write('아래는 DataFrame입니다.', df, '위는 dataframe입니다.')
st.markdown("---")
#########################################################

# alt.Chart ############################################# 
with st.container():
    st.header("altair")
    df2 = pd.DataFrame(
         np.random.randn(200, 3),
         columns=['a', 'b', 'c'])
    c = alt.Chart(df2).mark_circle().encode(
        x=alt.X('a', title='Xaxis'),
        y=alt.Y('b', title='Yaxis'),
        size=alt.Size('c', scale=alt.Scale(range=[50, 1000])),  # 크기 범위 조정
        color=alt.Color('c', scale=alt.Scale(scheme='viridis')),  # 색상 팔레트 'viridis'
        tooltip=[
            alt.Tooltip('a', title='X Value', format='.2f'),  # 툴팁에 제목 추가
            alt.Tooltip('b', title='Y Value', format='.2f'),
            alt.Tooltip('c', title='Size/Color', format='.2f')  # 소수점 2자리
        ]
    )
    st.write(c)
st.markdown("---")
#########################################################

# 화면에 코드 출력 ######################################
with st.container():
    st.text('화면에 코드 출력')
    st.code("""
         fruit = st.selectbox("좋아하는 과일을 선택하세요", ["사과", "바나나", "체리"])
         st.write("선택한 과일:", fruit)
    """, language="python")
st.markdown("---")

# Select Box 
with st.container():
    fruit = st.selectbox("좋아하는 과일을 선택하세요", ["사과", "바나나", "체리"])
    st.write("선택한 과일:", fruit)
    
    users = [{"id": 1, "name": "홍길동"}, {"id": 2, "name": "이몽룡"}]
    selected_user = st.selectbox(
        "사용자 선택",
        users,
        format_func=lambda x: f"{x['name']} (ID: {x['id']})"
    )
    st.write("선택한 사용자 ID:", selected_user['id'])
st.markdown("---")
#########################################################

# input 적용 ############################################
with st.container():
    name = st.text_input("이름을 입력하세요")  # 한줄 텍스트입력
    age = st.number_input("나이를 입력하세요", min_value=0, max_value=110) #숫자입력
    birthdate = st.date_input("생년월일 선택하세요") # 날짜 선택
    
    
    desc = st.text_area("하고싶은말 적으세요")   # 여러줄 텍스트입력  
    
    value = st.slider("나이", min_value=0, max_value=100, value=30, step=5)  # Slider로 숫자 선택 
    opt = st.selectbox("선택", ["A", "B", "C"]) # A,B,C중 선택
    opts = st.multiselect("복수 선택", ["A", "B", "C"]) # A,B,C중 다중선택
    gender = st.radio("선택", ["남자", "여자"]) # 둘중 하나 선택
    agree = st.checkbox("동의합니다") # 체크박스
    on = st.toggle("기능 활성화") # on/off설정
    
    time = st.time_input("시간 선택") # 시간 선택
    file = st.file_uploader("파일 업로드") 
    color = st.color_picker("색상", "#00f900")
    pw = st.text_input("비밀번호", type="password")
    
    if st.button("제출"):
        if not name:
            st.worning("이름을 입력하세요")
        elif not agree:
            st.error("동의가 필요합니다.")
        else:
            st.success("입력완료!!😊")
            st.subheader("입력내용 요약")
            st.write(f"이름:{name}")
            st.write(f"나이:{age}")
            st.write(f"성별:{gender}")
            st.write("**하고 싶은말**")
            st.info(desc if desc else "미작성")
st.markdown("---")
#########################################################

# 화면 분할 #############################################
with st.container():
    col1, col2 = st.columns([1,1]) # 1:1으로 화면 분할
    
    with col1:
        st.title("왼쪽")
    with col2:
        st.title("오른쪽")
        st.checkbox("우측 체크박스 1")
    # with 대신 사용
    col1.subheader("Left")
    col2.checkbox("Right checkbox")
st.markdown("---")

# tab 
with st.container():
    tab1, tab2 = st.tabs(['Tab A','Tab B']) # 1:1으로 화면 분할
    
    with tab1:
        st.write("왼쪽탭")
    with tab2:
        st.write("오른쪽탭")
    # side bar 
    st.sidebar.title("사이드바")
    st.sidebar.checkbox("체크박스 추가")
st.markdown("---")
#########################################################

# Expander ##############################################
with st.container():
    st.title("😊Example")
    
    # 설명 숨기기
    with st.expander("설명보기"):
        st.write("""
                 설명 숨기기
                 """)
        
    # 여러줄 텍스트입력
    with st.expander("메모입력"):
        note = st.text_area("여기에 메모하면 note로 저장됨")
    
    # DataFrame 숨기기
    df = pd.DataFrame({
        "과목": ['국', '영','수'],
        "점수":[100,80,90]
    })
    with st.expander("df"):
        st.dataframe(df)
st.markdown("---")
#########################################################

# 레이아웃 작성 #########################################
# sidebar, slider
with st.container():
    st.sidebar.title("sidebar의 slider")
    slide_val = st.sidebar.slider("값 선택", 0, 100, 35) #(값선택, min, max, default값)
    
    # tab
    tab1, tab2, tab3 = st.tabs(['AAA', 'BBB', 'CCC'])
    
    with tab1:
        st.write("AAA 상세내용")
    
        # 2*2 lay out
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### layout 1")
            st.info(f"slider value: {slide_val}")
        with col2:
            st.markdown("### layout 2")
            st.info("1사분면")
        col3, col4 = st.columns(2)
        with col3:
            st.markdown("### layout 3")
            st.info("3사분면")
        with col4:
            st.markdown("### layout 4")
            st.info("4사분면")
    with tab2:
        st.write("tab2")
    with tab3:
        st.write("Tab3")
st.markdown("---")
#########################################################

# select box ############################################
with st.container():
    users = [{"id": 1, "name": "김oo"}, {"id": 2, "name": "이oo"}]
    selected_user = st.selectbox(
        "사용자 선택", users,
        format_func=lambda x: f"{x['name']} (ID: {x['id']})"
    )
    st.write("선택한 사용자 ID:", selected_user['id'])
st.markdown("---")
#########################################################

# multi select box #######################################
with st.container():
    data = {
        "행정구역": ['서울', '경기', '부산', '인천'],
        "인구수":[950,1050,300,320]
    }
    df = pd.DataFrame(data)
    
    region_list = sorted(df['행정구역'].unique()) # multi select box선택시 보이는 정보 
    
    selected_regions = st.multiselect(
        "지역을 선택하세요",
        options=region_list,
        default = ['서울'] # default 설정
    )

    # multi select box 선택 결과 필터링
    filtered_df = df[df['행정구역'].isin(selected_regions)]
    st.write("선택된 지역 정보: ")
    st.dataframe(filtered_df)

st.markdown("---")
#########################################################

# radio button ##########################################
with st.container():
    gender = st.radio(
        "성별을 선택하세요", 
        ['남', '녀'],
        index=0 # default=남
    )
    st.write('선택한 성별', gender)

    color = st.radio(
        '선호하는 색을 고르세요',
        options=['black','red','blue','white'],
        index=0 # default=black
    )
    st.success(f"선택 색상 : {color}")
st.markdown("---")
#########################################################

# data editor#############################################
with st.container():
    df = pd.DataFrame({
        "이름": ["김ㅇㅇ", "이ㅇㅇ"],
        "나이": [30, 25]
    })
    
    edited_df = st.data_editor(df)
    st.write("수정된 데이터:")
    st.dataframe(edited_df)
st.markdown("---")
#########################################################

# file uploader ##########################################
with st.container():
    uploaded_file = st.file_uploader("csv파일을 업로드하세요", type="csv")
    if uploaded_file:
        # 파일 확장자 확인
        if uploaded_file.name.endswith(".csv"):
            try:
                df = pd.read_csv(uploaded_file)
                st.dataframe(df.head(5)) # 첫 5개행만 노춯
            except Exception as e:
                st.error(f"csv파일을 읽는 중 오류가 발생 : {str(e)}")
        else:
            st.error("업로드된 파일이 csv형식이 아닙니다. csv파일을 업로드하세요.")
st.markdown("---")
#########################################################