#Importação dos métodos do flask
from email.policy import default
from jinja2 import Undefined
from app import app
from flask import render_template, request, flash, redirect
#Importação das funções para cada página
from classes.db import db
from app.utils.validations.publisher_update_validation import publisher_update_validation
from app.utils.validations.employee_auth_validation import employee_auth_validation
from app.utils.validations.client_auth_validation import client_auth_validation
from app.utils.validations.client_create_validation import client_create_validation
from app.utils.validations.client_update_validation import client_update_validation

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
  #validar os dados do cliente. 
  if client_create_validation(request.form.get('name'), request.form.get('cpf'), request.form.get('birth_date'), request.form.get('password'), request.form.get('client-student'), request.form.get('student_id_card')):
    flash('Cliente criado com sucesso :)')
    return redirect('/clients/create')
  else:
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
  #validar os dados do cliente. Vai ter que pegar o índice para poder ter uma base 
  if client_update_validation(indice, client_type, request.form.get('name'), request.form.get('cpf'), request.form.get('birth_date'), request.form.get('password'), request.form.get('student_id_card')):
    flash('Cliente modificado com sucesso :)')
    return redirect('/clients')
  else:
    return redirect(f'/clients/update/{client_type}/{indice}')

    
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
    if book_id == None or int(book_id) > len(db.get_books_list())-1:
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

@app.route('/books/update/validation', methods=['POST'])
def book_update_validation():
  title = request.form.get('id-employee')
  password = request.form.get('password')
  #Fazer a validação de login de cliente abaixo em arquivo separado com as seguintes validações:
  
  # while user !='admin' and password !='1234@': #while user not in dicionário de clientes do banco:
  #   if user =='' and password=='':
  #     flash('Campos vazios :(')
  #   else:
  #     flash('Id de funcionário ou senha inválidos :(')
  #   # flash('Olá, tudo bem')
  #   return redirect('/login/employee')
  # else:
  #   db.set_usertype('employee')
  #   db.set_user(user)
  #   db.set_logged(True)
  #   flash('employee')
  #   return redirect('/main')

@app.route('/publishers')
def publishers():
  publishers_list = db.get_publishers_list()
  user = db.get_user()
  usertype = db.get_usertype()
  if (db.get_logged()):
    return render_template('publishers.html', publishers_list = publishers_list, usertype=usertype, user=user)
  else:
    return redirect('/')

@app.route('/publishers/update/', defaults={'publisher_id':None})
@app.route('/publishers/update/<publisher_id>')
def publisher_update(publisher_id):
  if db.get_logged():
    if publisher_id == None or int(publisher_id) > len(db.get_publishers_list())-1 :
      return redirect('/publishers')
    else:
      index = int(publisher_id)
      publisher = db.get_publisher_from_list(index)
      usertype = db.get_usertype()
      user = db.get_user()
      return render_template('publisher_update.html', publisher=publisher, usertype=usertype, user=user)
  else:
    return redirect('/index')

@app.route('/publishers/update/validation', methods=['POST'])
def publishers_update_validation():
  id = request.form.get('id')
  corp_name = request.form.get('corp-name')
  phone = request.form.get('phone')
  publishers_list = db.get_publishers_list()
  validation_dict = publisher_update_validation(id, corp_name, phone)
  while validation_dict['valid'] == False: #while user not in dicionário de clientes do banco:
    flash(validation_dict['message'])
    return redirect(f'/publishers/update/{id}')
  else:
    publishers_list[int(id)].set_corp_name(corp_name)
    publishers_list[int(id)].set_phone(phone)
    flash('Editora modificada')
    return redirect('/publishers')
    


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
