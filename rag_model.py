
def rag_model_function(prompt1, prompt2):
    from vectorstore import load_or_create_vectorstore
    from langchain.callbacks.manager import CallbackManager
    from langchain.llms import LlamaCpp
    from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
    # Callbacks support token-wise streaming
    callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
    
    
    # MY CODE:
    vectorstore = load_or_create_vectorstore()
    ## END

    from langchain.chains import LLMChain
    from langchain.prompts import PromptTemplate

    # Prompt
    prompt = PromptTemplate.from_template(
        prompt1+" {docs}" #Summarize the main themes in these retrieved docs: 
    )

    #https://api.python.langchain.com/en/stable/llms/langchain.llms.llamacpp.LlamaCpp.html
    llm = LlamaCpp(
        model_path="/usr/src/app/models/luna-ai-llama2-uncensored.Q2_K.gguf",
        temperature=0.75,
        max_tokens=4098,
        n_ctx=4098,
        top_p=1,
        callback_manager=callback_manager,
        verbose=True,  # Verbose is required to pass to the callback manager
    )

    # Chain
    llm_chain = LLMChain(llm=llm, prompt=prompt)

    # Run
    question = prompt2#"What are the approaches to Task Decomposition?"
    docs = vectorstore.similarity_search(question, k=2, fetch_k=5)
    result = llm_chain(docs)

    # Output
    print(result["text"])
    return result["text"], docs

if __name__ == "__main__":
    import sys
    from os.path import join
    import subprocess
    subprocess.run([sys.executable, join("webserver", "server.py")])