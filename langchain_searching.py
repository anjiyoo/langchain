# 크롤링 라이브러리 설치
# pip install beautifulsoup4

from dotenv import load_dotenv
import os
from openai import OpenAI
from langchain_openai import ChatOpenAI
load_dotenv()
openai_api_key = os.getenv("openai_api_key")

llm = ChatOpenAI(api_key=openai_api_key)

# 신규 데이터 web에서 가져오기
from langchain_community.document_loaders import WebBaseLoader
loader = WebBaseLoader("https://www.moel.go.kr/policy/policyinfo/support/list4.do")
doce = loader.load()
print(doce)