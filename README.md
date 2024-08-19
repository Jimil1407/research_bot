# 🤖 PDF Research Bot

**PDF Research Bot** is a web application built using Streamlit, LangChain, and OpenAI's GPT-3.5 language model, designed to assist users in researching PDF documents by generating questions and finding answers. This tool simplifies the process of extracting relevant information from PDFs, making research more efficient and accessible.

## 🔍 Overview

The PDF Research Bot leverages the capabilities of GPT-3.5 and LangChain to analyze PDF documents and provide users with insightful questions and answers based on the content. This application is particularly useful for students, researchers, and professionals who need to quickly sift through large amounts of text to find specific information.

## 🎯 Features

- **Question Generation:** Automatically generate questions from the content of a PDF document.
- **Answer Extraction:** Find and highlight answers to user-generated questions within the PDF.
- **Chain of Thought Reasoning:** Enhanced with LangChain to improve the accuracy and relevance of generated questions and answers.
- **User-Friendly Interface:** A simple and intuitive web interface built with Streamlit.
- **Interactive Experience:** Users can input custom queries and receive relevant answers in real-time.

## 🚀 Getting Started

### Prerequisites

Before running the PDF Research Bot, ensure you have the following installed:

- **Python 3.8+**
- **Streamlit** (`pip install streamlit`)
- **PyPDF2** (`pip install PyPDF2`)
- **LangChain** (`pip install langchain`)
- **OpenAI** (`pip install openai`)
- **Environment Variables:**
  - **OpenAI API Key** (You can get it from the [OpenAI website](https://platform.openai.com/docs/overview))

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Jimil1407/research_bot.git
   cd pdf-research-bot

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt

3. **Setup the OpenAI API key:**
  •	Create a .env file in the root directory of the project.
	•	Add your OpenAI API key:

4. **Run the Application:**
   ```bash
   streamlit run app.py

   ## 🛠️ Usage

1. **Upload a PDF document:**
   - Use the file uploader in the Streamlit app to upload your PDF document.

2. **Generate Questions:**
   - The bot will automatically generate questions based on the content of the PDF.

3. **Ask Custom Questions:**
   - Input your custom questions in the text box to get specific answers from the PDF.

4. **Explore Answers:**
   - The bot will display the most relevant answers fromt the sections of the PDF to your questions.

## 📊 Results

The PDF Research Bot provides users with a list of generated questions and their corresponding answers, helping to extract and focus on key information from PDF documents. The results are displayed interactively in the Streamlit interface, making it easy to navigate through the content.

## 🧠 How it Works

- **PDF Parsing:** The application uses PyPDF2 to extract text from PDF documents.
- **Chain of Thought Reasoning:** LangChain enhances the processing of text, enabling more accurate question generation and answer extraction.
- **Question Generation & Answering:** GPT-3.5 processes the extracted text, generating questions and finding answers based on user queries.
- **Streamlit Interface:** The front-end is powered by Streamlit, allowing users to interact with the bot in real-time.

## 🤝 Contributing

Contributions are welcome! If you have ideas for new features or improvements, feel free to open an issue or submit a pull request.
   

  
