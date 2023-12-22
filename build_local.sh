sudo apt-get update
sudo apt-get install -y python3-pip gcc g++ libc6

python3 -m venv venv
source venv/bin/activate

pip3 install torch torchvision torchaudio
pip3 install -r requirements.txt

python3 ./load_things.py