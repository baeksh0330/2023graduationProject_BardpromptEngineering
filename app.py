import streamlit as st
from streamlit_chat import message
import os

from bardapi import Bard


def query_optimizer(user_input):
    optimized_query = user_input
    # query opitmizer 하는 코드 넣기
    # optimize된 query 문장을 반환 
    return optimized_query

def generate_response(query):
    response = bard.get_answer(query)['content']
    # bard로 부터 optimize된 쿼리를 질문하여 답을 받아옴
    # bard로 부터 온 답변을 반환
    return response
 
def prompt_optimizer(response):
    optimized_prompt = response
    # Prompt optimize 하는 코드 넣고 결과 반환
    return optimized_prompt

def button1Clicked():
    print("버튼 1 클릭 시 동작하는 함수")

def button2Clicked():
    print("버튼 2 클릭 시 동작하는 함수")

def button3Clicked():
    print("버튼 3 클릭 시 동작하는 함수")

def button4Clicked():
    print("버튼 4 클릭 시 동작하는 함수")

def button5Clicked():
    print("버튼 5 클릭 시 동작하는 함수")

if 'generated' not in st.session_state:
    st.session_state['generated'] = []
    st.session_state['past'] = []

st.title('✨ Graduation Project ✨')

with st.form('form', clear_on_submit=True):
    user_input = st.text_input('You: ', '', key='input')
    submitted = st.form_submit_button('Send')
 
if submitted and user_input:

    token = 'dwg5yL4kwsQkay_WLnMrqlruwXvYokR5Ji4G_sUsuCSYczVdC9Y17Ampcp8h_x5KdhyBFA.'

    bard = Bard(token=token)

    optimized_query=query_optimizer(user_input) # 이 함수에서 쿼리 optimize하기
    
    response = generate_response(optimized_query) # optimze한 쿼리를 바드를 통해 답변 받아오기
    
    optimized_prompt = prompt_optimizer(response)
 
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.button("#디테일 1", key="detail_1", on_click=button1Clicked)
    with col2:
        st.button("#디테일2", key="detail_2", on_click=button2Clicked)
    with col3:
        st.button("#유지 보수", key="detail_3", on_click=button3Clicked)
    with col4:
        st.button("#언어", key="detail_4", on_click=button4Clicked)
    with col5:
        st.button("#보안", key="detail_5", on_click=button5Clicked)

    st.session_state.past.append(optimized_query)
    st.session_state.generated.append(optimized_prompt)\
        
    for i in range(len(st.session_state['generated'])):
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
        message(st.session_state["generated"][i], key=str(i))