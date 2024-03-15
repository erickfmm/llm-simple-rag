from src.config.config import AppConfig
import requests
import os
import typing
from langchain_core.documents.base import Document


class Answer:
    def __init__(self):
        self.model = None
        self.tokenizer = None
        
    def answer_question_llamacpp(self, prompt: str, docs: typing.List[Document]) -> str:
        from langchain_core.prompts import ChatPromptTemplate
        from langchain.prompts import HumanMessagePromptTemplate, SystemMessagePromptTemplate
        # Prompt
        if AppConfig.get_config().model.default_prompt_asistant is not None:
            messages = [
                SystemMessagePromptTemplate.from_template(AppConfig.get_config().model.default_prompt_asistant),
                HumanMessagePromptTemplate.from_template(prompt+" {docs}")
            ]
        else:
            messages = [
                HumanMessagePromptTemplate.from_template(prompt+" {docs}")
            ]
        prompt = ChatPromptTemplate.from_messages(messages)
        print(prompt)

        from langchain.callbacks.manager import CallbackManager
        from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
        # Callbacks support token-wise streaming
        callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
        
        from langchain_community.llms import LlamaCpp
        if self.model is None:
            if not os.path.exists(AppConfig.get_config().model.filename):
                r = requests.get(AppConfig.get_config().model.url)
                open(AppConfig.get_config().model.filename, "wb").write(r.content)
            self.model = LlamaCpp(
                model_path=AppConfig.get_config().model.filename,
                temperature=AppConfig.get_config().model.temperature,
                max_tokens=AppConfig.get_config().model.max_tokens,
                n_ctx=AppConfig.get_config().model.n_context,
                top_p=AppConfig.get_config().model.top_p,
                callback_manager=callback_manager,
                verbose=True,  # Verbose is required to pass to the callback manager
            )

        # Chain
        from langchain_core.output_parsers import StrOutputParser
        if docs is None:
            llm_chain = (
                {"docs": lambda docs : ""} 
                | prompt 
                | self.model 
                | StrOutputParser()
                )
        else:
            llm_chain = (
                {"docs": lambda docs : "\n\n".join(doc.page_content for doc in docs)} 
                | prompt 
                | self.model 
                | StrOutputParser()
                ) 
        result = llm_chain.invoke(docs)
        # Output
        #print(result)
        return result

    #####################################################################################
    def answer_question_mt5(self, prompt: str, docs: typing.List[Document]) -> str:
        from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
        if self.model is None or self.tokenizer is None:
            model_name = AppConfig.get_config().model.filename
            model_tokenizer_name = AppConfig.get_config().model.filename
            self.tokenizer = AutoTokenizer.from_pretrained(model_tokenizer_name)
            self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name).to(AppConfig.get_config().runs_on) #puedes cambiar a 'cuda' si tienes GPU

        if docs is None:
            docs = ""

        input_text =f"{AppConfig.get_config().model.token_start}\
                      {AppConfig.get_config().model.token_user} \
                      {prompt} \
                      {docs} \
                      {AppConfig.get_config().model.token_asistant}"

        inputs = self.tokenizer(input_text, return_tensors="pt").to(AppConfig.get_config().runs_on) #puedes cambiar a 'cuda' si tienes GPU

        outputs = self.model.generate(inputs["input_ids"],
                                do_sample = True,
                                max_length = AppConfig.get_config().model.max_tokens, #puedes subir este parametro hasta 500
                                num_return_sequences=AppConfig.get_config().model.num_return_sequences, #recomiendo hasta 6 para que no demore mucho
                                top_k=AppConfig.get_config().model.top_k,
                                top_p=AppConfig.get_config().model.top_p,
                                )
        detok_outputs = [self.tokenizer.decode(x, skip_special_tokens=True) for x in outputs]

        #for output in detok_outputs: 
        #    print(output)
        #    print("\n") # imprime un salto de linea para separar cada uno de los outputs (en el caso que num_return_sequences sea mayor que 1)
        return "\n".join(detok_outputs)