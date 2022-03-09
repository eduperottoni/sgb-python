from email.policy import default
from app import app
from flask import render_template, request, flash, redirect

from classes.db import db
from classes.book import supergenres, subgenres
from app.utils.validations.book_rent_validation import rent_book_validation 
from app.utils.validations.book_return_validation import return_book_validation

from app.utils.validations.client_auth_validation import client_auth_validation
from app.utils.validations.client_create_validation import client_create_validation
from app.utils.validations.client_update_validation import client_update_validation
from app.utils.validations.client_delete_validation import client_delete_validation


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

#Rota de validação de login dos clientes e funcinários
@app.route('/auth/client', methods=['POST'])
def auth_client():
  if client_auth_validation('client', request.form.get('user'), request.form.get('password')):
    return redirect('/books')
  else:
  	return redirect('/login/client')

@app.route('/auth/student', methods=['POST'])
def auth_student():
  if client_auth_validation('student', request.form.get('user'), request.form.get('password')):
    return redirect('/books')
  else:
  	return redirect('/login/student') 
  	
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
  validation_dict = client_create_validation(request.form.get('name'), request.form.get('cpf'), request.form.get('birth_date'), request.form.get('password'), request.form.get('client-student') , request.form.get('student_id_card'))
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

@app.route('/profile')
def profile():
  if db.get_logged():
    usertype = db.get_usertype()
    user = db.get_user()
    return render_template('profile.html', user=user, usertype=usertype)
  else:
    return redirect('/')

@app.route('/rent/',  defaults={'book_id':None})
@app.route('/rent/<book_id>')
def rent(book_id):
  if db.get_logged():
    if book_id == None:
      redirect('/books')
    else:
      usertype = db.get_usertype()
      user = db.get_user()
      book=db.get_book_from_list(int(book_id))
      return render_template('rent.html', user=user, usertype=usertype, book=book)
  else:
    return redirect('/')

@app.route('/rent/validation/', defaults={'book_id':None})
@app.route('/rent/validation/<book_id>')
def rent_validation(book_id):
  if db.get_logged():
    if book_id == None:
      redirect('/books')
    else:
      usertype = db.get_usertype()
      user = db.get_user()
      book=db.get_book_from_list(int(book_id))
      validation_dict = rent_book_validation(book, user)
      while validation_dict['valid'] == False:
        flash(validation_dict['message'])
        return redirect(f'/rent/validation/{int(book_id)}')
      else:
        flash(validation_dict['message'])
        book.set_leased_amount(book.get_leased_amount()+1)
        return redirect('/books')
  else:
    return redirect('/')


@app.route('/return')
def to_return():
  if db.get_logged():
    usertype = db.get_usertype()
    user = db.get_user()
    return render_template('rented.html', user=user, usertype=usertype)
  else:
    return redirect('/')

@app.route('/return/', defaults={'book_id':None})
@app.route('/return/<book_id>')
def return_confirmation(book_id):
  if db.get_logged():
    if book_id == None:
      return redirect('/return')
    else:
      usertype = db.get_usertype()
      user = db.get_user()
      book = db.get_book_from_list(int(book_id))
      return render_template('return.html', user=user, usertype=usertype, book=book)
  else:
    return redirect('/')

@app.route('/return/validation/', defaults={'book_id':None})
@app.route('/return/validation/<book_id>')
def return_validation(book_id):
  if db.get_logged():
    if book_id == None:
      return redirect('/return')
    else:
      usertype = db.get_usertype()
      user = db.get_user()
      book = db.get_book_from_list(int(book_id))
      validation_dict = return_book_validation(book, user)
      flash(validation_dict['message'])
      return redirect('/return')
  else:
    return redirect('/')
