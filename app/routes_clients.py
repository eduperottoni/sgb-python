from email.policy import default
from app import app
from flask import render_template, request, flash, redirect

from classes.db import db
from classes.book import supergenres, subgenres
from app.utils.validations.book_rent_validation import rent_book_validation 
from app.utils.validations.book_return_validation import return_book_validation

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