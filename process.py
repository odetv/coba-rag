import os
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings.ollama import OllamaEmbeddings
from dotenv import load_dotenv


# Load environment variables
load_dotenv()
ollama_base_url = os.getenv("OLLAMA_BASE_URL")


# Handle directory references
if not os.path.exists("datasets"):
    os.makedirs("datasets")
if not os.path.exists("vectordb"):
    os.makedirs("vectordb")


# Process load document datasets
loader = PyPDFDirectoryLoader("datasets")
documents = loader.load()


# Process chunking documents
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=75,
    separators=[" ", ",", ".", "\n", "\n\n", "\n\n\n", "\f"]
)
chunks = text_splitter.split_documents(documents)


# Process embeddings chunks to vector database
vectordb = FAISS.from_documents(chunks, OllamaEmbeddings(base_url=ollama_base_url, model="nomic-embed-text", show_progress=True))
vectordb.save_local("vectordb")
