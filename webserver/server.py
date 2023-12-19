from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from datetime import datetime

def rag_model_function(prompt1, prompt2):
    return "Hola mundo"


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

def format_message(sender, message):
    timestamp = datetime.now().strftime('%H:%M')
    if sender == 'user':
        return f'<div class="row user-message"><p class="message-timestamp mb-1">{timestamp}</p><p>{message}</p></div>'
    else:
        return f'<div class="row server-message"><p class="message-timestamp mb-1">{timestamp}</p><p>{message}</p></div>'

@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('user_message')
def user_message(data):
    prompt1 = data['prompt1']
    prompt2 = data['prompt2']
    emit('chat_message', {'message': format_message('user', "<div>"+str(prompt1)+"\n<hr>\n"+str(prompt2)+"</div>")}, broadcast=True)
    response = rag_model_function(prompt1, prompt2)
    emit('chat_message', {'message': format_message('server', response)}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)

