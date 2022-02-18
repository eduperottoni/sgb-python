class DB():
  def __init__(self, lista_livros):
    self.lista_livros = lista_livros
  
  def get_lista_livros(self):
    return self.lista_livros

db = DB([])

