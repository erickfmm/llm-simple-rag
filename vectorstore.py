from load_data import make_splits

def make_vectorstore():
    all_splits = make_splits()
    from langchain.embeddings import HuggingFaceEmbeddings
    from langchain.vectorstores import Chroma
    print("to vector store")
    vectorstore = Chroma.from_documents(documents=all_splits, embedding=HuggingFaceEmbeddings(model_name='dccuchile/bert-base-spanish-wwm-uncased'), persist_directory="./models/chroma_db")
    print("vector store saved")
    return vectorstore

def load_vectorstore():
    from langchain.embeddings import HuggingFaceEmbeddings
    from langchain.vectorstores import Chroma
    print("to load vector store")
    db3 = Chroma(persist_directory="./models/chroma_db", embedding_function=HuggingFaceEmbeddings(model_name='dccuchile/bert-base-spanish-wwm-uncased'))
    return db3

def load_or_create_vectorstore():
    import os
    if os.path.exists("./models/chroma_db"):
        return load_vectorstore()
    else:
        return make_vectorstore()