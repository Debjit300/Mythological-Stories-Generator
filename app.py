import streamlit as st
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline

# Load HuggingFace Embeddings
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Load your Vector Store safely
vector_store = FAISS.load_local(
    "vector_store",
    embeddings,
    allow_dangerous_deserialization=True
)

# Load Free HuggingFace Model Locally
flan_pipeline = pipeline(
    "text2text-generation",
    model="google/flan-t5-xl",   # If too heavy, switch to flan-t5-base
    max_length=512
)

llm = HuggingFacePipeline(pipeline=flan_pipeline)

# Build QA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vector_store.as_retriever(search_kwargs={"k": 3})
)

# Streamlit UI Setup
st.set_page_config(page_title="Insurance Policy Assistant", page_icon="🛡️", layout="centered")

# Custom CSS Styling
st.markdown(
    """
    <style>
    body {
        background-color: #f0f2f6;
    }
    .main {
        background-color: #f0f2f6;
        padding: 2rem;
    }
    .title {
        font-size: 40px;
        text-align: center;
        font-weight: bold;
        color: #333333;
    }
    .subtitle {
        font-size: 20px;
        text-align: center;
        color: #555555;
        margin-bottom: 30px;
    }
    .response-box {
        background-color: #ffffff;
        padding: 20px;
        margin-top: 20px;
        border-radius: 10px;
        box-shadow: 0px 2px 8px rgba(0, 0, 0, 0.1);
        color: #333333;
    }
    .stButton > button {
        width: 100%;
        height: 45px;
        font-size: 18px;
        font-weight: bold;
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar
with st.sidebar:
    st.title("ℹ️ About")
    st.markdown("This chatbot helps you with information about Auto, Health, and Home Insurance.")
    st.markdown("---")
    st.title("📋 Help")
    st.markdown("Type your question about insurance policies and click **Send**.")
    st.markdown("If the bot is not sure, click **Connect to Human Agent**.")
    st.markdown("---")
    if st.button("🔄 Reset Chat"):
        st.experimental_rerun()

# Title & Subtitle
st.markdown('<div class="title">🛡️ Insurance Policy Assistant</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Ask me anything about Auto, Health, or Home Insurance!</div>', unsafe_allow_html=True)

# Input + Send Button
with st.form(key='chat_form'):
    user_input = st.text_input("Enter your question:", key="input", placeholder="e.g., What does home insurance cover?", help="Ask about Auto, Health, or Home Insurance.")
    submit_button = st.form_submit_button(label="Send")

if submit_button and user_input:
    response = qa_chain.run(user_input)

    if "I'm not sure" in response or len(response) < 20:
        st.warning("🤔 I'm not confident about this answer. Would you like to speak to a human agent?")
        if st.button("👩‍💼 Connect to Human Agent"):
            st.success("✅ A human agent will reach out to you shortly!")
    else:
        st.markdown(f"<div class='response-box'><b>Answer:</b><br>{response}</div>", unsafe_allow_html=True)
