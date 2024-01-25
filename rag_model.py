from config import config

from vectorstore import load_or_create_vectorstore
from datetime import datetime


class RAG_Model():
    def __init__(self) -> None:
        self.timestamp_created = datetime.now()
        print("Creating RAG model... at", self.timestamp_created)
        self.vectorstore = None
        self.llm = None
        #self.vectorstore = load_or_create_vectorstore()

    def rag_model_function(self, prompt1, prompt2):
        print("RAG created at...", self.timestamp_created)
        from langchain.callbacks.manager import CallbackManager
        from langchain_community.llms import LlamaCpp
        from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
        # Callbacks support token-wise streaming
        callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
        
        
        # MY CODE:
        if self.vectorstore is None:
            self.vectorstore = load_or_create_vectorstore()
        ## END

        from langchain.chains import LLMChain
        from langchain.prompts import PromptTemplate
        from langchain_core.prompts import ChatPromptTemplate
        

        # Prompt
        #prompt = PromptTemplate.from_template(
        #    config["TOKEN_START"]+config["TOKEN_USER"]+prompt1+" {docs}"+config["TOKEN_ASISTANT"] #Summarize the main themes in these retrieved docs: 
        #)
        prompt = ChatPromptTemplate.from_template(
            config["TOKEN_START"]+config["TOKEN_USER"]+prompt1+" {docs}"+config["TOKEN_ASISTANT"]
        )

        # Run
        question = prompt2#"What are the approaches to Task Decomposition?"
        docs = self.vectorstore.similarity_search(question, k=3)
        for d in docs:
            print(d)
            print("-"*15)
        del self.vectorstore
        self.vectorstore = None

        if self.llm is None:
        #https://api.python.langchain.com/en/stable/llms/langchain.llms.llamacpp.LlamaCpp.html
            self.llm = LlamaCpp(
                model_path=config["model_filename"],
                temperature=config["model_temperature"],
                max_tokens=4098,
                n_ctx=4098,
                top_p=1,
                callback_manager=callback_manager,
                verbose=True,  # Verbose is required to pass to the callback manager
            )

        # Chain TODO: TEST
        #runnable = prompt | llm() | StrOutputParser()
        #result = runnable.invoke({"docs": docs})
        
        def format_docs(docs):
            return "\n\n".join(doc.page_content for doc in docs)
        # Chain Legacy
        #llm_chain = LLMChain(llm=self.llm, prompt=prompt)
        from langchain_core.output_parsers import StrOutputParser
        llm_chain = (
            {"docs": format_docs} 
            | prompt 
            | self.llm 
            | StrOutputParser()
            ) #.bind(stop=config["TOKEN_STOP"])
        result = llm_chain.invoke(docs)

        # Output
        print(result)
        return result, docs

if __name__ == "__main__":
    import sys
    from os.path import join
    import subprocess
    subprocess.run([sys.executable, join("webserver", "server.py")])