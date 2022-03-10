#Importação dos métodos do flask
from flask import render_template, request, flash, redirect
# from contextlib import redirect_stderr

from app import app
from app import routes_books
from app import routes_clients
from app import routes_employees
from app import routes_publishers

#Importação das funções para cada página
from classes.db import db
from classes.book import supergenres, subgenres

from app.utils.validations.subgenre_create_validation import subgenre_create_validation
from app.utils.validations.supergenre_create_validation import supergenre_create_validation
from app.utils.creations.create_supergenre_subgenre import create_supergenre, create_subgenre

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

#Rota principal do sistema
@app.route('/main')
def main():
  user = db.get_user()
  username = db.get_username()
  usertype = db.get_usertype()
  if(db.get_logged()):
    return render_template('main.html', user=user, usertype=usertype, username=username)
  else:
    return redirect('/')

#Rota de logout
@app.route('/logout')
def logout():
  db.set_user('')
  db.set_usertype('')
  db.set_logged('')
  return redirect('/')

@app.route('/supergenre/create')
def supergenre_create():
  if db.get_logged():
      usertype = db.get_usertype()
      user = db.get_user()
      return render_template('supergenre_create.html', supergenres=supergenres, subgenres=subgenres, usertype=usertype, user=user)
  else:
    return redirect('/index')

@app.route('/supergenre/create/validation', methods=['POST'])
def supergenres_create_validation():
  if db.get_logged():
    supergenre = request.form.get('supergenre').title()
    subgenre = request.form.get('subgenre').title()
    validation_dict = supergenre_create_validation(supergenre, subgenre)
    while validation_dict['valid'] == False:
      flash(validation_dict['message'])
      return redirect('/supergenre/create')
    else:
      create_supergenre(supergenre, subgenre)
      flash(validation_dict['message'])
      return redirect('/books')
  else:
    return redirect('/')

@app.route('/subgenre/create')
def subgenre_create():
  if db.get_logged():
      usertype = db.get_usertype()
      user = db.get_user()
      return render_template('subgenre_create.html', supergenres=supergenres, subgenres=subgenres, usertype=usertype, user=user)
  else:
    return redirect('/index')

@app.route('/subgenre/create/validation', methods=['POST'])
def subgenres_create_validation():
  if db.get_logged():
    supergenre = request.form.get('supergenre')
    subgenre = request.form.get('subgenre').title()
    validation_dict = subgenre_create_validation(subgenre)
    while validation_dict['valid'] == False:
      print('oi')
      flash(validation_dict['message'])
      return redirect('/subgenre/create')
    else:
      create_subgenre(supergenre, subgenre)
      flash(validation_dict['message'])
      return redirect('/books')
  else:
    return redirect('/')
