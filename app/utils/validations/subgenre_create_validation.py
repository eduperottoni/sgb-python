from classes.book import subgenres

def subgenre_create_validation(subgenre):
  #Tem número no nome?
  has_numbers = False
  for i in subgenre:
    if i.isdigit():
      has_numbers = True
  #Subgênero já existe?
  exists = False
  for value in subgenres.values():
    if subgenre in value: 
      exists = True 
  #Campos vazios?  
  if subgenre == '':
    return {'valid':False, 'message':'Campos vazios :('}
  #Menos de 3 caracteres?
  elif len(subgenre.strip()) < 3:
    return {'valid':False, 'message':'Sub-gêneros devem possuir pelo menos 3 letras :('}
  elif has_numbers:
    return {'valid':False, 'message':'Nomes de sub-gêneros devem conter apenas letras :('}
  elif exists:
    return {'valid':False, 'message':'Sub-gênero já existe :('}
  else:
    return{'valid':True, 'message':f'Sub-gênero {subgenre} criado :)'}
