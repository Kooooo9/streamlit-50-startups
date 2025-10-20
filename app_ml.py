import streamlit as st
import joblib 
import pandas as pd

def run_ml() :
    st.subheader('수익 예측')
    st.info('아래 데이터를 넣으시면, 수익을 예측합니다.')

    rnd = st.number_input('연구개발비', min_value=0)
    admin = st.number_input('운영비', min_value=10000)
    marketing = st.number_input('마케팅비', min_value=0)
    state = st.radio('주 선택', ['California','Florida','New York' ] ) 

    if st.button('수익예측') :
        pipe = joblib.load('./model/pipe.pkl')

        new_data = [{'R&D Spend':rnd , 'Administration':admin, 'Marketing Spend':marketing, 'State':state}]

        df_new = pd.DataFrame(data= new_data)

        y_pred = pipe.predict(df_new)

        y_pred = y_pred[0]

        st.info( '예상 수익은 ' + format( round(y_pred) , ',' ) + '달러 입니다')

        


