from app import app
from flask import render_template, request, flash, redirect

from classes.db import db
from classes.book import supergenres, subgenres

from app.utils.creations.create_book import create_book
from app.utils.updates.update_book import update_book
from app.utils.validations.book_create_validation import book_create_validation
from app.utils.validations.book_update_validation import book_update_validation

#Rota principal dos livros
@app.route('/books')
def books():
  user = db.get_user()
  usertype = db.get_usertype()
  books_list = db.get_books_list()
  if db.get_logged():
    return render_template('books.html', supergenres=supergenres, usertype = usertype, books_list=books_list, user=user)
  else:
    return redirect('/index')

#Rota de detalhes de cada livro
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

#Rota de criação de livro - escolha de supergênero
@app.route('/books/create')
def books_create_supergenre():
  if db.get_logged():
    usertype = db.get_usertype()
    user = db.get_user()
    return render_template('book_create_supergenre.html', supergenres=supergenres, usertype=usertype, user=user)
  else:
    return redirect('/')

#Rota de criação de livro - escolha de subgênero
@app.route('/books/create/', defaults={'supergenre':None})
@app.route('/books/create/<supergenre>')
def books_create_subgenre(supergenre):
  if db.get_logged():
    if supergenre == None or supergenre not in supergenres.keys():
      return redirect('/books/create')
    else:
      subgenres_list = subgenres[supergenre]
      usertype = db.get_usertype()
      user = db.get_user()
      return render_template('book_create_subgenre.html', supergenre=supergenre, subgenres=subgenres_list, usertype=usertype, user=user)
  else:
    return redirect('/index')

#Rota de criação de livro - formulário
@app.route('/books/create/', defaults={'supergenre':None, 'subgenre_index':None})
@app.route('/books/create/<supergenre>/<subgenre_index>')
def books_create_form(supergenre, subgenre_index):
  subgenre_index = int(subgenre_index)
  if db.get_logged():
    is_valid = True
    if supergenre == None or supergenre not in supergenres.keys():
      is_valid = False
    else:
      if subgenre_index not in range (0,len(subgenres[supergenre])):
        is_valid = False
    if is_valid:
      usertype = db.get_usertype()
      user = db.get_user()
      publishers = db.get_publishers_list()
      return render_template('book_create_form.html',publishers=publishers, supergenres=supergenres, supergenre=supergenre, subgenre_index=subgenre_index, subgenre=subgenres[supergenre][subgenre_index], usertype=usertype, user=user)
    else:
      return redirect('/books/create')
  else:
    return redirect('/index')

#Rota de validação da criação do livro
@app.route('/books/create/', defaults={'supergenre':None, 'subgenre_index':None})
@app.route('/books/create/validation/<supergenre>/<subgenre_index>', methods=['POST'])
def books_create_validation(supergenre, subgenre_index):
  if db.get_logged():
    title = request.form.get('title')
    publisher_id= request.form.get('publisher')
    author = request.form.get('author')
    year = int(request.form.get('year'))
    bio = request.form.get('bio')
    pgs_number = int(request.form.get('pgs-number'))
    total_amount = int(request.form.get('total-amount'))
    validation_dict = book_create_validation(title, publisher_id, author, year, bio, pgs_number, total_amount)
    publishers = db.get_publishers_list()
    while validation_dict['valid'] == False:
      flash(validation_dict['message'])
      return redirect(f'/books/create/{supergenre}/{subgenre_index}')
    else:
      create_book(title, publishers[int(publisher_id)], author,year, supergenre, subgenres[supergenre][int(subgenre_index)], bio, pgs_number, total_amount)
      flash(validation_dict['message'])
      return redirect('/books')
  else:
    return redirect('/')

#Rota de update dos livros
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
      publishers = db.get_publishers_list()
      return render_template('book_update.html', publishers=publishers, book=book, usertype=usertype, user=user)
  else:
    return redirect('/index')

#Validação do update dos livros
@app.route('/books/update/validation/<book_id>', methods=['POST'])
def books_update_validation(book_id):
  if db.get_logged():
    book = db.get_book_from_list(int(book_id))
    title = request.form.get('title')
    publisher_id= request.form.get('publisher')
    author = request.form.get('author')
    year = int(request.form.get('year'))
    bio = request.form.get('bio')
    pgs_number = int(request.form.get('pgs-number'))
    total_amount = int(request.form.get('total-amount'))
    publisher = db.get_publisher_from_list(int(publisher_id))
    validation_dict = book_update_validation(book, title, publisher_id, author,year, bio, pgs_number, total_amount)
    while validation_dict['valid'] == False:
      flash(validation_dict['message'])
      return redirect(f'/books/update/{book.get_id()}')
    else:
      update_book(book, title, publisher, author,year, bio, pgs_number, total_amount)
      flash(validation_dict['message'])
      return redirect('/books')
  else:
    return redirect('/')