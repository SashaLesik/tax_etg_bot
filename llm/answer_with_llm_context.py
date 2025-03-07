from langchain.chains import create_history_aware_retriever
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.messages import HumanMessage

contextualize_q_system_prompt = """Given a chat history and the latest user question \
which might reference context in the chat history, formulate a standalone question \
which can be understood without the chat history. Do NOT answer the question, \
just reformulate it if needed and otherwise return it as is."""
contextualize_q_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", contextualize_q_system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ]
)
vectorstore = Chroma(persist_directory="./chroma_db", embedding_function=OpenAIEmbeddings())
# vectorstore = Chroma.from_documents(documents=splits,
#                                     embedding=OpenAIEmbeddings(), persist_directory="./chroma_db")
retriever = vectorstore.as_retriever()
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

history_aware_retriever = create_history_aware_retriever(
    llm, retriever, contextualize_q_prompt
)

qa_system_prompt = """You are an assistant for question-answering tasks. \
Use the following pieces of retrieved context to answer the question. \
If you don't know the answer, just say that you don't know. \
Use three sentences maximum and keep the answer concise.\

{context}"""
qa_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", qa_system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ]
)


question_answer_chain = create_stuff_documents_chain(llm, qa_prompt)

rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)



chat_history = []

def answer(query, context):
    response = rag_chain.invoke({"input": query, "chat_history": [context]})
    #response = 'Тут будет ответ на вопрос ' + query + ' с контекстом ' + context
    return {"response": response['answer']}
# question = "What is Task Decomposition?"
# ai_msg_1 = rag_chain.invoke({"input": question, "chat_history": chat_history})
# chat_history.extend([HumanMessage(content=question), ai_msg_1["answer"]])
#
# second_question = "What are common ways of doing it?"
# ai_msg_2 = rag_chain.invoke({"input": second_question, "chat_history": chat_history})
#
# print(ai_msg_2["answer"])