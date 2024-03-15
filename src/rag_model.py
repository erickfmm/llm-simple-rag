from src.config.config import AppConfig
from langchain_core.documents.base import Document
from src.steps.vectorstore import load_or_create_vectorstore, retrieve
from src.steps.answer_question_llm import Answer
from datetime import datetime
import typing

class RAG_Model():
    def __init__(self) -> None:
        self.timestamp_created = datetime.now()
        print("Creating RAG model... at", self.timestamp_created)
        self.vectorstore = None
        self.answer = Answer()

    def make_question(self, question) -> typing.List[Document]:
        if self.vectorstore is None:
            self.vectorstore = load_or_create_vectorstore()
        # Run
        
        retriever = retrieve(vectorstore=self.vectorstore, k = AppConfig.get_config().k_documents, filters=None)
        docs = retriever.get_relevant_documents(question)
        print(docs)
        for d in docs:
            print(d)
            print("-"*15)
        del self.vectorstore
        self.vectorstore = None #for empty the memory
        return docs

    def rag_model_function(self, prompt1, prompt2):
        print("RAG created at...", self.timestamp_created)
        
        question = prompt2
        docs = self.make_question(question)
        if AppConfig.get_config().model.TYPE == "gguf":
            result = self.answer.answer_question_llamacpp(prompt1, docs)
        elif AppConfig.get_config().model.TYPE == "mt5":
            result = self.answer.answer_question_mt5(prompt1, docs)
        else:
            raise NotImplementedError("Model type not implemented")
        return result, docs
