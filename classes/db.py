class DB():
  def __init__(self, books_list=[], user='', usertype='', people_list=[]):
    self.user = user
    self.usertype = usertype
    self.logged = False
    self.books_list = books_list
    self.person_list = people_list
  
  def get_books_list(self):
    return self.lista_livros

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

class Livro():
  def __init__(self, autor, ano, tipo):
    self.autor = autor
    self.ano = ano
    self.tipo = tipo

db = DB()




