from langchain_community.embeddings import HuggingFaceEmbeddings
from transformers import AutoTokenizer
from src.config.config import AppConfig

if __name__ == "__main__":
	HuggingFaceEmbeddings(model_name=AppConfig.get_config().huggingface_embeddings)
	if AppConfig.get_config().tokenizer == "huggingface":
		tokenizer = AutoTokenizer.from_pretrained(AppConfig.get_config().tokenizer_model)