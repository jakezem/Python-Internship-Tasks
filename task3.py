from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
  
def init_db():
  conn = sqlite3.connect('database.db')
  cursor = conn.cursor()
  cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      username TEXT NOT NULL,
      email TEXT NOT NULL,
      phone TEXT NOT NULL,
      password TEXT NOT NULL
    )
  ''')
  conn.commit()
  conn.close()

init_db()

@app.route('/')
def signup_form():
  return render_template('signup.html')

@app.route('/register', methods=['POST'])
def register():
  username = request.form['username']
  email = request.form['email']
  phone = request.form['phone']
  password = request.form['password']
  confirm_password = request.form['confirm_password']

  if not all([username, email, phone, password, confirm_password]):
    return "All fields are required!", 400

  if password != confirm_password:
    return "Passwords do not match!", 400

  conn = sqlite3.connect('database.db')
  cursor = conn.cursor()
  cursor.execute('''
    INSERT INTO users (username, email, phone, password)
    VALUES (?, ?, ?, ?)
    ''', (username, email, phone, password))
  conn.commit()
  conn.close()

  return redirect(url_for('success'))

@app.route('/success')
def success():
  return render_template('success.html')

if __name__ == '__main__':
  app.run(debug=True)
