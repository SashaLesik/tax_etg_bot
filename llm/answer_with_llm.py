
from langchain import hub
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_community.vectorstores import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)
# Load Documents
# loader = DirectoryLoader(
#     './data', glob='**/*', loader_cls=TextLoader
# )
# docs = loader.load()
#
# # Split
# text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
# splits = text_splitter.split_documents(docs)

# Embed
vectorstore = Chroma(persist_directory="./chroma_db", embedding_function=OpenAIEmbeddings())
# vectorstore = Chroma.from_documents(documents=splits,
#                                     embedding=OpenAIEmbeddings(), persist_directory="./chroma_db")
retriever = vectorstore.as_retriever()
prompt = hub.pull("rlm/rag-prompt")
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)


rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)
def answer(query):
    #response = rag_chain.invoke(query)
    return {"response": 'это респонс-затычка чтобы не тратить деньги пока цикл не починится))'}




# Question

