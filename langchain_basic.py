from dotenv import load_dotenv
import os
from openai import OpenAI
from langchain_openai import ChatOpenAI
load_dotenv()
openai_api_key = os.getenv("openai_api_key")

# api key 불러오는지 확인하기
# print(os.getenv("openai_api_key"))

# langchain client 생성
llm = ChatOpenAI(api_key=openai_api_key)

# langchain 모델 사용 (신규 데이터에 대해선 정보가 업데이트 안됨)
output = llm.invoke("2024년 청년 지원 정책에 대하여 알려줘")
print(output)