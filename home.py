import streamlit as st 

def bmi_range(bmi):
    if bmi>= 25:
        st.error("비만 입니다!")
    elif bmi >=23:
        st.warning('과체중 입니다!')
    elif bmi >= 18.5:
        st.success('정상 입니다!')
    else:
        st.warning('저체중 입니다!')

    


st.header('체질량 지수 계산기')

st.info('체질량지수는 자신의 몸무게를 키의 제곱으로 나눈 값입니다.')

height = st.number_input('신장 (cm)',value = 160, step =5)
st.write(height,'cm')

weight = st.number_input('체중 (kg)', value = 50, step =5)
st.write(weight,'kg')

bmi = weight/((height/100)**2)

if st.button('계산'):
    st.write('당신의 체질량 지수는', round(bmi,2), '입니다.')
    bmi_range(bmi)
    
    

    

