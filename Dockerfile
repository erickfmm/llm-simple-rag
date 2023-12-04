FROM ubuntu:22.04

WORKDIR /usr/src/app

RUN apt-get update
RUN apt-get install -y python3-pip gcc g++ libc6

RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
RUN pip install langchain langchain-experimental llama-cpp-python sentence_transformers chromadb beautifulsoup4

COPY . .

RUN python3 ./load_things.py

CMD [ "python3", "./basic_rag.py" ]