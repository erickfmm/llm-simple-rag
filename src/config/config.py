from .config_class import ModelCard, Config
import yaml
import os

class AppConfig:
    _config = None
    @classmethod
    def get_config(cls):
        if cls._config is not None:
            return cls._config
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), "configuration.yaml")), "r") as yobj:
            config_obj = yaml.safe_load(yobj)
            default_model = config_obj["models"][config_obj["default_model"]]
        cls._config = Config(
            model=ModelCard(
                TYPE=default_model["TYPE"],
                filename=default_model["filename"] if "filename" in default_model else None,
                url=default_model["url"] if "url" in default_model else None,
                n_context=default_model["n_context"] if "n_context" in default_model else None,
                temperature=default_model["temperature"] if "temperature" in default_model else config_obj["global_temperature"],
                max_tokens=default_model["max_tokens"] if "max_tokens" in default_model else None,
                num_return_sequences=default_model["num_return_sequences"] if "num_return_sequences" in default_model else None,
                top_k=default_model["top_k"] if "top_k" in default_model else None,
                top_p=default_model["top_p"],
                token_user=default_model["token_user"] if "token_user" in default_model else "",
                token_asistant=default_model["token_asistant"] if "token_asistant" in default_model else "",
                token_start=default_model["token_start"] if "token_start" in default_model else "",
                token_stop=default_model["token_stop"] if "token_stop" in default_model else ""
            ),
            huggingface_embeddings=config_obj["huggingface_embeddings"],
            huggingface_tokenizer=config_obj["huggingface_tokenizer"],
            splittokens_n=config_obj["splittokens_n"],
            splittokens_overlap=config_obj["splittokens_overlap"],
            chroma_path=config_obj["chroma_path"],
            data_folder=config_obj["data_folder"],
            k_documents=config_obj["k_documents"]
        )
        return cls._config
    
    @classmethod
    def reset_config(cls):
        cls._config = None
    
    @classmethod
    def put_config(cls, config: Config):
        cls._config = config
