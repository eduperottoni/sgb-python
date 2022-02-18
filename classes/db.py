class DB():
  def __init__(self, lista_livros, user):
    self.lista_livros = lista_livros
    self.user = user
  
  def get_lista_livros(self):
    return self.lista_livros

  def set_user(self, user):
    self.user = user
  def get_user(self):
    return self.user

class Livro():
  def __init__(self, autor, ano, tipo):
    self.autor = autor
    self.ano = ano
    self.tipo = tipo


db = DB([], '')




