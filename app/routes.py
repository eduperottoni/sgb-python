#Importação dos métodos do flask
from app import app
from flask import render_template, request, flash, redirect
#Importação das funções para cada página

from classes.db import db

dicionario = []

@app.route('/')
@app.route('/index')
def index():
  return render_template('index.html', nome=db.user)

@app.route('/register')
def cadastro():
  if db.user == '03651138089':
    return render_template('cadastro_livros.html')
  else:
    return 'Você não possui acesso de admin'

@app.route('/auth_books', methods=['POST'])
def print():
  nome_livro = request.form.get('livro')
  nome_autor = request.form.get('autor')
  db.lista_livros.append([nome_autor, nome_livro])
  return redirect('/books')

@app.route('/books')
def books():
  lista_livros = db.get_lista_livros()
  return render_template('books.html', data=lista_livros)

@app.route('/login')
def login():
  return render_template('login.html')

@app.route('/auth_person', methods=['POST'])
def auth():
  user = request.form.get('user')
  password = request.form.get('password')
  if user=='03651138089' and password=='1234@':
    db.set_user(user)
    return redirect('/index')
  else:
    flash('Dados inválidos')
    return redirect('/login')

