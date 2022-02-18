class Pessoa():
  def __init__(self, name, cpf, birth_date, password):
    self.name = name
    self.cpf = cpf
    self.birth_date = birth_date
    self.password = password
  
  def get_name(self):
    return self.name

  def set_name(self,name):
    self.name = name

  def get_cpf(self):
    return self.cpf
  
  def set_cpf(self,cpf):
    self.cpf = cpf





eduardo = Pessoa('Eduardo', '03651138089','18/07/2001','edu1234@')

print(eduardo.name)