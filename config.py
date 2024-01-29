
class ModelCard:
    def __init__(self, 
                 filename: str, 
                 url: str, 
                 n_context: int, 
                 temperature: float, 
                 max_tokens: int, 
                 top_p, 
                 token_user: str, 
                 token_asistant: str, 
                 token_start: str, 
                 token_stop: str):
        self.filename = filename
        self.url = url
        self.n_context = n_context
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.top_p = top_p
        self.token_user = token_user
        self.token_asistant = token_asistant
        self.token_start = token_start
        self.token_stop = token_stop

class Config:
    def __init__(self, 
                 model: ModelCard, 
                 huggingface_embeddings: str, 
                 huggingface_tokenizer: str, 
                 splittokens_n: int, 
                 splittokens_overlap: int, 
                 chroma_path: str,
                 data_folder: str,
                 k_documents: int):
        self.model = model
        self.huggingface_embeddings = huggingface_embeddings
        self.huggingface_tokenizer = huggingface_tokenizer
        self.splittokens_n = splittokens_n
        self.splittokens_overlap = splittokens_overlap
        self.chroma_path = chroma_path
        self.data_folder = data_folder
        self.k_documents = k_documents

_huggingface_embeddings = "dccuchile/bert-base-spanish-wwm-uncased"
_huggingface_tokenizer = "dccuchile/bert-base-spanish-wwm-uncased"
_splittokens_n = 500
_splittokens_overlap = 15
_chroma_path = "./models/chroma_db"
_data_folder = "data/curriculum nacional txt extracted"
_global_temperature = 0.3

models = {
    "luna_Q2": ModelCard(filename="models/luna-ai-llama2-uncensored.Q2_K.gguf",
                          url="https://huggingface.co/TheBloke/Luna-AI-Llama2-Uncensored-GGUF/resolve/main/luna-ai-llama2-uncensored.Q2_K.gguf",
                          n_context=4098,
                          temperature=_global_temperature,
                          max_tokens=4098,
                          top_p=1,
                          token_user="USER: ",
                          token_asistant="\nASSISTANT: ",
                          token_start="",
                          token_stop=""),
    "mixtral_Q5": ModelCard(filename="models/mixtral-8x7b-instruct-v0.1.Q5_K_M.gguf",
                            url="https://huggingface.co/TheBloke/Mixtral-8x7B-Instruct-v0.1-GGUF/raw/main/mixtral-8x7b-instruct-v0.1.Q5_K_M.gguf",
                            n_context=4098,
                            temperature=_global_temperature,
                            max_tokens=4098,
                            top_p=1,
                            token_user="[INST] ",
                            token_asistant=" [/INST]",
                            token_start="<s>",
                            token_stop="</s>"),
    #Spanish
    "llama_es_Q2": ModelCard(filename="models/llama-2-7b-ft-instruct-es.Q2_K.gguf",
                          url="https://huggingface.co/TheBloke/Llama-2-7B-ft-instruct-es-GGUF/resolve/main/llama-2-7b-ft-instruct-es.Q2_K.gguf",
                          n_context=4098,
                          temperature=_global_temperature,
                          max_tokens=4098,
                          top_p=1,
                          token_user="[INST] ",
                          token_asistant=" [/INST]",
                          token_start="<s>",
                          token_stop="</s>"),
    "llama_es_Q5": ModelCard(filename="models/llama-2-7b-ft-instruct-es.Q5_K_M.gguf",
                          url="https://huggingface.co/TheBloke/Llama-2-7B-ft-instruct-es-GGUF/resolve/main/llama-2-7b-ft-instruct-es.Q5_K_M.gguf",
                          n_context=4098,
                          temperature=_global_temperature,
                          max_tokens=4098,
                          top_p=1,
                          token_user="A continuación hay una instrucción que describe una tarea. Escriba una respuesta que complete adecuadamente la solicitud.\n### Instrucción:\n",
                          token_asistant="\n\n### Respuesta:",
                          token_start="",
                          token_stop=""),
    "mixtral_es_Q5": ModelCard(filename="models/mixtral_spanish_ft.Q5_K_M.gguf",
                          url="https://huggingface.co/TheBloke/mixtral_spanish_ft-GGUF/resolve/main/mixtral_spanish_ft.Q5_K_M.gguf",
                          n_context=4098,
                          temperature=_global_temperature,
                          max_tokens=4098,
                          top_p=1,
                          token_user="<|user|>\n",
                          token_asistant="\n<|assistant|>",
                          token_start="",
                          token_stop=""),
    "tinyllama_Q5": ModelCard(filename="models/tinyllama-1.1b-chat-v1.0.Q5_K_M.gguf",
                          url="https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/raw/main/tinyllama-1.1b-chat-v1.0.Q5_K_M.gguf",
                          n_context=2048,
                          temperature=_global_temperature,
                          max_tokens=512,
                          top_p=1,
                          token_user="<|system|>\nSigue las instrucciones</s>\n<|user|>\n",
                          token_asistant="\n<|assistant|>",
                          token_start="",
                          token_stop="")
                            
}

config = Config(model=models["tinyllama_Q5"],
                huggingface_embeddings=_huggingface_embeddings,
                huggingface_tokenizer=_huggingface_tokenizer,
                splittokens_n=_splittokens_n,
                splittokens_overlap=_splittokens_overlap,
                chroma_path=_chroma_path,
                data_folder=_data_folder,
                k_documents=3)