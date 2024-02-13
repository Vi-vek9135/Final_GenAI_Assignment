# ## Documentation for FastAPI Application for PDF Upload and Question Answering

# Make sure to set up environment variables for authentication (e.g., GOOGLE_API_KEY) as required for accessing Google's Generative AI models.

# For Running this project you have to create virtual environment
    # conda create -p venv python==3.10.0
    # conda activate venv
    # pip install -r requirements.txt
    # python main.py





# Purpose:

# This FastAPI application allows users to upload PDF files and get answers to their questions about the uploaded content. It utilizes various libraries and tools like PyPDFDirectoryLoader, Chroma, Google Generative AI, and Langchain to process text, create embeddings, and generate answers.

# Functionalities:

# - Upload PDF: Users can upload single or multiple PDF files.
# - Process and Save: The application extracts text from the uploaded PDFs, splits it into chunks, and converts them into embeddings using Google Generative AI models. These embeddings are saved in a Chroma vector database for efficient retrieval.
# - Question Answering: Users can ask questions about the uploaded documents. The application utilizes the Chroma database to find relevant passages based on the question and employs Langchain with a pre-trained question-answering model to generate an answer from those passages.

# API endpoints:

# - `/uploadpdf/`: Accepts POST requests with `pdf_name` and a list of `files`. It uploads the files, processes them, and saves embeddings in Chroma.
# - `/qa/`: Accepts POST requests with `pdf_name` and `question`. It searches the Chroma database for relevant text based on the question, generates an answer using Langchain, and returns it.

# Dependencies:

# - FastAPI
# - uvicorn
# - PyPDFDirectoryLoader
# - RecursiveCharacterTextSplitter
# - Chroma
# - Google Generative AI
# - Langchain
# - dotenv

# Code Structure:

# - The code consists of several functions:
#     - `upload_pdf`: Handles file upload and text extraction.
#     - `process_and_save_to_chroma`: Converts text to embeddings and saves them in Chroma.
#     - `create_embeddings`: Creates embeddings using Google Generative AI models.
#     - `search_chroma_db`: Searches for relevant text in Chroma based on a question.
#     - `get_answer_using_palm2`: Generates an answer using Langchain and a pre-trained QA model.

# Running the application:

# 1. Ensure you have all dependencies installed.
# 2. Set environment variables for Google API key using `dotenv`.
# 3. Replace `models/embedding-001` with the actual path to your embedding model.
# 4. Run the application using `uvicorn.run("main:app",host="127.0.0.1",reload=True)`.








