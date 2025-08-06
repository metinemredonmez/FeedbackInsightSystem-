from app.langchain_utils.retriever_rag import get_retriever

class RAGNode:
    def __init__(self):
        self.retriever = get_retriever()

    def run(self, query: str):
        docs = self.retriever.get_relevant_documents(query)
        return {"retrieved_docs": [d.page_content for d in docs]}
