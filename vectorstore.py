from load_data import make_splits
from config import config
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma


def make_vectorstore():
    all_splits = make_splits()
    
    print("to vector store")
    vectorstore = Chroma.from_documents(documents=all_splits, embedding=HuggingFaceEmbeddings(model_name=config.huggingface_embeddings), persist_directory=config.chroma_path)
    print("vector store saved")
    return vectorstore

def load_vectorstore():
    print("to load vector store")
    vectorstore = Chroma(persist_directory=config.chroma_path, embedding_function=HuggingFaceEmbeddings(model_name=config.huggingface_embeddings))
    return vectorstore

def load_or_create_vectorstore():
    """Tries to load a vectore store if exists, if not, make and return a new vectorstore

    Returns:
        Chroma: A Chroma db store with each splitted document with its embedding
    """
    import os
    if os.path.exists(config.chroma_path):
        try:
            return load_vectorstore()
        except:
            return make_vectorstore()
    else:
        return make_vectorstore()