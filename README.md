# llm-simple-rag
An experiment to build a simple RAG Application, capable of run any llamacpp-compatible LLM and any HuggingFace-compatible BERT Embedding/Sentence Transformer model. Using ChromaDB as VectorStore and Flask-SocketIO as Webserver.

# How to run

1. Download an LLM model according to README.md in models/ folder.
2. Change config.py according to the chosen model.
3. Install Docker
4. Run:
 * In Windows run `build_docker.bat` and `run_docker.bat`
 * In Linux/Other run `sh build_docker.sh` and `sh run_docker.sh`

# Screen shot
Screehshot
<img src="https://github.com/erickfmm/llm-simple-rag/blob/main/docs/capture.png?raw=true" alt="Screenshot"/>

# Diagrams
Sequence diagram of the App:
<img src="https://github.com/erickfmm/llm-simple-rag/blob/main/docs/sequence.png?raw=true" alt="Sequence diagram"/>


Class Diagram (without dependencies):
<img src="https://github.com/erickfmm/llm-simple-rag/blob/main/docs/class-simplified.png?raw=true" alt="Sequence diagram"/>

Class Diagram (with dependencies):
<img src="https://github.com//erickfmm/llm-simple-rag/blob/main/docs/class-full.png?raw=true" alt="Sequence diagram"/>

# TODO

- [ ] Pydoc documentation
- [ ] Config HTML View
- [x] Split Config and make a Class with Singleton
- [x] Download LLM models automatically
