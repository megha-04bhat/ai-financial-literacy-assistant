import streamlit as st

from rag.embedder import load_vectorstore
from rag.retrieval import get_retriever, retrieve_docs
from rag.formatter import format_context
from utils.model import generate_response

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
#  LOAD VECTOR DB
# ==============================

@st.cache_resource
def load_resources():
    vectorstore = load_vectorstore()
    retriever = get_retriever(vectorstore)
    return retriever

retriever = load_resources()

# ==============================
#  UI CONFIG
# ==============================

st.set_page_config(page_title="💰 Financial AI Agent", layout="wide")

st.title("💰 AI Agent for Digital Financial Literacy")
st.markdown("Ask questions about UPI, banking, safety, and finance")

# ==============================
#  CHAT HISTORY (IMPORTANT)
# ==============================

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chats
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ==============================
#  USER INPUT
# ==============================

query = st.chat_input("Ask your question...")

if query:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.markdown(query)

    # ==============================
    #  SAFETY CHECK
    # ==============================

    warning = safety_check(query)
    if warning:
        response = warning

    else:
        # ==============================
        #  RAG + FALLBACK
        # ==============================

        if is_general_question(query):
            context = ""
        else:
            docs = retrieve_docs(retriever, query)

            if should_use_fallback(docs):
                context = ""
            else:
                context = format_context(docs)

        # ==============================
        #  PROMPT
        # ==============================

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

        # ==============================
        #  GENERATE RESPONSE
        # ==============================

        response = generate_response(prompt)

    # Show AI response
    with st.chat_message("assistant"):
        st.markdown(response)

    # Save to history
    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )