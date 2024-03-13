from dotenv import load_dotenv
import os
from openai import OpenAI
from langchain_openai import ChatOpenAI
load_dotenv()
openai_api_key = os.getenv("openai_api_key")


# langchain Template 기반 사용
from langchain_core.prompts import ChatPromptTemplate
llm = ChatOpenAI(api_key=openai_api_key)
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "너는 청년을 행복하게 하기 위한 정부정책 안내 컨설턴트야"),
        ("user", "{input}")
    ]
)

chain = prompt | llm
chain.invoke({"input":"2024년 청년 지원 정책에 대하여 알려줘"})


from langchain.chains.combine_documents import create_stuff_documents_chain
prompt = ChatPromptTemplate.from_template("""Answer the following question based only on the provided context:
<context>
{context}
</context>
Question: {input}""")
document_chain = create_stuff_documents_chain(llm, prompt)


# 바로 Docs 내용을 반영도 가능
from langchain_core.documents import Document

output = document_chain.invoke({
    "input": "국민취업지원제도가 뭐야",
    "context": [Document(page_content="""국민취업지원제도란?

취업을 원하는 사람에게 취업지원서비스를 일괄적으로 제공하고 저소득 구직자에게는 최소한의 소득도 지원하는 한국형 실업부조입니다. 2024년부터 15~69세 저소득층, 청년 등 취업취약계층에게 맞춤형 취업지원서비스와 소득지원을 함께 제공합니다.
[출처] 2024년 달라지는 청년 지원 정책을 확인하세요.|작성자 정부24""")]
})
print(output)