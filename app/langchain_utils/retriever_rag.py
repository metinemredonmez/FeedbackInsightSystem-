import pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone as PineconeVectorStore
from app.core.config import PINECONE_API_KEY, OPENAI_API_KEY

def get_retriever(index_name="feedback-insight", environment="gcp-starter"):
    pinecone.init(api_key=PINECONE_API_KEY, environment=environment)
    index = pinecone.Index(index_name)
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    vectorstore = PineconeVectorStore(index, embeddings.embed_query, "text")
    return vectorstore.as_retriever()
