from src.config.config import AppConfig
from langchain_core.documents.base import Document
from langchain.text_splitter import TokenTextSplitter
from transformers import AutoTokenizer


def make_splits():
    data = []
    import os
    print("to read data")
    i_file = 0
    for filename in os.listdir(AppConfig.get_config().data_folder):
        with open(os.path.join(AppConfig.get_config().data_folder, filename), "r") as fobj:
            data.append(Document(page_content=fobj.read(), metadata={"filename": filename}))
        i_file += 1
        if i_file % 1000 == 0:
            print(i_file)
    print("data readed")
    
    print("to chunk")
    tokenizer = AutoTokenizer.from_pretrained(AppConfig.get_config().huggingface_tokenizer)
    tsplitter = TokenTextSplitter.from_huggingface_tokenizer(tokenizer, chunk_size=AppConfig.get_config().splittokens_n, chunk_overlap=AppConfig.get_config().splittokens_overlap, strip_whitespace=True)
    returned_docs = tsplitter.split_documents(data)
    
    return returned_docs