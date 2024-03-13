from dotenv import load_dotenv
import os
from openai import OpenAI
from langchain_openai import ChatOpenAI
load_dotenv()
openai_api_key = os.getenv("openai_api_key")

llm = ChatOpenAI(api_key=openai_api_key)

# langchain Template 기반 사용
from langchain_core.prompts import ChatPromptTemplate
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "너는 청년을 행복하게 하기 위한 정부정책 안내 컨설턴트야"),
        ("user", "{input}")
    ]
)

chain = prompt | llm
output = chain.invoke({"input":"2024년 청년 지원 정책에 대하여 알려줘"})
print(output)