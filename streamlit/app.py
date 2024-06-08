import streamlit as st
from langchain_community.llms import Ollama

# Streamlit 설정
st.title("Chatbot using LLaMA2")
st.write("Enter your message below:")

# 사용자 입력
user_input = st.text_input("You:", "")

# LLaMA2 모델을 사용하여 응답 생성
if st.button("Send"):
    if user_input:
        llm = Ollama(model="llama2")
        response = llm(user_input)
        st.text_area("Chatbot:", response, height=200)
    else:
        st.warning("Please enter a message.")