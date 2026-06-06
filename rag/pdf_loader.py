from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_pdfs(pdf_paths):
    documents = []
    
    for path in pdf_paths:
        loader = PyPDFLoader(path)
        documents.extend(loader.load())
    
    return documents


def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    
    return splitter.split_documents(documents)