from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from datetime import datetime

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from src.rag_model import RAG_Model

#def rag_model_function(prompt1, prompt2):
#    return "Hola mundo"
rag = None

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

def format_message(sender, message, docs):
    timestamp = datetime.now().strftime('%H:%M')
    if sender == 'user':
        return f'<div class="row user-message"><p class="message-timestamp mb-1">{timestamp}</p><p>{message}</p></div>'
    else:
        return f'<div class="row server-message"><p class="message-timestamp mb-1">{timestamp}</p><p>{message}<p><b>En base a los documentos:</b> <ol>{["<li>"+str(doc)+"</li>" for doc in docs]}</ol></p></p></div>'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/config')
def config():
    return render_template('config.html')

@socketio.on('connect')
def test_connect(auth):
    #emit('my response', {'data': 'Connected'})
    global rag
    rag = RAG_Model()

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')

@socketio.on('user_message')
def user_message(data):
    prompt1 = data['prompt1']
    prompt2 = data['prompt2']
    emit('chat_message', {'message': format_message('user', "<div>"+str(prompt1)+"\n<hr>\n"+str(prompt2)+"</div>", [])}, broadcast=True)
    response, docs = rag.rag_model_function(prompt1, prompt2)
    print("the docs are: ", docs)
    emit('chat_message', {'message': format_message('server', response, docs)}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)

