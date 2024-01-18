# llm-simple-rag
An experiment to build a simple RAG Application, capable of run any llamacpp-compatible LLM and any HuggingFace-compatible BERT Embedding/Sentence Transformer model. Using ChromaDB as VectorStore and Flask-SocketIO as Webserver.

# How to run

1. Download an LLM model according to README.md in models/ folder.
2. Change config.py according to the chosen model.
3. Install Docker
4. Run:
 * In Windows run `build_docker.bat` and `run_docker.bat`
 * In Linux/Other run `sh build_docker.sh` and `sh run_docker.sh`

# Diagrams
Sequence diagram of the App:

![Sequence diagram](https://github.com//erickfmm/llm-simple-rag/blob/master/docs/sequence.png?raw=true)

Class Diagram (without dependencies):

![Class Diagram (without dependencies)](https://github.com//erickfmm/llm-simple-rag/blob/master/docs/class-simplified.png?raw=true)


Class Diagram (with dependencies):

![Class Diagram (with dependencies)](https://github.com//erickfmm/llm-simple-rag/blob/master/docs/class-full.png?raw=true)

# TODO

* Pydoc documentation
* Config HTML View
* Split Config and make a Class with Singleton
* Download LLM models automatically
