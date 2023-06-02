import streamlit as st 
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt

def bmi_range(bmi):
    if bmi>= 25:
        st.error("비만 입니다!")
    elif bmi >=23:
        st.warning('과체중 입니다!')
    elif bmi >= 18.5:
        st.success('정상 입니다!')
    else:
        st.warning('저체중 입니다!')


selected = st.sidebar.selectbox(
    "목차",
    ("체질량 계산기", "갭마인더", "마이페이지")
)

if selected =='체질량 계산기':

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
        
        
    image = Image.open('vegetables.jpg')

    st.image(image, caption='eat a lot of vegetables!')
        
elif selected == '갭마인더':
    st.header('Gapminder 분석')

    st.write('파일 읽어오기 ')

    data = pd.read_csv('gapminder.csv')

    #st.write(data)

    colors = []
    for x in data['continent']:
        if x == 'Asia':
            colors.append('tomato')
        elif x =='Europe':
            colors.append('blue')
        elif x == 'Africa':
            colors.append('olive')
        elif x =='Americas':
            colors.append('green')
        else:
            colors.append('orange')

    data['colors'] = colors 

    year = st.slider('Select a Year', 1952, 2007, 1952, step = 5)
    st.write('## ', year, '년')

    data = data[data['year']==year]

    fig, ax = plt.subplots()
    ax.scatter(data['gdpPercap'],data['lifeExp'],s=data['pop']*0.000002, color = data['colors'])
    ax.set_title('How Does Gdp per Capital relate to Life Expectancy?')
    ax.set_xlabel("Gdp per Capital")
    ax.set_ylabel('Life Expectancy')
    st.pyplot(fig)

    #st.write('(Asia: tomato, Europe: blue, Africa: olive, Americas: green, others: orange)')
    
else:
    st.header("마이페이지")
