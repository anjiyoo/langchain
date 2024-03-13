from dotenv import load_dotenv
import os
from openai import OpenAI
from langchain_openai import ChatOpenAI
load_dotenv()
openai_api_key = os.getenv("openai_api_key")

llm = ChatOpenAI(api_key=openai_api_key)

# 파싱하기
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "너는 청년을 행복하게 하기 위한 정부정책 안내 컨설턴트야"),
        ("user", "{input}")
    ]
)

output_parser = StrOutputParser()
chain = prompt | llm | output_parser
output = chain.invoke({"input": "2024년 청년 지원 정책에 대해 알려줘"})
print(output)