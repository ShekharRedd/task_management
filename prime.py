# app.py

from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime, timedelta
from flask_cors import CORS
from flask_socketio import SocketIO

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app)

app.config['SECRET_KEY'] = 'your_secret_key'
tasks = []

@app.route('/')
def index():
    now = datetime.now()
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    due_date_str = request.form.get('due_date')

    if task and due_date_str:
        due_date = datetime.strptime(due_date_str, '%Y-%m-%d')
        tasks.append({'task': task, 'due_date': due_date})

    now = datetime.now()
    return render_template('view_tasks.html', tasks=tasks, now=now)

@app.route('/delete/<int:task_id>')
def delete(task_id):
    if 0 <= task_id < len(tasks):
        del tasks[task_id]
    if not tasks:
        return redirect(url_for('index'))
    return redirect(url_for('view_tasks'))

@app.route('/view_tasks')
def view_tasks():
    now = datetime.now()
    return render_template('view_tasks.html', tasks=tasks, now=now)

# New route for chat
@app.route('/chat')
def chat():
    return render_template('chat.html')

# SocketIO event handler for chat
@socketio.on('message')
def handle_message(msg):
    print('Received message: ' + msg)
    socketio.emit('message', msg, broadcast=True)

if __name__ == '__main__':
    # Run the app with SocketIO support
    socketio.run(app, port=5004, debug=True, host='0.0.0.0')
