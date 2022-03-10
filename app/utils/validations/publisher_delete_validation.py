from classes.db import db

def publisher_delete_validation(publisher_id):
  books_list = db.get_books_list()
  publisher = db.get_publisher_from_list(publisher_id)
  for book in books_list:
    if book.get_publisher() == publisher:
      return {'valid': False, 'message':'Existem livros dessa editora :('}
  return {'valid':True, 'message':f'Editora {publisher.get_corp_name()} excluída :)'}
