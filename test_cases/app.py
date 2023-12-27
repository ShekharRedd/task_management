from flask import Flask, render_template, request, redirect, url_for , flash
from datetime import datetime, timedelta
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = 'your_secret_key'
# Sample in-memory database
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
        # flash('Task successfully added!', 'success')

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

@app.route('/chat')
def chat():
    return render_template('chat.html')

if __name__ == '__main__': # pragma: no cover
    app.run(port=5004,host='0.0.0.0')





# from flask import Flask, render_template, request, redirect, url_for, flash
# from datetime import datetime, timedelta
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)

# app.config['SECRET_KEY'] = 'your_secret_key'
# # Sample in-memory database
# tasks = []

# @app.route('/')
# def index():
#     now = datetime.now()
#     return render_template('index.html')

# @app.route('/add', methods=['POST'])
# def add():
#     task = request.form.get('task')
#     due_date_str = request.form.get('due_date')

#     if task and due_date_str:
#         due_date = datetime.strptime(due_date_str, '%Y-%m-%d')
#         tasks.append({'task': task, 'due_date': due_date})
#         # flash('Task successfully added!', 'success')

#     return redirect(url_for('view_tasks'))

# @app.route('/delete/<int:task_id>')
# def delete(task_id):
#     if 0 <= task_id < len(tasks):
#         del tasks[task_id]
#         # flash('Task successfully deleted!', 'success')
#     if not tasks:
#         return redirect(url_for('index'))
    
#     return redirect(url_for('view_tasks'))

# @app.route('/view_tasks')
# def view_tasks():
#     now = datetime.now()
#     return render_template('view_tasks.html', tasks=tasks, now=now)

# if __name__ == '__main__':
#     app.run(port=5004, host='0.0.0.0')


# from flask import Flask, render_template, request, redirect, url_for, flash
# from datetime import datetime
# from flask_cors import CORS
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# CORS(app)

# # Use SQLite as the database engine with a file named 'tasks.db' in the working directory
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SECRET_KEY'] = 'your_secret_key'
# db = SQLAlchemy(app)

# # Model for the Task table
# class Task(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     task = db.Column(db.String(255), nullable=False)
#     due_date = db.Column(db.DateTime, nullable=False)

# # Wrap the creation of database tables in the Flask application context
# with app.app_context():
#     # Create the database tables
#     db.create_all()

# @app.route('/')
# def index():
#     now = datetime.now()
#     return render_template('index.html')

# @app.route('/add', methods=['POST'])
# def add():
#     task_content = request.form.get('task')
#     due_date_str = request.form.get('due_date')

#     if task_content and due_date_str:
#         due_date = datetime.strptime(due_date_str, '%Y-%m-%d')
#         new_task = Task(task=task_content, due_date=due_date)
#         db.session.add(new_task)
#         db.session.commit()
#         flash('Task successfully added!', 'success')

#     return redirect(url_for('view_tasks'))

# @app.route('/delete/<int:task_id>')
# def delete(task_id):
#     task_to_delete = db.session.get(Task, task_id)
#     if task_to_delete:
#         db.session.delete(task_to_delete)
#         db.session.commit()
#         flash('Task successfully deleted!', 'success')

#     return redirect(url_for('view_tasks'))

# @app.route('/view_tasks')
# def view_tasks():
#     tasks = Task.query.all()  # Retrieve all tasks from the database
#     now = datetime.now()
#     return render_template('view_tasks.html', tasks=tasks, now=now)

# if __name__ == '__main__':
#     app.run(port=5004, host='0.0.0.0')



