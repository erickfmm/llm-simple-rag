from load_data import make_splits
from config import config

def make_vectorstore():
    all_splits = make_splits()
    from langchain_community.embeddings import HuggingFaceEmbeddings
    from langchain_community.vectorstores import Chroma
    print("to vector store")
    vectorstore = Chroma.from_documents(documents=all_splits, embedding=HuggingFaceEmbeddings(model_name=config["HuggingFaceEmbeddings"]), persist_directory=config["chromadb_file"])
    print("vector store saved")
    return vectorstore

def load_vectorstore():
    from langchain_community.embeddings import HuggingFaceEmbeddings
    from langchain_community.vectorstores import Chroma
    print("to load vector store")
    db3 = Chroma(persist_directory=config["chromadb_file"], embedding_function=HuggingFaceEmbeddings(model_name=config["HuggingFaceEmbeddings"]))
    return db3

def load_or_create_vectorstore():
    import os
    if os.path.exists(config["chromadb_file"]):
        return load_vectorstore()
    else:
        return make_vectorstore()