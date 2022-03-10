from classes.book import supergenres, subgenres

def supergenre_create_validation(supergenre, subgenre):
  #Tem número no nome?
  has_numbers = False
  for i in supergenre:
    if i.isdigit():
      has_numbers = True
  for i in subgenre:
    if i.isdigit():
      has_numbers = True
  #Gênero já existe?
  exists = False
  if supergenre in supergenres.values(): 
    exists = True 
  else:
    for value in subgenres.values():
      if subgenre in value: 
        exists = True 
  #Campos vazios?  
  if supergenre == '' or subgenre == '':
    return {'valid':False, 'message':'Campos vazios :('}
  #Menos de 3 caracteres?
  elif len(supergenre.strip()) < 3 or len(subgenre.strip()) < 3:
    return {'valid':False, 'message':'Gêneros devem possuir pelo menos 3 letras :('}
  elif has_numbers:
    return {'valid':False, 'message':'Nomes de gêneros devem conter apenas letras :('}
  elif exists:
    return {'valid':False, 'message':'Gênero e/ou sub-gênero já existe(m) :('}
  else:
    return{'valid':True, 'message':f'Gênero {supergenre} criado :)'}
