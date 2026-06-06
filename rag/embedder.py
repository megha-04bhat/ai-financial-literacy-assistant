from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

def get_embeddings():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )


def create_vectorstore(chunks):
    embeddings = get_embeddings()
    
    vectorstore = FAISS.from_documents(chunks, embeddings)
    vectorstore.save_local("vectorstore")
    
    return vectorstore


def load_vectorstore():
    embeddings = get_embeddings()
    
    return FAISS.load_local(
        "vectorstore",
        embeddings,
        allow_dangerous_deserialization=True
    )