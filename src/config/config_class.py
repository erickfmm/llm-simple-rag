class ModelCard:
    def __init__(self, 
                 TYPE : str,
                 filename: str, 
                 url: str, 
                 n_context: int, 
                 temperature: float, 
                 max_tokens: int, 
                 num_return_sequences: int,
                 top_k: float,
                 top_p: float, 
                 token_user: str, 
                 token_asistant: str, 
                 token_start: str, 
                 token_stop: str):
        self.TYPE = TYPE
        self.filename = filename
        self.url = url
        self.n_context = n_context
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.num_return_sequences = num_return_sequences
        self.top_k = top_k
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
