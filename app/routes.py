#Importação dos métodos do flask
from app import app
from flask import render_template, request, flash, redirect
#Importação das funções para cada página

from classes.db import db

dicionario = []
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
def auth():
  user = request.form.get('user')
  password = request.form.get('password')
  #Fazer a validação de login de cliente abaixo em arquivo separado com as seguintes validações:
  # - VALIDADE DO CPF (Número de caracteres se está no banco)
  # - VALIDADE DA SENHA (Número de caracteres e se está no banco)
  while user !='admin' and password !='1234@':
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

#Rota principal do sistema
@app.route('/main')
def main():
  user = db.get_user()
  usertype = db.get_usertype()
  if(db.get_logged()):
    return render_template('main.html', user=user, usertype=usertype)
  else:
    return redirect('/')

#Rota de visualização da lista de livros disponíveis
@app.route('/show/books/view')
def show_books():
  return render_template('show_books_view.html')

#Rota de logout
@app.route('/logout')
def logout():
  db.set_user('')
  db.set_usertype('')
  db.set_logged('')
  return redirect('/')


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