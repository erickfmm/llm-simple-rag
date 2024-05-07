from src.config.config import AppConfig
from langchain_core.documents.base import Document
from langchain.text_splitter import TokenTextSplitter
from transformers import AutoTokenizer
import re
import os
import pandas as pd

def is_int(n):
    try:
        _ = int(n)
        return True
    except:
        return False

def chunk_data(data):
    print("to chunk")
    if AppConfig.get_config().tokenizer == "tiktoken":
        tsplitter = TokenTextSplitter.from_tiktoken_encoder(AppConfig.get_config().tokenizer_model, chunk_size=AppConfig.get_config().splittokens_n, chunk_overlap=AppConfig.get_config().splittokens_overlap, strip_whitespace=True)
        returned_docs = tsplitter.split_documents(data)
    elif AppConfig.get_config().tokenizer == "huggingface":
        tokenizer = AutoTokenizer.from_pretrained(AppConfig.get_config().tokenizer_model)
        tsplitter = TokenTextSplitter.from_huggingface_tokenizer(tokenizer, chunk_size=AppConfig.get_config().splittokens_n, chunk_overlap=AppConfig.get_config().splittokens_overlap, strip_whitespace=True)
        returned_docs = tsplitter.split_documents(data)
        docs_to_return = []
        for doc in returned_docs:
            if AppConfig.get_config().splittokens_n*AppConfig.get_config().percentage_length_low \
                < len(tokenizer.tokenize(" ".join(doc.page_content.split()))) < \
                    AppConfig.get_config().splittokens_n*AppConfig.get_config().percentage_length_up:
                docs_to_return.append(doc)
        returned_docs = docs_to_return
    else:
        raise NotImplementedError("Tokenizer not implemented")
    
    
    #import matplotlib.pyplot as plt
    #size_chunks = [len(tokenizer.tokenize(doc.page_content)) for doc in returned_docs]
    #plt.hist(size_chunks, 30)
    #plt.show()
    print(len(returned_docs), " total chunked documents")
    return returned_docs

def read_data_from_folder():
    data = []
    print("to read data")
    i_file = 0
    for filename in os.listdir(AppConfig.get_config().data_folder):
        with open(os.path.join(AppConfig.get_config().data_folder, filename), "r") as fobj:
            text = fobj.read()
            if AppConfig.get_config().regex_preprocessing is not None:
                text = re.sub(AppConfig.get_config().regex_preprocessing, ' ', text) #delete weird characters and replace it by space
            text = re.sub(r'(\n( )?)+', r'\n', text) #remove duplicate new lines
            text = re.sub(r'( )+', r' ', text) #remove duplicate spaces
            text_tmp = []
            for line in text.splitlines():
                if not is_int(line.strip().replace(".", "")) and len(line.strip()) > 1:
                    text_tmp.append(line)
            text = "\n".join(text_tmp)
            if len(text) > 0:
                print(text)
                data.append(Document(page_content=text, metadata={"filename": filename}))
        i_file += 1
        if i_file % 1000 == 0:
            print(i_file)
    print("data readed")

def read_data_from_file():
    data = []
    df = pd.read_csv(AppConfig.get_config().data_file)
    for idx, row in df.iterrows():
        if not AppConfig.get_config().data_file_column in row:
            raise ValueError("Error no target column in data file")
        target_value = row[AppConfig.get_config().data_file_column]
        if AppConfig.get_config().regex_preprocessing is not None:
            target_value = re.sub(AppConfig.get_config().regex_preprocessing, ' ', target_value) #delete weird characters and replace it by space
            target_value = re.sub(r'(\n( )?)+', r'\n', target_value) #remove duplicate new lines
            target_value = re.sub(r'( )+', r' ', target_value) #remove duplicate spaces
        metadatas = dict()
        for k in row.keys():
            if k != AppConfig.get_config().data_file_column and not pd.isna(row[k]):
                metadatas[k] = row[k]
        if len(target_value) > 0:
            data.append(Document(page_content=target_value, metadata=metadatas))
    return data

def make_splits():
    if AppConfig.get_config().data_folder is not None:
        return chunk_data(read_data_from_folder())
    elif AppConfig.get_config().data_file is not None and AppConfig.get_config().data_file_column is not None:
        return chunk_data(read_data_from_file())
    else:
        raise ValueError("You must set a data source")