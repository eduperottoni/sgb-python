from classes.db import db

def publisher_update_validation(id, corp_name, phone):
  publishers_list = db.get_publishers_list()
  repeated_name = False
  repeated_phone = False
  for publisher in publishers_list:
    if publisher:
      if publisher != publishers_list[int(id)]:
        if publisher.corp_name == corp_name:
          repeated_name = True
        if publisher.phone == phone:
          repeated_phone = False
  for i in phone:
    if not i.isdigit():
      return {'valid':False, 'message':'Telefone deve conter apenas números'}
  if (len(corp_name.strip()) < 3) or repeated_name:
    return {'valid':False, 'message':'Nome de editora inválido :('}
  elif (len(phone.strip()) not in [10,11]) or repeated_phone:
    return {'valid':False, 'message':'Telefone inválido :('}
  else:
    return {'valid':True, 'message':''}