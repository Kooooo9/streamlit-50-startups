import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def run_home():
    st.header("Home - 스타트업 수익 예측 앱")
    st.markdown(
        "이 앱은 `data/50_Startups.csv` 데이터를 사용해 스타트업의 수익을 예측합니다.\n\n" 
        "여기서는 데이터 미리보기, 기술 통계, 변수 간 상관관계와 간단한 시각화를 제공합니다.")

    # 데이터 로드
    df = pd.read_csv("data/50_Startups.csv")

    st.subheader("데이터 샘플")
    st.write(df.head())

    st.subheader("기본 정보")
    st.write(df.describe().T)

    # State 컬럼 분포
    st.subheader("State 분포")
    state_counts = df['State'].value_counts()
    st.bar_chart(state_counts)

    # 산점도: R&D Spend vs Profit, Marketing Spend vs Profit
    st.subheader("R&D Spend / Marketing Spend 와 Profit 관계")
    col1, col2 = st.columns(2)
    with col1:
        fig1, ax1 = plt.subplots()
        sns.scatterplot(data=df, x='R&D Spend', y='Profit', hue='State', ax=ax1)
        ax1.set_xlabel('R&D Spend')
        ax1.set_ylabel('Profit')
        st.pyplot(fig1)
    with col2:
        fig2, ax2 = plt.subplots()
        sns.scatterplot(data=df, x='Marketing Spend', y='Profit', hue='State', ax=ax2)
        ax2.set_xlabel('Marketing Spend')
        ax2.set_ylabel('Profit')
        st.pyplot(fig2)

    # 상관행렬
    st.subheader("수치형 변수 상관관계")
    num_df = df.select_dtypes(include=['number'])
    corr = num_df.corr()
    fig3, ax3 = plt.subplots()
    sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', ax=ax3)
    st.pyplot(fig3)

    # 간단한 사용자 입력 예시 (predictor) - 값은 기본 설명용
    st.subheader("간단한 예측 입력 예시")
    r_and_d = st.number_input('R&D Spend', value=100000.0, step=1000.0)
    administration = st.number_input('Administration', value=120000.0, step=1000.0)
    marketing = st.number_input('Marketing Spend', value=200000.0, step=1000.0)
    state = st.selectbox('State', options=df['State'].unique())

    st.markdown("실제 모델은 'ML' 탭에서 실행됩니다. 여기는 예시 입력만 제공합니다.")
    if st.button('입력 값 요약 보기'):
        st.write({
            'R&D Spend': r_and_d,
            'Administration': administration,
            'Marketing Spend': marketing,
            'State': state
        })

    # 파일 다운로드
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(label='데이터 다운로드 (CSV)', data=csv, file_name='50_Startups_sample.csv', mime='text/csv')
