from src.config.config import AppConfig

from src.vectorstore import load_or_create_vectorstore
from datetime import datetime
import os
import requests


class RAG_Model():
    def __init__(self) -> None:
        self.timestamp_created = datetime.now()
        print("Creating RAG model... at", self.timestamp_created)
        self.vectorstore = None
        self.llm = None

    def rag_model_function(self, prompt1, prompt2):
        print("RAG created at...", self.timestamp_created)
        from langchain.callbacks.manager import CallbackManager
        from langchain_community.llms import LlamaCpp
        from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
        # Callbacks support token-wise streaming
        callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
        
        
        if self.vectorstore is None:
            self.vectorstore = load_or_create_vectorstore()

        from langchain.chains import LLMChain
        from langchain.prompts import PromptTemplate
        from langchain_core.prompts import ChatPromptTemplate
        

        # Prompt
        prompt = ChatPromptTemplate.from_template(
            #AppConfig.get_config().model.token_start+\
            AppConfig.get_config().model.token_user+\
            prompt1+\
            " {docs}"+\
            AppConfig.get_config().model.token_asistant
        )

        # Run
        question = prompt2
        docs = self.vectorstore.similarity_search(question, k=AppConfig.get_config().k_documents)
        for d in docs:
            print(d)
            print("-"*15)
        del self.vectorstore
        self.vectorstore = None

        if self.llm is None:
            if not os.path.exists(AppConfig.get_config().model.filename):
                r = requests.get(AppConfig.get_config().model.url)
                open(AppConfig.get_config().model.filename, "wb").write(r.content)
            self.llm = LlamaCpp(
                model_path=AppConfig.get_config().model.filename,
                temperature=AppConfig.get_config().model.temperature,
                max_tokens=AppConfig.get_config().model.max_tokens,
                n_ctx=AppConfig.get_config().model.n_context,
                top_p=AppConfig.get_config().model.top_p,
                callback_manager=callback_manager,
                verbose=True,  # Verbose is required to pass to the callback manager
            )

        # Chain
        
        def format_docs(docs):
            return "\n\n".join(doc.page_content for doc in docs)
        
        from langchain_core.output_parsers import StrOutputParser
        llm_chain = (
            {"docs": format_docs} 
            | prompt 
            | self.llm #.bind(stop=config.model.token_stop)
            | StrOutputParser()
            ) 
        result = llm_chain.invoke(docs)

        # Output
        print(result)
        return result, docs

if __name__ == "__main__":
    import sys
    from os.path import join
    import subprocess
    subprocess.run([sys.executable, join("webserver", "server.py")])