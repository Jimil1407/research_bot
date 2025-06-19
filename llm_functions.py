from langchain.text_splitter import TokenTextSplitter
from langchain.docstore.document import Document
from langchain.chat_models import ChatOpenAI
from langchain.chains.summarize import load_summarize_chain
from prompts import PROMPT_QUESTIONS, REFINE_PROMPT_QUESTIONS
from langchain.chains import RetrievalQA
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from PyPDF2 import PdfReader 

def load_data(uploaded_file):
    pdf_reader = PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    
    return text

#function to split text

def split_text(text, chunk_size, chunk_overlap):
    text_splitter = TokenTextSplitter(model_name="gpt-3.5-turbo-16k", chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    text_chunks = text_splitter.split_text(text)
    documents = [Document(page_content=t) for t in text_chunks]

    return documents

def initialize_llm(openai_api_key, model, temperature):
    llm = ChatOpenAI(openai_api_key=openai_api_key,model=model, temperature=temperature)

    return llm

def generate_questions(llm, chain_type, documents):
    question_chain = load_summarize_chain(llm=llm, chain_type=chain_type, question_prompt=PROMPT_QUESTIONS, refine_prompt=REFINE_PROMPT_QUESTIONS)
    questions = question_chain.run(documents)

    return questions

def create_retrieval_qa_chain(openai_api_key, documents, llm):
    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    vector_database = Chroma.from_documents(documents=documents, embedding=embeddings)
    retrieval_qa_chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=vector_database.as_retriever())
    
    return retrieval_qa_chain