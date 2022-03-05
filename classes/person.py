class Person:
  def __init__(self, name, cpf, birth_date, password):
    self.name = name
    self.cpf = cpf
    self.birth_date = birth_date
    self.password = password

  def get_name(self):
    return self.name
   
  def get_cpf(self):
    return self.cpf
  
  def get_birth_date(self): 
    return self.birth_date
  
  def get_password(self):
    return self.password

  def set_name(self, name):
    self.name = name

  def set_cpf(self, cpf):
    self.cpf = cpf
    
  def set_birth_date(self, birth_date):
    self.birth_date = birth_date

  def set_password(self, password):
    self.password = password

class Employee(Person):
  def __init__(self, name='', cpf='', birth_date='', password='', employee_code=''):
    Person.__init__(self, name, cpf, birth_date, password)
    
    self.employee_code = employee_code
    
  def get_employee_code(self):
    return self.employee_code
      
  def set_employee_code(self, employee_code):
    self.employee_code = employee_code
    
class Client(Person):
  def __init__(self, name='', cpf='', birth_date='', password=''):
    Person.__init__(self, name, cpf, birth_date, password)
    
    self.rented = []

  def get_rented(self):
    return self.rented
    
  # def get_max_number():
  #   return 3
  	
  def set_rented(self, rented):
    self.rented = rented
  
  def has_books(self):
    if len(self.rented) > 0: return True
    else: return False
  		
  # book é um objeto 
  def rent(self, book):
    if len(self.rented) < 3:
      self.rented.append(book)
      return {'valid':True, 'message':'Livro alugado :)'}
    elif len(self.rented == 3):
      return {'valid':False,'message':'Número máximo de livros já alugados :('}
    elif book in self.rented:
      return {'valid':False, 'message':'Você já possui esse livro'}
  
  def to_return(self, book):
    self.rented.remove(book)
    
class Student(Client):
  def __init__(self, name='', cpf='', birth_date='', password='', student_id_card=''):
    Client.__init__(self, name, cpf, birth_date, password)
    
    self.student_id_card = student_id_card
  
  def get_student_id_card(self):
    return self.student_id_card
  
  # polimorfismo
  # def get_max_number():
  #   return 5
  
  def set_student_id_card(self, student_id_card):
    self.student_id_card = student_id_card

  # polimorfismo
  def rent(self, book):
    if len(self.rented) < 5:
      self.rented.append(book)
      return {'valid':True, 'message':'Livro alugado :)'}
    elif len(self.rented == 5):
      return {'valid':False,'message':'Número máximo de livros já alugados :('}
    elif book in self.rented:
      return {'valid':False, 'message':'Você já possui esse livro'}
