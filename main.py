import streamlit as st
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(openai_api_key = "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")

from langchain_core.prompts import ChatPromptTemplate
prompt = ChatPromptTemplate.from_messages([
    ("system", "너는 사람들에게 관광지를 추천해주는 여행 전문가야."),
    ("user", "{input}")
])

from langchain_core.output_parsers import StrOutputParser
output_parser = StrOutputParser()

chain = prompt | llm | output_parser

st.title('대한민국 관광명소 추천')
title = st.text_input('어떤 여행을 떠나시나요?')

if st.button('여행지 추천받기'):
    with st.spinner('골똘히 고민 중...'):
        result = chain.invoke({"input" : title})
        st.write(result)

