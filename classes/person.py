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
  
  def get_birth_date(self): return self.birth_date
  
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
    self.max_number = 3
    
  def get_rented(self):
    return self.rented
  
  def get_max_number(self):
    return self.max_number
  	
  def set_rented(self, rented):
    self.rented = rented
   
  # book é um objeto 
  def rent(self, book):
    self.rented.append(book)
  
  def to_return(self, book):
    self.rented.remove(book)
    
class Student(Client):
  def __init__(self, name='', cpf='', birth_date='', password='', student_id_card=''):
    Client.__init__(self, name, cpf, birth_date, password)
    
    self.student_id_card = student_id_card
    self.max_number = 5
  
  def get_student_id_card(self):
    return self.student_id_card
  
  def set_student_id_card(self, student_id_card):
    self.student_id_card = student_id_card
    
    
# student = Student(name='Eduardo', cpf='03651138089', birth_date='18/07/2001', password='1234', student_id_card='000006')
# print(student.get_max_number())