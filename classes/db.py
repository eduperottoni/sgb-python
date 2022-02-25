from classes.book import Book
from classes.publisher import Publisher
class DB():
  def __init__(self, books_list=[], user='', usertype='', people_list=[], publishers_list=[]):
    self.user = user
    self.usertype = usertype
    self.logged = False
    self.books_list = books_list
    self.person_list = people_list
    self.publishers_list = publishers_list

  
  def get_books_list(self):
    return self.books_list
  def add_books_to_list(self, book):
    self.books_list.append(book)
  def get_book_from_list(self, index):
    return self.books_list[index]

  def get_publishers_list(self):
    return self.publishers_list
  def add_publisher_to_list(self, publisher):
    self.publishers_list.append(publisher)
  def get_publisher_from_list(self, index):
    return self.publishers_list[index]

  def set_user(self, user):
    self.user = user
  def get_user(self):
    return self.user
  
  def set_usertype(self, usertype):
    self.usertype = usertype
  def get_usertype(self):
    return self.usertype

  def set_logged(self, logged):
    self.logged = logged
  def get_logged(self):
    return self.logged

db = DB()

editora1 = Publisher('Casa do Código', '54 58624518')
editora2 = Publisher('Editora UFSC', '54 92561185')
editora3 = Publisher('Editora POOI', '54 32569588')

livro1 = Book(supergener='G01',
              subgener='Computação',
              title='Introdução à Informática',
              author='Eduardo',
              year=2020,
              publisher=editora1,
              bio='Livro com uma Introdução aos conceitos fundamentais de informática',
              pgs_number=230,
              total_amount=10)

livro2 = Book(supergener='G01',
              subgener='Computação',
              title='Métodos de binários',
              author='Eduardo',
              year=2020,
              publisher=editora2,
              bio='Livro com uma Introdução aos conceitos fundamentais de informática',
              pgs_number=230,
              total_amount=10)

livro3 = Book(supergener='G01',
              subgener='Computação',
              title='Números binários e suas aplicações',
              author='Eduardo',
              year=2020,
              publisher=editora3,
              bio='Livro com uma Introdução aos conceitos fundamentais de informática',
              pgs_number=230,
              total_amount=10)

db.add_publisher_to_list(editora1)
db.add_publisher_to_list(editora2)
db.add_publisher_to_list(editora3)

db.add_books_to_list(livro1)
db.add_books_to_list(livro2)
db.add_books_to_list(livro3)


