from flask import Flask, url_for
from flask import Flask, flash, redirect, render_template, request, session, abort
from passlib.hash import sha256_crypt
import mysql.connector as mariadb
import os
import operator
import psycopg2
app = Flask(__name__)

conn = psycopg2.connect(
   database="StocksUserDB", user='postgres', password='ravindra@089', host='localhost', port= '5432'
)
#Setting auto commit false
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()













@app.route('/')
def home():
  if not session.get('logged_in'):
    return render_template('login.html')
  else:
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def do_admin_login():
  login = request.form

  userName = login['username']
  password = login['password']
  try:
    cursor.execute('SELECT * FROM useraccount WHERE email=%s and password=%s', (userName,password))
    session['logged_in'] = True
  except:
    flash('wrong password!')
  return home()

@app.route('/logout')
def logout():
  session['logged_in'] = False
  return home()

if __name__ == "__main__":
  app.secret_key = os.urandom(12)
  app.run(debug=False,host='0.0.0.0', port=5000)