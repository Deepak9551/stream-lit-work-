
import streamlit as st
import  numpy as np
import pandas as pd
import time as t

st.title("Hello GeeksForGeeks !!!")
st.text('my name is deepak')
st.image('https://imgs.search.brave.com/w5h9ISnvVDHDEZvxgYHhhzATEvle7eRGhXa653S1ESM/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9zdGF0/aWMudmVjdGVlenku/Y29tL3N5c3RlbS9y/ZXNvdXJjZXMvdGh1/bWJuYWlscy8wMjMv/NjAyLzI1NS9zbWFs/bC90cm9waWNhbC13/YWxscGFwZXItYmFu/bmVyLXdpdGgtZXhv/dGljLXBhcnJvdC1v/bi12aXZpZC1iYWNr/Z3JvdW5kLWdlbmVy/YXRpdmUtYWktcGhv/dG8uanBn')
st.caption('parot image',text_alignment="left")

st.checkbox('my check')

st.text('pick your city')
st.button('click me')

st.radio('pick your city',['lucknow','delhi'] , index=1)

st.selectbox('pick you fav sport ',['cricket','gaming','singing','walking'])

st.select_slider(':rainbow[give me rate]',['bad','good','excellent'])
st.slider('score',1,100)

on =  st.toggle('activate')
if on :
    st.write(':red[feature activated !!]')

st.title('User Input')
num = st.number_input('Enter number',value=0)

if num:
    st.write('num is : ',num)

db = st.date_input('enter your birthday.',value=None)
if db:
    st.write('dob : ',db)

tm = st.time_input('enter time.',value=None)
if tm:
    st.write('dob : ',tm)

tx = st.text_input('enter text.',value=None)
if tx:
    st.write('data : ',tx)
txarea = st.text_area('enter text.',value=None)
if txarea:
    st.write('description : ',txarea)
st.file_uploader('upload file')

color = st.color_picker('color picker',value='#FF0000')
st.write('color : ',color)

st.success('success')
st.error('error')
st.info('info')
st.exception(Exception('this is error'))

st.sidebar.header('Stream lit')
st.sidebar.text("DEEPAK KUMAR",text_alignment="center")
st.sidebar.image('https://wallpapers.com/images/hd/goku-ultra-instinct-pictures-yv6nqgnu9xbmmmfr.jpg')

df = pd.DataFrame(data=np.random.randint(1,100,size=(10,5)))
st.dataframe(df)

col1,col2,col3  = st.columns(3)
col1.metric('Temperature','70 F','1.2 F')
col2.metric('Wind','8 mph','-8%')
col3.metric('Humidity','86%','4%')

with st.status('step 1'):
    t.sleep(1)
    st.write('step2')
    t.sleep(2)
    st.write('step3')
    t.sleep(3)
    st.write('step4')
st.button('rerun')

promt = st.chat_input('say something ')
if promt:
    st.write('chat : ',promt)

d = pd.DataFrame(np.random.randn(20,3),columns=['a','b','c'])
st.write(d)
st.area_chart(d)

with st.chat_message('user'):
    st.write('Hello ji')
with st.chat_message('admin'):
    st.write('Hello admin ji')
with st.chat_message('bot'):
    st.write('Hello bot ji')