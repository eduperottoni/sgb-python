from classes.book import Book
class DB():
  def __init__(self, books_list=[], user='', usertype='', people_list=[]):
    self.user = user
    self.usertype = usertype
    self.logged = False
    self.books_list = books_list
    self.person_list = people_list
  
  def get_books_list(self):
    return self.books_list
  def add_books_to_list(self, book):
    self.books_list.append(book)
  def get_book_from_list(self, index):
    return self.books_list[index]

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

livro1 = Book(supergener='01',
              subgener='Computação',
              title='Introdução à Informática',
              author='Eduardo',
              year=2020,
              publish_house='Casa do Código',
              bio='Livro com uma Introdução aos conceitos fundamentais de informática',
              pgs_number=230,
              total_amount=10)

livro2 = Book(supergener='01',
              subgener='Computação',
              title='Métodos de binários',
              author='Eduardo',
              year=2020,
              publish_house='Casa do Código',
              bio='Livro com uma Introdução aos conceitos fundamentais de informática',
              pgs_number=230,
              total_amount=10)

livro3 = Book(supergener='01',
              subgener='Computação',
              title='Números binários e suas aplicações',
              author='Eduardo',
              year=2020,
              publish_house='Casa do Código',
              bio='Livro com uma Introdução aos conceitos fundamentais de informática',
              pgs_number=230,
              total_amount=10)


print(livro2.get_id())
db.add_books_to_list(livro1)
db.add_books_to_list(livro2)
db.add_books_to_list(livro3)


