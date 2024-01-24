from langchain_community.embeddings import HuggingFaceEmbeddings
from transformers import AutoTokenizer
from config import config

if __name__ == "__main__":
	HuggingFaceEmbeddings(model_name=config["HuggingFaceEmbeddings"])
	tokenizer = AutoTokenizer.from_pretrained(config["HuggingFaceTokenizer"])