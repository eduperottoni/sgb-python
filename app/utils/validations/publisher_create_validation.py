from classes.db import db

def publisher_create_validation(corp_name, phone):
  #Testando se os dados já existem
  publishers_list = db.get_publishers_list()
  for publisher in publishers_list:
    if publisher:
      if publisher.get_corp_name() == corp_name:
        return {'valid':False,'message':'Essa editora já está cadastrada :('}
      elif publisher.get_phone() == phone:
        return {'valid':False,'message':'Telefone repetido :('}  
  #Testando se os valores são válidos
  #Testando se estão vindo vazios
  if corp_name == '' or phone == '':
    return {'valid':False, 'message':'Campos vazios :('}
  #Testando se nome da editora tem mais de 3 dígitos
  elif (len(corp_name.strip()) < 3):
      return {'valid':False, 'message':'Nome de editora deve ter mais de 3 caracteres :('}
  #Testando se o telefone tem pelo menos 10 caracteres
  elif(len(phone.strip()) not in [10,11]):
    return {'valid':False,'message':'Telefone deve conter o DDD e o número :('}
  for i in phone:
    if not i.isdigit():
      return {'valid':False, 'message':'Telefone deve conter apenas números :('}
  return {'valid':True,'message':f'Editora {corp_name} criada :)'}
        


