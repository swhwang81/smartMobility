import streamlit as st 

st.write('# 체질량 지수 계산기')

height = st.number_input('신장 (cm)',value = 160, step =5)
st.write(height,'cm')

weight = st.number_input('체중 (kg)', value = 50, step =5)
st.write(weight,'kg')

bmi = weight/((height/100)**2)

if st.button('계산'):
    st.write('당신의 체질량 지수는', round(bmi,2), '입니다.')
    

