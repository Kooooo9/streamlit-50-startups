import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def run_eda():
    st.header("EDA - 데이터 탐색")
    st.markdown("`data/50_Startups.csv` 파일을 로드하여 변수별 분포와 통계, 상관관계 등을 탐색합니다.")

    df = pd.read_csv("data/50_Startups.csv")

    st.subheader("원본 데이터 샘플")
    st.dataframe(df.head())

    st.subheader("기본 정보")
    col1, col2 = st.columns(2)
    with col1:
        st.write("행 수, 열 수:")
        st.write(df.shape)
        st.write("데이터 타입:")
        st.write(df.dtypes)
    with col2:
        st.write("결측치 개수:")
        st.write(df.isnull().sum())

    st.subheader("수치형 변수 기술 통계")
    st.write(df.select_dtypes(include=['number']).describe().T)

    # 상태별 요약
    st.subheader("State별 Profit 요약")
    st.write(df.groupby('State')['Profit'].agg(['count','mean','std','min','max']).round(2))

    # 컬럼 선택 기반 시각화
    st.subheader("변수별 분포 시각화")
    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
    col_x = st.selectbox('히스토그램/박스플롯으로 볼 열을 선택하세요', numeric_cols, index=0)

    bins = st.slider('히스토그램 빈(bin) 수', min_value=5, max_value=100, value=30)
    fig1, ax1 = plt.subplots(1,2, figsize=(10,4))
    sns.histplot(df[col_x], bins=bins, kde=True, ax=ax1[0])
    ax1[0].set_title(f'{col_x} 분포')
    sns.boxplot(x=df[col_x], ax=ax1[1])
    ax1[1].set_title(f'{col_x} 박스플롯')
    st.pyplot(fig1)

    # 산점도: 선택한 x,y
    st.subheader("산점도 (변수 간 관계)")
    x_col = st.selectbox('X 축', numeric_cols, index=0, key='x_col')
    y_col = st.selectbox('Y 축', numeric_cols, index=3 if len(numeric_cols)>3 else 1, key='y_col')
    hue_col = st.selectbox('색상 기준 (옵션)', ['None'] + df.columns.tolist(), index=0)

    fig2, ax2 = plt.subplots()
    if hue_col == 'None':
        sns.scatterplot(data=df, x=x_col, y=y_col, ax=ax2)
    else:
        sns.scatterplot(data=df, x=x_col, y=y_col, hue=df[hue_col], ax=ax2)
    ax2.set_xlabel(x_col)
    ax2.set_ylabel(y_col)
    st.pyplot(fig2)

    # 상관행렬
    st.subheader("수치형 변수 상관관계")
    corr = df.select_dtypes(include=['number']).corr()
    fig3, ax3 = plt.subplots(figsize=(6,4))
    sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', ax=ax3)
    st.pyplot(fig3)

    # State 필터링 및 다운로드
    st.subheader("데이터 필터링 및 다운로드")
    states = ['All'] + df['State'].unique().tolist()
    sel_state = st.selectbox('State로 필터링', states)
    if sel_state == 'All':
        filtered = df.copy()
    else:
        filtered = df[df['State'] == sel_state]

    st.write(f'필터된 데이터 행 수: {filtered.shape[0]}')
    st.dataframe(filtered.head(50))

    csv = filtered.to_csv(index=False).encode('utf-8')
    st.download_button('필터된 데이터 다운로드 (CSV)', csv, file_name='50_Startups_filtered.csv', mime='text/csv')

    st.markdown('---')
    st.info('참고: ML 탭에서 모델 학습/예측을 실행하세요.')
