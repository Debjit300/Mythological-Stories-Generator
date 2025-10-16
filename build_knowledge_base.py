import pdfplumber
import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

def extract_text(folder_path):
    text = ""
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.pdf'):
            with pdfplumber.open(os.path.join(folder_path, file_name)) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text
    return text

def split_text(text):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_text(text)
    return chunks

def create_vector_store(chunks, embeddings):
    vector_store = FAISS.from_texts(chunks, embeddings)
    vector_store.save_local("vector_store")

if __name__ == "__main__":
    text_data = extract_text("knowledge_base/")
    chunks = split_text(text_data)
    create_vector_store(chunks, embeddings)
    print("Knowledge Base Created Successfully ✅")
