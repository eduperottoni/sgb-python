from classes.db import db
def book_delete_validation(book):
  if book.get_leased_amount() > 0:
    return {'valid':False, 'message':'O livro está alugado :('}
  else:
    return {'valid':True, 'message':f'Livro {book.get_title()} deletado :)'}

