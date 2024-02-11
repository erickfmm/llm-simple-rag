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
                filename=default_model["filename"],
                url=default_model["url"],
                n_context=default_model["n_context"],
                temperature=config_obj["global_temperature"],
                max_tokens=default_model["max_tokens"],
                top_p=default_model["top_p"],
                token_user=default_model["token_user"],
                token_asistant=default_model["token_asistant"],
                token_start=default_model["token_start"],
                token_stop=default_model["token_stop"]
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