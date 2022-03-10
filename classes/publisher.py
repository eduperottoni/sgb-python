id_counter = -1
def id_generator():
  global id_counter
  id_counter += 1
  return id_counter

class Publisher():
  def __init__(self, corp_name, phone):
    self.id = id_generator()
    self.corp_name = corp_name
    self.phone = phone
  
  def get_id(self): return self.id
  def get_corp_name(self) : return self.corp_name
  def get_phone(self) : return self.phone

  def set_corp_name(self,corp_name): self.corp_name = corp_name
  def set_phone(self, phone): self.phone = phone