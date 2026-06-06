def get_retriever(vectorstore):
    return vectorstore.as_retriever(search_kwargs={"k": 5})


def retrieve_docs(retriever, query):
    docs = retriever.invoke(query)
    
    #  Filter weak/empty docs
    filtered_docs = [doc for doc in docs if len(doc.page_content.strip()) > 50]
    
    return filtered_docs