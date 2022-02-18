#Importação dos métodos do flask
from app import app
from flask import render_template, request, flash, redirect
#Importação das funções para cada página
from app.aux_routes import aux_index
from app.aux_routes import aux_auth

dicioario = []

@app.route('/')
@app.route('/index')
def index():
  return aux_index.show_index()

@app.route('/cadastro')
def cadastro():
  return render_template('cadastro_livros.html')

@app.route('/login')
def login():
  return render_template('login.html')

@app.route('/auth', methods=['POST'])
def auth():
  return aux_auth.auth()