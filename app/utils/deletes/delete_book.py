from classes.db import db

def delete_book(book_id):
  db.delete_book_from_list(book_id)
