# app.py
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# This will store messages temporarily. In a real-world application, you'd use a database.
messages = []

@app.route('/')
def index():
    return render_template('index.html', messages=messages)

@socketio.on('message')
def handle_message(data):
    username = data['username']
    message = data['message']
    timestamp = datetime.now().strftime('%m/%d/%y %I:%M %p')  # Adjusted timestamp format
    messages.append({'username': username, 'message': message, 'timestamp': timestamp})
    emit('new_message', {'username': username, 'message': message, 'timestamp': timestamp}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)
