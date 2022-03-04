from app import app
from flask import render_template, request, flash, redirect

from classes.db import db
from app.utils.validations.publisher_update_validation import publisher_update_validation
from app.utils.validations.publisher_delete_validation import publisher_delete_validation
from app.utils.validations.publisher_create_validation import publisher_create_validation
from app.utils.creations.create_publisher import create_publisher
from app.utils.updates.update_publisher import update_publisher
from app.utils.deletes.delete_publisher import delete_publisher

#Rota principal das editoras
@app.route('/publishers')
def publishers():
  publishers_list = db.get_publishers_list()
  user = db.get_user()
  usertype = db.get_usertype()
  if (db.get_logged()):
    return render_template('publishers.html', publishers_list = publishers_list, usertype=usertype, user=user)
  else:
    return redirect('/')

#Criação das editoras
@app.route('/publishers/create')
def publishers_create():
  user = db.get_user()
  usertype = db.get_usertype()
  if (db.get_logged()):
    return render_template('publisher_create.html', usertype=usertype, user=user)
  else:
    return redirect('/')

#Validação da criação
@app.route('/publishers/create/validation', methods=['POST'])
def publishers_create_validation():
  if db.get_logged():
    corp_name = request.form.get('corp-name')
    phone = request.form.get('phone')
    validation_dict = publisher_create_validation(corp_name, phone)
    while validation_dict['valid'] == False:
      flash(validation_dict['message'])
      return redirect('/publishers/create')
    else:
      create_publisher(corp_name, phone)
      flash(validation_dict['message'])
      return redirect('/publishers')
  else:
    return redirect('/')

#Update das editoras
@app.route('/publishers/update/', defaults={'publisher_id':None})
@app.route('/publishers/update/<publisher_id>')
def publishers_update(publisher_id):
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


#Validação do update das editoras
@app.route('/publishers/update/validation/', defaults={'publisher_id':None})
@app.route('/publishers/update/validation/<publisher_id>', methods=['POST'])
def publishers_update_validation(publisher_id):
  corp_name = request.form.get('corp-name')
  phone = request.form.get('phone')
  publisher = db.get_publisher_from_list(int(publisher_id))
  validation_dict = publisher_update_validation(publisher_id, corp_name, phone)
  while validation_dict['valid'] == False: #while user not in dicionário de clientes do banco:
    flash(validation_dict['message'])
    return redirect(f'/publishers/update/{publisher_id}')
  else:
    update_publisher(publisher, corp_name, phone)
    flash('Editora modificada :)')
    return redirect('/publishers')

#Delete das editoras 
@app.route('/publishers/delete/', defaults={'publisher_id':None})
@app.route('/publishers/delete/<publisher_id>')
def publisher_delete(publisher_id):
  if db.get_logged():
    if publisher_id == None or int(publisher_id) > len(db.get_publishers_list())-1 :
      return redirect('/publishers')
    else:
      index = int(publisher_id)
      publisher = db.get_publisher_from_list(index)
      usertype = db.get_usertype()
      user = db.get_user()
      return render_template('publisher_delete.html', publisher=publisher, usertype=usertype, user=user)
  else:
    return redirect('/index')

#Validação do delete das editoras
@app.route('/publishers/delete/validation/', defaults={'publisher_id':None})
@app.route('/publishers/delete/validation/<publisher_id>')
def publishers_delete_validation(publisher_id):
  validation_dict = publisher_delete_validation(int(publisher_id))
  while validation_dict['valid'] == False:
    flash(validation_dict['message'])
    return redirect(f'/publishers/delete/{publisher_id}')
  else:
    delete_publisher(publisher_id)
    flash(validation_dict['message'])
    return redirect('/publishers')