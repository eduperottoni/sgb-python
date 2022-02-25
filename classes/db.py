from classes.book import Book
from classes.publisher import Publisher
from classes.person import Student, Client, Employee

class DB():
  def __init__(self, books_list=[], user='', usertype='', people_dict={}, publishers_list=[]):
    self.user = user
    self.usertype = usertype
    self.logged = False
    self.books_list = books_list
    self.publishers_list = publishers_list
    self.people_dict = {'clients': [], 'students': [], 'employees': []}
  
  def get_books_list(self):
    return self.books_list
  def add_books_to_list(self, book):
    self.books_list.append(book)
  def get_book_from_list(self, index):
    return self.books_list[index]
    
  # esse ERROR é para quando alguém tentar se autenticar, mas ainda não existir ngm cadastrado  
  def get_people_dict(self):
    if (len(self.people_dict) == 0):
      return "ERROR"
    else:
      return self.people_dict

  def add_people_to_dict(self, person, t):
    self.people_dict[t].append(person)

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


estudante1 = Student(name='Eduardo', 
                     cpf='11111111111', 
                     birth_date='05-09-2001', 
                     password='1234@', 
                     student_id_card='000001')

estudante2 = Student(name='Fernanda', 
                     cpf='22222222222', 
                     birth_date='13-08-2001', 
                     password='@4321', 
                     student_id_card='000002')

cliente1 = Client(name='Lisete', 
                  cpf='33333333333', 
                  birth_date='12-12-1972', 
                  password='abcd#')
                  
cliente2 = Client(name='Elton', 
                  cpf='44444444444', 
                  birth_date='05-01-1968', 
                  password='#dcba')
                  
funcionario1 = Employee(name='Eduarda', 
               cpf='55555555555', 
               birth_date='16-11-1999', 
               password='123abc', 
               employee_code='00001')

funcionario2 = Employee(name='Tiago', 
               cpf='66666666666', 
               birth_date='04-01-1995', 
               password='abc123', 
               employee_code='00002')
               
               
db.add_people_to_list(estudante1, 'student')               
db.add_people_to_list(estudante2, 'student')               
db.add_people_to_list(cliente1, 'client')               
db.add_people_to_list(cliente2, 'client')               
db.add_people_to_list(funcionario1, 'employee')               
db.add_people_to_list(funcionario2, 'employee')               
