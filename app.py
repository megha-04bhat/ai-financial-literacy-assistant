from rag.pdf_loader import load_pdfs, split_documents
from rag.embedder import create_vectorstore, load_vectorstore
from rag.retrieval import get_retriever, retrieve_docs
from rag.formatter import format_context
from utils.model import generate_response

import os

#  PDF paths
pdf_paths = [
    "data/form2.pdf",
    "data/Google_Pay_guidelines.pdf",
    "data/GUIDE310113_F.pdf",
    "data/Upi_guidelines.pdf"
]

# ==============================
#  HELPER FUNCTIONS
# ==============================

def safety_check(query):
    risky_words = ["otp", "pin", "password", "bank details"]
    for word in risky_words:
        if word in query.lower():
            return "⚠️ Never share OTP, PIN, or passwords with anyone."
    return None


def should_use_fallback(docs):
    if not docs:
        return True
    total_length = sum(len(doc.page_content) for doc in docs)
    return total_length < 200


def is_general_question(query):
    keywords = ["save", "budget", "investment", "loan", "interest", "money"]
    return any(word in query.lower() for word in keywords)


# ==============================
#  VECTOR DATABASE SETUP
# ==============================

if not os.path.exists("vectorstore/index.faiss"):
    print("🔄 Creating vector database...")
    documents = load_pdfs(pdf_paths)
    chunks = split_documents(documents)
    vectorstore = create_vectorstore(chunks)
    print("✅ Vector DB created!")
else:
    print("⚡ Loading existing vector DB...")
    vectorstore = load_vectorstore()

#  Retriever
retriever = get_retriever(vectorstore)

print("\n💰 Financial Literacy AI Agent Ready! (type 'exit' to quit)\n")

# ==============================
#  CHAT LOOP
# ==============================

while True:
    query = input("You: ")

    if query.lower() == "exit":
        print("👋 Exiting... Stay financially safe!")
        break

    #  Safety check
    warning = safety_check(query)
    if warning:
        print("AI:", warning, "\n")
        continue

    #  Routing + fallback
    if is_general_question(query):
        context = ""
    else:
        docs = retrieve_docs(retriever, query)

        if should_use_fallback(docs):
            context = ""
        else:
            context = format_context(docs)

    #  Prompt design (optimized for LLaMA3)
    if context:
        prompt = f"""
You are a financial assistant.

Use the context below and explain clearly in simple words in 4-5 lines.
Do NOT copy text. Explain in your own words.

Context:
{context}

Question: {query}
Answer:
"""
    else:
        prompt = f"""
You are a financial assistant.

Explain clearly in simple language in 4-5 lines.

Question: {query}
Answer:
"""

    # Generate response
    response = generate_response(prompt)

    print("AI:", response, "\n")