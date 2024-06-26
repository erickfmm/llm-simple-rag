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
                 default_prompt_asistant: str,
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
        self.default_prompt_asistant = default_prompt_asistant
        self.token_user = token_user
        self.token_asistant = token_asistant
        self.token_start = token_start
        self.token_stop = token_stop

class Config:
    def __init__(self, 
                 model: ModelCard, 
                 huggingface_embeddings: str, 
                 tokenizer_model: str, 
                 tokenizer : str,
                 regex_preprocessing: str,
                 splittokens_n: int, 
                 splittokens_overlap: int,
                 percentage_length_low : float,
                 percentage_length_up: float,
                 chroma_path: str,
                 data_folder: str,
                 data_file: str,
                 data_file_column: str,
                 k_documents: int,
                 runs_on: str):
        self.model = model
        self.huggingface_embeddings = huggingface_embeddings
        self.tokenizer_model = tokenizer_model
        self.splittokens_n = splittokens_n
        self.splittokens_overlap = splittokens_overlap
        self.percentage_length_low = percentage_length_low
        self.percentage_length_up = percentage_length_up
        self.chroma_path = chroma_path
        self.data_file = data_file
        self.data_file_column = data_file_column
        self.data_folder = data_folder
        self.k_documents = k_documents
        self.tokenizer = tokenizer
        self.regex_preprocessing = regex_preprocessing
        self.runs_on = runs_on
