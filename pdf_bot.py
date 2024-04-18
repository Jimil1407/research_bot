import streamlit as st
from llm_functions import load_data, split_text, initialize_llm, generate_questions, create_retrieval_qa_chain
from langchain_community.vectorstores import Chroma



if 'questions' not in st.session_state:
    st.session_state['questions'] = 'empty'
    st.session_state['questions_to_answers'] = []
    st.session_state['submitted'] = False

st.title("PDF Research Bot")
st.subheader("This bot generates questions and answers from a PDF file.")
openai_api_key = st.text_input("OpenAI API Key", type="password")

st.write("Upload your PDF file to generate questions and answers.")
uploaded_file = st.file_uploader("Upload PDF", type=['pdf'])


if uploaded_file is not None and openai_api_key:

    text_from_pdf = load_data(uploaded_file)

    documents_for_question_gen = split_text(text_from_pdf, chunk_size=10000, chunk_overlap=200)
    documents_for_question_answering = split_text(text_from_pdf, chunk_size=500, chunk_overlap=200)

    llm_question_gen = initialize_llm(openai_api_key=openai_api_key, model="gpt-3.5-turbo-16k", temperature=0.4)
    llm_question_answering = initialize_llm(openai_api_key=openai_api_key, model="gpt-3.5-turbo", temperature=0.1)

    if st.session_state['questions'] == 'empty':
        with st.spinner("Generating questions..."):
            st.session_state['questions'] = generate_questions(llm=llm_question_gen, chain_type="refine", documents=documents_for_question_gen)

    if st.session_state['questions'] != 'empty':
        st.subheader("Generated Questions")
        st.info(st.session_state['questions'])

        st.session_state['questions_list'] = st.session_state['questions'].split('\n')

        st.subheader("Select Questions to Answer")
        st.write("Select the questions you want answers to:")
        st.session_state['questions_to_answers'] = st.multiselect(label="", options=st.session_state['questions_list'])

        if st.button('Generate Answers'):
            st.session_state['submitted'] = True


    if st.session_state['submitted']:
        st.subheader("Generated Answers")
        with st.spinner("Generating answers..."):
            generate_answer_chain = create_retrieval_qa_chain(openai_api_key=openai_api_key, documents=documents_for_question_answering, llm=llm_question_answering)
            for question in st.session_state['questions_to_answers']:
                answer = generate_answer_chain.run(question)
                st.write(f"Question: {question}")
                st.info(f"Answer: {answer}")
