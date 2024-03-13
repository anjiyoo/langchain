# pip install faiss-cpu
# Facebook AI Research에 의해 개발된 효율적인 유사성 검색 및 클러스터링의 대규모 데이터셋을 위한 라이브러리

from dotenv import load_dotenv
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'  # OMP: Error #15: Initializing libiomp5md.dll 해결
from openai import OpenAI
from langchain_openai import ChatOpenAI
load_dotenv()
openai_api_key = os.getenv("openai_api_key")


from langchain_openai import ChatOpenAI
llm = ChatOpenAI(api_key=openai_api_key)


from langchain_core.prompts import ChatPromptTemplate
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "너는 청년을 행복하게 하기 위한 정부정책 안내 컨설턴트야"),
        ("user", "{input}")
    ]
)
chain = prompt | llm
chain

from langchain_community.document_loaders import WebBaseLoader
loader = WebBaseLoader("https://www.moel.go.kr/policy/policyinfo/support/list4.do")
docs = loader.load()


from langchain_openai import OpenAIEmbeddings
embeddings = OpenAIEmbeddings(api_key=openai_api_key)


from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter()
documents = text_splitter.split_documents(docs)
vector = FAISS.from_documents(documents, embeddings)


from langchain.chains.combine_documents import create_stuff_documents_chain
prompt = ChatPromptTemplate.from_template("""Answer the following question based only on the provided context:
<context>
{context}
</context>
Question: {input}""")
document_chain = create_stuff_documents_chain(llm, prompt)


from langchain.chains import create_retrieval_chain
retriever = vector.as_retriever()
retrieval_chain = create_retrieval_chain(retriever, document_chain)
response = retrieval_chain.invoke({"input": "상담센터 전화번호 뭐야"})
print(response["answer"])