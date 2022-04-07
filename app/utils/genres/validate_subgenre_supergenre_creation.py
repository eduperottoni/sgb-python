from urllib import response
from classes.book import subgenres, supergenres
from app.utils.patterns.validations import has_empty_string, has_number, response_dict, shorter_than

def subgenre_create_validation(subgenre):
  already_exists = False
  for supergenre_id in subgenres.values():
    if subgenre in supergenre_id: 
      already_exists = True  
  if has_empty_string(subgenre):
    return response_dict(False, 'Campos vazios :(')
  elif shorter_than(subgenre, 3):
    return response_dict(False, 'Sub-gêneros devem possuir pelo menos 3 letras')
  elif has_number(subgenre):
    #PARAMOS AQUI
  
  
  
  
    return {'valid':False, 'message':'Nomes de sub-gêneros devem conter apenas letras :('}
  elif already_exists:
    return {'valid':False, 'message':'Sub-gênero já existe :('}
  else:
    return{'valid':True, 'message':f'Sub-gênero {subgenre} criado :)'}

def supergenre_create_validation(supergenre, subgenre):
  already_exists = False
  if supergenre in supergenres.values(): 
    already_exists = True 
  else:
    for supergenre_id in subgenres.values():
      if subgenre in supergenre_id: 
        already_exists = True 
  #Campos vazios?  
  if has_empty_string([supergenre, subgenre]):
    return {'valid':False, 'message':'Campos vazios :('}
  #Menos de 3 caracteres?
  elif len(supergenre.strip()) < 3 or len(subgenre.strip()) < 3:
    return {'valid':False, 'message':'Gêneros devem possuir pelo menos 3 letras :('}
  elif has_number(supergenre) or has_number(subgenre):
    return {'valid':False, 'message':'Nomes de gêneros devem conter apenas letras :('}
  elif already_exists:
    return {'valid':False, 'message':'Gênero e/ou sub-gênero já existe(m) :('}
  else:
    return{'valid':True, 'message':f'Gênero {supergenre} criado :)'}
