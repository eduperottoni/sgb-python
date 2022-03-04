#Importação dos métodos do flask
# from contextlib import redirect_stderr
from app import app
from app import routes_publishers
from app import routes_books

from flask import render_template, request, flash, redirect

#Importação das funções para cada página
from classes.db import db
from classes.book import supergenres, subgenres

from app.utils.validations.supergenre_create_validation import supergenre_create_validation
from app.utils.validations.subgenre_create_validation import subgenre_create_validation

from app.utils.creations.create_supergenre_subgenre import create_supergenre, create_subgenre
from app.utils.validations.employee_auth_validation import employee_auth_validation
from app.utils.validations.client_auth_validation import client_auth_validation
from app.utils.validations.client_create_validation import client_create_validation
from app.utils.validations.client_update_validation import client_update_validation
from app.utils.validations.client_delete_validation import client_delete_validation

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

#Rota de login de cliente
@app.route('/login/client')
def login_client():
  db.set_user('')
  db.set_usertype('')
  db.set_logged('')
  return render_template('login_client.html')

#Rota de login de cliente
@app.route('/login/student')
def login_student():
  db.set_user('')
  db.set_usertype('')
  db.set_logged('')
  return render_template('login_student.html')

#Rota de login do funcionário
@app.route('/login/employee')
def login_employee():
  db.set_user('')
  db.set_usertype('')
  db.set_logged('')
  return render_template('login_employee.html')

#Rota de validação de login dos clientee e funcinários
@app.route('/auth/client', methods=['POST'])
def auth_client():
  if client_auth_validation('client', request.form.get('user'), request.form.get('password')):
    return redirect('/main')
  else:
  	return redirect('/login/client')

@app.route('/auth/student', methods=['POST'])
def auth_student():
  if client_auth_validation('student', request.form.get('user'), request.form.get('password')):
    return redirect('/main')
  else:
  	return redirect('/login/student') 

@app.route('/auth/employee', methods=['POST'])
def auth_employee():
  if employee_auth_validation(request.form.get('id-employee'), request.form.get('password')):
    return redirect('/main')
  else:
  	return redirect('/login/employee')

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
    
#Para o CRUD de clientes
@app.route('/clients')
def clients():
  user = db.get_user()
  usertype = db.get_usertype()
  people_dict = db.get_people_dict()
  
  if db.get_logged():
    return render_template('clients.html', usertype=usertype, people_dict=people_dict, user=user)
  else:
    return redirect('/index')
    
#Para o create de clientes
@app.route('/clients/create')
def clients_create():
  user = db.get_user()
  usertype = db.get_usertype()
  people_dict = db.get_people_dict()
  
  return render_template('clients_create.html', usertype=usertype, people_dict=people_dict, user=user)

@app.route('/clients/create/auth', methods=['POST'])
def clients_create_auth():
  validation_dict = client_create_validation(request.form.get('name'), request.form.get('cpf'), request.form.get('birth_date'), request.form.get('password'), request.form.get('client-student'), request.form.get('student_id_card'))
  if validation_dict['valid']:
    flash(validation_dict['message'])
    return redirect('/clients')
  else:
    flash(validation_dict['message'])
    return redirect('/clients/create')

@app.route('/clients/update', defaults={'client_type':None, 'indice':None})
@app.route('/clients/update/<client_type>/<indice>')
def clients_update(client_type, indice):
  if db.get_logged():
    if indice == None:
      return redirect('/clients')

    for i in db.get_people_dict()[client_type]:
      if i == db.get_people_dict()[client_type][int(indice)]:
        usertype = db.get_usertype()
        user = db.get_user()
        return render_template('clients_update.html', client_type=client_type, indice=indice, client=i, usertype=usertype, user=user)
   
  else:
    return redirect('/index')

@app.route('/clients/update/', defaults={'client_type':None, 'indice':None})
@app.route('/clients/update/<client_type>/<indice>/auth', methods=['POST'])
def clients_update_auth(client_type, indice):
  validation_dict = client_update_validation(indice, client_type, request.form.get('name'), request.form.get('cpf'), request.form.get('birth_date'), request.form.get('password'), request.form.get('student_id_card'))
  if validation_dict['valid']:
    flash(validation_dict['message'])
    return redirect('/clients')
  else:
    flash(validation_dict['message'])
    return redirect(f'/clients/update/{client_type}/{indice}')
    
@app.route('/clients/delete/', defaults={'client_type':None, 'indice':None})
@app.route('/clients/delete/<client_type>/<indice>')
def clients_delete(client_type, indice):
  if db.get_logged():
    if indice == None:
      return redirect('/clients')
      
    for i in db.get_people_dict()[client_type]:
      if i == db.get_people_dict()[client_type][int(indice)]:
        usertype = db.get_usertype()
        user = db.get_user()
        return render_template('clients_delete.html', client_type=client_type, indice=indice, client=i, usertype=usertype, user=user)
   
  else:
    return redirect('/index')

@app.route('/clients/delete/', defaults={'client_type':None, 'indice':None})
@app.route('/clients/delete/<client_type>/<indice>/auth')
def clients_delete_auth(client_type, indice):
  validation_dict = client_delete_validation(client_type, indice)
  if validation_dict['valid']:
    db.delete_people_from_dict(client_type, int(indice))
    flash(validation_dict['message'])
    return redirect('/clients')
  else:
    return redirect(f'/clients/delete/{client_type}/{indice}')
   
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
