from classes.db import db

def publisher_update_validation(id, corp_name, phone):
  publishers_list = db.get_publishers_list()
  repeated_name = False
  repeated_phone = False
  for i in publishers_list:
    if i != publishers_list[int(id)]:
      if i.corp_name == corp_name:
        repeated_name = True
      if i.phone == phone:
        repeated_phone = False
  if (len(corp_name.strip()) < 3) or repeated_name:
    return {'valid':False, 'message':'Nome de editora inválido :('}
  elif (len(phone.strip()) < 8) or repeated_phone:
    return {'valid':False, 'message':'Telefone inválido :('}
  else:
    return {'valid':True, 'message':''}