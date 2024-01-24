from config import config
from langchain_core.documents.base import Document
from langchain.text_splitter import TokenTextSplitter
from transformers import AutoTokenizer


def make_splits():
    #from langchain.document_loaders import DirectoryLoader

    #loader = DirectoryLoader(config["data_folder"], glob="**/*.txt", show_progress=True)
    #data = loader.load()
    data = []
    import os
    print("to read data")
    i_file = 0
    for filename in os.listdir(config["data_folder"]):
        with open(os.path.join(config["data_folder"], filename), "r") as fobj:
            data.append(Document(page_content=fobj.read(), metadata={"filename": filename}))
        i_file += 1
        if i_file % 1000 == 0:
            print(i_file)
    print("data readed")
    #from utils import get_chunks
    #all_splits = []
    #i_file = 0
    print("to chunk")
    tokenizer = AutoTokenizer.from_pretrained(config["HuggingFaceTokenizer"])
    tsplitter = TokenTextSplitter.from_huggingface_tokenizer(tokenizer, chunk_size=config["SplitTokens_N"], chunk_overlap=config["SplitTokens_Overlap"], strip_whitespace=True)
    returned_docs = tsplitter.split_documents(data)
    #for _d in data:
    #    chunks = get_chunks(_d, size=500, around=10, overlap=100)
    #    all_splits.extend(chunks)
    #    i_file += 1
    #    if i_file % 1000 == 0:
    #        print(i_file)
    return returned_docs#[Document(page_content=x) for x in all_splits]
    #from langchain.text_splitter import RecursiveCharacterTextSplitter

    #text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    #all_splits = text_splitter.split_documents(data)
    #return all_splits