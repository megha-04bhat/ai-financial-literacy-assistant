# AI Agent for Digital Financial Literacy

## Overview

AI Agent for Digital Financial Literacy is a Retrieval-Augmented Generation (RAG) based chatbot designed to improve financial awareness and digital payment literacy. The system provides accurate and easy-to-understand answers related to UPI, banking services, savings, interest rates, and digital financial safety.

The project combines semantic document retrieval with a Large Language Model (LLaMA3) to generate context-aware responses from trusted financial documents.

---

## Features

* Retrieval-Augmented Generation (RAG)
* Semantic Search using FAISS
* Local LLM Inference using LLaMA3 via Ollama
* Streamlit-based Chat Interface
* Session-based Chat History
* Fallback Mechanism for General Queries
* Fraud Prevention Alerts (OTP/PIN Safety Checks)
* Context-Aware Financial Guidance
* Privacy-Focused and Offline-Capable Deployment

---

## System Architecture

User Query
→ Query Processing
→ Safety Check
→ Smart Routing
→ FAISS Retrieval
→ Context Generation
→ LLaMA3 (Ollama)
→ Response Generation
→ Streamlit UI

---

## Technologies Used

* Python
* LangChain
* FAISS
* Sentence Transformers
* LLaMA3
* Ollama
* Streamlit
* PyPDF
* Requests

---

## Project Structure

```text
ai-financial-literacy-assistant/
│
├── data/
├── rag/
├── utils/
├── vectorstore/
├── app.py
├── streamlit_app.py
├── requirements.txt
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/ai-financial-literacy-assistant.git

cd ai-financial-literacy-assistant
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

Windows:

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Install Ollama

Download and install Ollama:

https://ollama.com

Pull LLaMA3:

```bash
ollama pull llama3
```

Verify:

```bash
ollama list
```

---

## Run Application

Terminal 1:

```bash
ollama run llama3
```

Terminal 2:

```bash
streamlit run streamlit_app.py
```

---

## Sample Questions

* What is UPI?
* How do I send money using UPI?
* What is a savings account?
* How can I avoid online banking fraud?
* What is a safe interest rate for a loan?

---

## Future Enhancements

* Multilingual Support (Kannada, Hindi)
* Voice-Based Interaction
* Mobile Application Deployment
* Real-Time Fraud Detection
* Personalized Financial Recommendations

---


