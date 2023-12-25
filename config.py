

config_luna_Q2 = {
    "model_filename": "models/luna-ai-llama2-uncensored.Q2_K.gguf",
    "TOKEN_USER": "USER: ",
    "TOKEN_ASISTANT": "\nASSISTANT: ",
    "TOKEN_START": "",
    "TOKEN_STOP": None,
    "HuggingFaceEmbeddings": "dccuchile/bert-base-spanish-wwm-uncased",
    "chromadb_file": "./models/chroma_db",
    "data_folder": "data/drive-download-20231222T025931Z-001",
    "model_temperature": 0.3
}

config_mixtral_Q5 = {
    "model_filename": "models/mixtral-8x7b-instruct-v0.1.Q5_K_M.gguf",
    "TOKEN_USER": "[INST] ",
    "TOKEN_ASISTANT": " [/INST]",
    "TOKEN_START": "<s>",
    "TOKEN_STOP": "</s>",
    "HuggingFaceEmbeddings": "dccuchile/bert-base-spanish-wwm-uncased",
    "chromadb_file": "./models/chroma_db",
    "data_folder": "data/drive-download-20231222T025931Z-001",
    "model_temperature": 0.3
}

#Spanish
config_llama_es_Q2 = {
    "model_filename": "models/llama-2-7b-ft-instruct-es.Q2_K.gguf",
    "TOKEN_USER": "A continuación hay una instrucción que describe una tarea. Escriba una respuesta que complete adecuadamente la solicitud.\n### Instrucción:\n",
    "TOKEN_ASISTANT": "\n\n### Respuesta:",
    "TOKEN_START": "",
    "TOKEN_STOP": "",
    "HuggingFaceEmbeddings": "dccuchile/bert-base-spanish-wwm-uncased",
    "chromadb_file": "./models/chroma_db",
    "data_folder": "data/drive-download-20231222T025931Z-001",
    "model_temperature": 0.3
}
config_llama_es_Q5 = {
    "model_filename": "models/llama-2-7b-ft-instruct-es.Q2_K.gguf",
    "TOKEN_USER": "A continuación hay una instrucción que describe una tarea. Escriba una respuesta que complete adecuadamente la solicitud.\n### Instrucción:\n",
    "TOKEN_ASISTANT": "\n\n### Respuesta:",
    "TOKEN_START": "",
    "TOKEN_STOP": "",
    "HuggingFaceEmbeddings": "dccuchile/bert-base-spanish-wwm-uncased",
    "chromadb_file": "./models/chroma_db",
    "data_folder": "data/drive-download-20231222T025931Z-001",
    "model_temperature": 0.3
}
config_mixtral_es_Q5 = {
    "model_filename": "models/mixtral_spanish_ft.Q5_K_M.gguf",
    "TOKEN_USER": "<|user|>\n",
    "TOKEN_ASISTANT": "\n<|assistant|>",
    "TOKEN_START": "",
    "TOKEN_STOP": "",
    "HuggingFaceEmbeddings": "dccuchile/bert-base-spanish-wwm-uncased",
    "chromadb_file": "./models/chroma_db",
    "data_folder": "data/drive-download-20231222T025931Z-001",
    "model_temperature": 0.3
}

config = config_llama_es_Q2