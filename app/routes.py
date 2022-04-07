#Importação dos métodos do flask
from flask import render_template, request, flash, redirect
# from contextlib import redirect_stderr

from app import app
from app import routes_geners
from app import routes_books
from app import routes_clients
from app import routes_employees
from app import routes_publishers

#Importação das funções para cada página
from classes.db import db



#Rota inicial
@app.route('/')
@app.route('/index')
def index():
  db.set_user('')
  db.set_logged('')
  db.set_usertype('')
  return render_template('index.html')

#Rota de escolha do tipo de login
@app.route('/login')
def login():
  db.set_user('')
  db.set_usertype('')
  db.set_logged('')
  return render_template('login.html')

#Rota de logout
@app.route('/logout')
def logout():
  db.set_user('')
  db.set_usertype('')
  db.set_logged('')
  return redirect('/')
