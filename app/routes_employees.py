from app import app
from flask import render_template, request, flash, redirect

from classes.db import db

from app.utils.validations.employee_auth_validation import employee_auth_validation
from app.utils.validations.employee_create_validation import employee_create_validation
from app.utils.validations.employee_update_validation import employee_update_validation
from app.utils.validations.employee_delete_validation import employee_delete_validation

from app.utils.validations.employee_special_auth_validation import employee_special_auth_validation

# mudar de outros funcionários para somente funcionários no menu
#

#Rota de login do funcionário
@app.route('/login/employee')
def login_employee():
  db.set_user('')
  db.set_usertype('')
  db.set_logged('')
  return render_template('login_employee.html')

@app.route('/auth/employee', methods=['POST'])
def auth_employee():
  if employee_auth_validation(request.form.get('id-employee'), request.form.get('password')):
    return redirect('/books')
  else:
  	return redirect('/login/employee')

@app.route('/employees')
def employees():
  user = db.get_user()
  usertype = db.get_usertype()
  people_dict = db.get_people_dict()
  
  if db.get_logged():
    return render_template('employees.html', usertype=usertype, people_dict=people_dict, user=user)
  else:
    return redirect('/index')
    
@app.route('/employees/special/auth/', defaults={'request_type':None, 'indice':None})
@app.route('/employees/special/auth/<request_type>/<indice>', methods=['POST', 'GET'])
def employees_special_auth(request_type, indice):
  user = db.get_user()
  print (user)
  usertype = db.get_usertype()
  people_dict = db.get_people_dict()
  
  return render_template('employees_special_auth.html', usertype=usertype, people_dict=people_dict, user=user, request_type=request_type, indice=indice)

@app.route('/employees/special/auth/validation/', defaults={'request_type':None, 'indice':None})
@app.route('/employees/special/auth/validation/<request_type>/<indice>', methods=['POST', 'GET'])
def employees_special_auth_validation(request_type, indice):
  validation_dict = employee_special_auth_validation(request.form.get('user'), request.form.get('password'))
 
  if validation_dict['valid']:
    return redirect(f'/employees/{request_type}/{indice}')
  else:
    flash(validation_dict['message'])
    return redirect(f'/employees/special/auth/{request_type}/{indice}')

@app.route('/employees/create/', defaults={'indice':None})
@app.route('/employees/create/<indice>')
def employees_create(indice):
  user = db.get_user()
  usertype = db.get_usertype()
  people_dict = db.get_people_dict()
  
  return render_template('employees_create.html', usertype=usertype, people_dict=people_dict, user=user)

@app.route('/employees/create/auth', methods=['POST'])
def employees_create_auth():
  validation_dict = employee_create_validation(request.form.get('name'), request.form.get('id'), request.form.get('cpf'), request.form.get('birth_date'), request.form.get('password'))
  if validation_dict['valid']:
    flash(validation_dict['message'])
    return redirect('/employees')
  else:
    flash(validation_dict['message'])
    return redirect(f'/employees/create/{None}')

@app.route('/employees/update/', defaults={'indice':None})
@app.route('/employees/update/<indice>')
def employees_update(indice):
  user = db.get_user()
  usertype = db.get_usertype()
  people_dict = db.get_people_dict()

  return render_template('employees_update.html', usertype=usertype, employee=db.get_people_dict()['employees'][int(indice)], user=user, indice=indice)

@app.route('/employees/update/auth/', defaults={'indice':None}) 
@app.route('/employees/update/auth/<indice>', methods=['POST'])
def employees_update_auth(indice):
  user = db.get_user()

  validation_dict = employee_update_validation(user, request.form.get('name'), request.form.get('id'), request.form.get('cpf'), request.form.get('birth_date'), request.form.get('password'), indice)
  if validation_dict['valid']:
    flash(validation_dict['message'])
    return redirect('/employees')
  else:
    flash(validation_dict['message'])
    return redirect(f'/employees/update/{indice}')
    
    
    
@app.route('/employees/delete/', defaults={'indice':None})
@app.route('/employees/delete/<indice>')
def employees_delete(indice):
  if db.get_logged():
    if indice == None:
      return redirect('/employees')
      
    for i in db.get_people_dict()['employees']:
      if i == db.get_people_dict()['employees'][int(indice)]:
        usertype = db.get_usertype()
        user = db.get_user()
        return render_template('employees_delete.html', indice=indice, employee=i, usertype=usertype, user=user)
   
  else:
    return redirect('/index')

@app.route('/employees/delete/auth/', defaults={'indice':None}) 
@app.route('/employees/delete/auth/<indice>', methods=['GET'])
def employees_delete_auth(indice):
  user = db.get_user()

  validation_dict = employee_delete_validation(user, indice)
  if validation_dict['valid']:
    db.delete_people_from_dict('employees', int(indice))
    flash(validation_dict['message'])
    return redirect('/employees')
  else:
    flash(validation_dict['message'])
    return redirect(f'/employees/delete/{indice}')
