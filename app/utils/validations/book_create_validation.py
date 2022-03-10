from classes.db import db

def book_create_validation(title, publisher, author, year, bio, pgs_number, total_amount):
  exists = False
  for book in db.get_books_list():
    if book:
      if book.get_title() == title:
        exists = True
  has_numbers = False
  for i in author:
    if i.isdigit():
      has_numbers = True
  #Campos vazios?
  if title == '' or publisher == '' or author == '' or bio == '' or pgs_number == '' or total_amount == '':
    return {'valid' : False, 'message' : 'Campos vazios :('}
  #Título já existe?
  elif exists:
    return {'valid': False, 'message':'Título já existe na biblioteca :('}
  #Título tem menos de 3 letras?
  elif len(title.strip()) < 3:
    return {'valid':False, 'message':'Título não pode ter menos de 3 caracteres :('}
  #Autor tem números no nome:
  elif has_numbers:
    return{'valid':False, 'message':'Nome do autor deve conter apenas letras :('}
  #Autor tem menos de 3 letras?
  elif len(author.strip()) < 3:
    return {'valid':False, 'message':'Nome do autor deve ter ao menos 3 letras :('}
  #Ano é maior que o ano atual ou negativo?
  elif int(year) not in range(0,2023):
    return {'valid':False, 'message':'Ano inválido :('}
  #Bio tem menos de 20 caracteres?
  elif len(bio.strip()) < 20:
    return {'valid':False, 'message':'Bio deve ter ao menos 20 caracteres :('}
  #Número de páginas maior que 3000?
  elif int(pgs_number) not in range (1,3001):
    return {'valid':False, 'message':'Número de páginas inválido :('}
  elif int(total_amount) not in range (1,100):
    return {'valid':False, 'message':'Quantidade disponível deve estar entre 1 e 100 :('}
  else:
    return {'valid':True, 'message':f'Livro {title} cadastrado com sucesso :)'}
  