from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
from flask_cors import CORS
import mysql.connector
from mysql.connector import errorcode
import time

import time
import os
def get_database_connection():
    max_retries = 5
    retries = 0

    while retries < max_retries:
        try:
            # Attempt to connect to the database
            conn = mysql.connector.connect(
                host="localhost",
                user='shekhar1',
                password='shekhar@143',
                database='sample_user',
                port=3306
            )

            # Check if the 'tasks' table exists, and create it if not
            cursor = conn.cursor()
            cursor.execute("SHOW TABLES LIKE 'tasks'")
            result = cursor.fetchone()

            if not result:
                cursor.close()  # Close the cursor before creating the table
                cursor = conn.cursor()  # Reopen the cursor after closing

                cursor.execute('''
                    CREATE TABLE tasks (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        task VARCHAR(255) NOT NULL,
                        due_date DATE NOT NULL
                    )
                ''')
                conn.commit()

            return conn, cursor

        except mysql.connector.Error as err:
            if err.errno == mysql.connector.errorcode.CR_SERVER_LOST or err.errno == mysql.connector.errorcode.CR_CONN_HOST_ERROR:
                # Handle server connection errors by retrying
                print(f"Retrying database connection... (Attempt {retries + 1}/{max_retries})")
                time.sleep(10)  # Wait for 5 minutes before retrying
                retries += 1
            else:
                # Handle other errors
                raise

    print("Max retries reached. Unable to connect to the database.")
    raise SystemExit


conn, cursor = get_database_connection()

app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = 'your_secret_key'


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
        # Get the database connection
        conn, cursor = get_database_connection()
        
        # Insert task into the database
        cursor.execute('INSERT INTO tasks (task, due_date) VALUES (%s, %s)', (task, due_date))
        
        # Commit the changes
        conn.commit()
        
        # Close the cursor
        cursor.close()

        flash('Task successfully added!', 'success')

    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    # Get the database connection
    conn, cursor = get_database_connection()
    
    # Delete task from the database
    cursor.execute('DELETE FROM tasks WHERE id = %s', (task_id,))
    
    # Commit the changes
    conn.commit()
    
    # Close the cursor
    cursor.close()

    return redirect(url_for('view_tasks'))

@app.route('/view_tasks')
def view_tasks():
    now = datetime.now()
    
    # Get the database connection
    conn, cursor = get_database_connection()

    # Execute the SELECT query
    cursor.execute('SELECT * FROM tasks')

    # Fetch all rows
    rows = cursor.fetchall()

    # Convert rows to a list of dictionaries
    tasks = [{'id': row[0], 'task': row[1], 'due_date': row[2]} for row in rows]

    for task in tasks:
        # Convert due_date to datetime.datetime type
        task['due_date'] = datetime.combine(task['due_date'], datetime.min.time())

        # Calculate remaining_time
        remaining_time = task['due_date'] - now
        task['remaining_time'] = remaining_time.days

    # Close the cursor
    cursor.close()

    return render_template('view_tasks.html', tasks=tasks, now=now)

if __name__ == '__main__':
    app.run(port=5004, host='0.0.0.0')
