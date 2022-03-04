#Ver necessidade de matriz no trabalho
def supergenre_id_generator():
  len_list_supergenres = len(supergenres)
  next_number = len_list_supergenres + 1
  if next_number <= 9:
    return(f'G00{next_number}')
  elif next_number <= 99:
    return(f'G0{next_number}')
  elif next_number >99:
    return(f'G{next_number}')

supergenres = {'G001': 'Técnico',
              'G002': 'Infantil',
              'G003': 'Ficção'}

subgenres = {'G001': ['Computação', 'Cálculo','Física'],
            'G002': ['Contos','Fábulas'],
            'G003': ['Aventura','Mitologia']}

id_counter = -1

def id_generator():
  global id_counter
  id_counter += 1
  return id_counter
class Book:
  def __init__(self, supergenre = '',
                     subgenre = '',
                     title='', 
                     author='', 
                     year=0, 
                     publisher='', 
                     bio='', 
                     pgs_number=0, 
                     total_amount=0):

    self.id = id_generator()
    self.supergenre = supergenre
    self.subgenre = subgenre
    self.title = title
    self.author = author
    self.year = year
    self.publisher = publisher
    self.bio = bio
    self.pgs_number = pgs_number
    self.total_amount = total_amount
    self.leased_amount = 0
  
  def get_id(self) : return self.id
  def get_supergenre(self): return self.supergenre
  def get_subgenre(self): return self.subgenre
  def get_title(self) : return self.title
  def get_author(self): return self.author
  def get_year(self): return self.year
  def get_publisher(self): return self.publisher
  def get_bio(self): return self.bio
  def get_pgs_number(self): return self.pgs_number
  def get_total_amount(self): return self.total_amount
  def get_leased_amount(self): return self.leased_amount

  def set_supergenre(self, supergenre): self.supergenre = supergenre
  def set_subgenre(self, subgenre): self.subgenre = subgenre
  def set_title(self, title) : self.title = title
  def set_author(self, author): self.author = author
  def set_year(self, year): self.year = year
  def set_publisher(self, publisher): self.publisher = publisher
  def set_bio(self, bio): self.bio = bio
  def set_pgs_number(self, bio): self.pgs_number = bio
  def set_total_amount(self, total_amount): self.total_amount = total_amount
  def set_leased_amount(self, leased_amount): self.leased_amount = leased_amount
  
  def get_available_amount(self): return self.total_amount - self.leased_amount
