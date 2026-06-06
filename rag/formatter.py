
def format_context(docs):
    return "\n".join([doc.page_content for doc in docs])


def build_prompt(query, context):
    return f"""
Answer the question in simple words.

Question: {query}

Answer:
"""