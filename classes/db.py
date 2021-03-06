from classes.book import Book
from classes.publisher import Publisher
from classes.person import Student, Client, Employee

class DB():
  def __init__(self, books_list=[], user='', username='', usertype='', publishers_list=[]):
    self.user = user
    self.logged = False
    self.username = username
    self.usertype = usertype
    self.books_list = books_list
    self.publishers_list = publishers_list
    self.people_dict = {'clients': [], 'students': [], 'employees': []}
    
    self.special_auth = {'user': 'admin', 'password': 'admin'}

  def get_user(self): return self.user
  def get_logged(self): return self.logged
  def get_username(self): return self.username
  def get_usertype(self): return self.usertype
  def get_books_list(self): return self.books_list
  def get_people_dict(self): return self.people_dict
  def get_publishers_list(self): return self.publishers_list

  def set_user(self, user): self.user = user
  def set_logged(self, logged): self.logged = logged
  def set_username(self, username): self.username = username
  def set_usertype(self, usertype): self.usertype = usertype
  
  def add_books_to_list(self, book): self.books_list.append(book)
  def get_book_from_list(self, index): return self.books_list[index]
  def delete_book_from_list(self, index): self.books_list[index] = ''
  
  def get_people_from_dict(self, client_type, index): return self.people_dict[client_type][index]
  def add_people_to_dict(self, person, key): self.people_dict[key].append(person)
  def delete_people_from_dict(self, client_type, index): self.people_dict[client_type][index] = ''

  def add_publisher_to_list(self, publisher): self.publishers_list.append(publisher)
  def delete_publisher_from_list(self, publisher_id): self.publishers_list[publisher_id] = ''
  def get_publisher_from_list(self, index): return self.publishers_list[index]

db = DB()

editora1 = Publisher('Casa do Código', '5458624518')
editora2 = Publisher('Editora UFSC', '5492561185')
editora3 = Publisher('Editora POOI', '5432569588')

livro1 = Book(supergenre='G001',
              subgenre='Computação',
              title='Introdução à Informática',
              author='Eduardo',
              year=2020,
              publisher=editora1,
              bio='Livro com uma Introdução aos conceitos fundamentais de informática',
              pgs_number=230,
              total_amount=10)

livro2 = Book(supergenre='G001',
              subgenre='Computação',
              title='Métodos de binários',
              author='Eduardo',
              year=2020,
              publisher=editora2,
              bio='Livro com uma Introdução aos conceitos fundamentais de informática',
              pgs_number=230,
              total_amount=10)

livro3 = Book(supergenre='G002',
              subgenre='Fábulas',
              title='Branca de Neve',
              author='Eduardo',
              year=2010,
              publisher=editora2,
              bio='A história de uma princesa da Disney',
              pgs_number=55,
              total_amount=10)

db.add_publisher_to_list(editora1)
db.add_publisher_to_list(editora2)
db.add_publisher_to_list(editora3)

db.add_books_to_list(livro1)
db.add_books_to_list(livro2)
db.add_books_to_list(livro3)


estudante1 = Student(name='Eduardo', 
                     cpf='11111111111', 
                     birth_date='2001-05-09', 
                     password='1234@', 
                     student_id_card='000001')

estudante2 = Student(name='Fernanda', 
                     cpf='22222222222', 
                     birth_date='2001-08-13', 
                     password='@4321', 
                     student_id_card='000002')

cliente1 = Client(name='Lisete', 
                  cpf='33333333333', 
             	     birth_date='1972-12-12', 
                  password='abcd#')
                  
cliente2 = Client(name='Elton', 
                  cpf='44444444444', 
                  birth_date='1968-05-01', 
                  password='#dcba')
                  
funcionario1 = Employee(name='Eduarda', 
               cpf='55555555555', 
               birth_date='1999-11-11', 
               password='123abc', 
               employee_code='00001')

funcionario2 = Employee(name='Tiago', 
               cpf='66666666666', 
               birth_date='1995-04-01', 
               password='abc123', 
               employee_code='00002')
               
               
db.add_people_to_dict(estudante1, 'students')               
db.add_people_to_dict(estudante2, 'students')               
db.add_people_to_dict(cliente1, 'clients')               
db.add_people_to_dict(cliente2, 'clients')               
db.add_people_to_dict(funcionario1, 'employees')               
db.add_people_to_dict(funcionario2, 'employees')               
