#Importação dos métodos do flask
from email.policy import default
from jinja2 import Undefined
from app import app
from flask import render_template, request, flash, redirect
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

#Rota de login de cliente
@app.route('/login/client')
def login_client():
  db.set_user('')
  db.set_usertype('')
  db.set_logged('')
  return render_template('login_client.html')

#Rota de login do funcionário
@app.route('/login/employee')
def login_employee():
  db.set_user('')
  db.set_usertype('')
  db.set_logged('')
  return render_template('login_employee.html')

#Rota de validação de login do cliente
@app.route('/auth/client', methods=['POST'])
def auth_client():
  user = request.form.get('user')
  password = request.form.get('password')
  #Fazer a validação de login de cliente abaixo em arquivo separado com as seguintes validações:
  # - VALIDADE DO CPF (Número de caracteres se está no banco)
  # - VALIDADE DA SENHA (Número de caracteres e se está no banco)
  while user !='admin' and password !='1234@': #while user not in dicionário de clientes do banco:
    if user =='' and password=='':
      flash('Campos vazios :(')
    else:
      flash('Usuário ou senha inválidos :(')
    # flash('Olá, tudo bem')
    return redirect('/login/client')
  else:
    db.set_usertype('client')
    db.set_user(user)
    db.set_logged(True)
    flash('client')
    return redirect('/main')

@app.route('/auth/employee', methods=['POST'])
def auth_employee():
  user = request.form.get('id-employee')
  password = request.form.get('password')
  #Fazer a validação de login de cliente abaixo em arquivo separado com as seguintes validações:
  # - VALIDADE DO CPF (Número de caracteres se está no banco)
  # - VALIDADE DA SENHA (Número de caracteres e se está no banco)
  while user !='admin' and password !='1234@': #while user not in dicionário de clientes do banco:
    if user =='' and password=='':
      flash('Campos vazios :(')
    else:
      flash('Id de funcionário ou senha inválidos :(')
    # flash('Olá, tudo bem')
    return redirect('/login/employee')
  else:
    db.set_usertype('employee')
    db.set_user(user)
    db.set_logged(True)
    flash('employee')
    return redirect('/main')

#Rota principal do sistema
@app.route('/main')
def main():
  user = db.get_user()
  usertype = db.get_usertype()
  if(db.get_logged()):
    return render_template('main.html', user=user, usertype=usertype)
  else:
    return redirect('/')

#Rota de visualização da lista de livros
@app.route('/books/view')
def show_books():
  return render_template('books_view.html')

#Rota de logout
@app.route('/logout')
def logout():
  db.set_user('')
  db.set_usertype('')
  db.set_logged('')
  return redirect('/')

#Rota de criação de livros
@app.route('/books')
def books():
  user = db.get_user()
  usertype = db.get_usertype()
  books_list = db.get_books_list()
  if db.get_logged():
    return render_template('books.html', usertype = usertype, books_list=books_list, user=user)
  else:
    return redirect('/index')

@app.route('/books/', defaults={'book_id':None})
@app.route('/books/<book_id>')
def book_details(book_id):
  if db.get_logged():
    if book_id == None or int(book_id) > len(db.get_books_list())-1 :
      return redirect('/books')
    else:
      index = int(book_id)
      book = db.get_book_from_list(index)
      usertype = db.get_usertype()
      user = db.get_user()
      return render_template('book_details.html', book=book, usertype=usertype, user=user)
  else:
    return redirect('/index')

@app.route('/books/update/', defaults={'book_id':None})
@app.route('/books/update/<book_id>')
def book_update(book_id):
  if db.get_logged():
    if book_id == None or int(book_id) > len(db.get_books_list())-1 :
      return redirect('/books')
    else:
      index = int(book_id)
      book = db.get_book_from_list(index)
      usertype = db.get_usertype()
      user = db.get_user()
      return render_template('book_update.html', book=book, usertype=usertype, user=user)
  else:
    return redirect('/index')

#HEADER DO FUNCIONÁRIO:
### Livros (alteração, criação e delete de livros)
### Clientes (alterar, criar e deletar clientes)
### Outros funcionários (alterar, criar, e deletar funcionários --> auth especial de admin)
### Logout do funcionário

#HEADER DO CLIENTE:
### Livros no main
### Devolução (lista de livros do cliente com opção de devolução)
### Perfil (alterar dados)
### Logout do cliente

# if user=='03651138089' and password=='1234@':
#   db.set_user(user)
#   return redirect('/index')
# else:
#   flash('Dados inválidos')
#   return redirect('/login')

# @app.route('/register')
# def cadastro():
#   if db.user == '03651138089':
#     return render_template('cadastro_livros.html')
#   else:
#     return 'Você não possui acesso de admin'

# @app.route('/auth_books', methods=['POST'])
# def print():
#   nome_livro = request.form.get('livro')
#   nome_autor = request.form.get('autor')
#   db.lista_livros.append([nome_autor, nome_livro])
#   return redirect('/books')

# @app.route('/books')
# def books():
#   lista_livros = db.get_lista_livros()
#   return render_template('books.html', data=lista_livros)




# @app.route('/logout')
# def logout():
#   db.set_user('')
#   return redirect('/index')