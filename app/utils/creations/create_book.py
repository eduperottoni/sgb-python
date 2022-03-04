from classes.book import Book
from classes.db import db

def create_book(title, publisher, author,year, supergenre, subgenre, bio, pgs_number, total_amount):
  book = Book(supergenre, subgenre, title, author, year, publisher, bio, pgs_number, total_amount)
  db.add_books_to_list(book)