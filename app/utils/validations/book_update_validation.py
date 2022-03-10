from classes.db import db

def book_update_validation(book, title, publisher, author, year, bio, pgs_number, total_amount):
  exists = False
  for i in db.get_books_list():
    if i:
      if i.get_title() == title and i.get_id() != book.get_id():
        exists = True
  has_numbers = False
  for i in author:
    if i.isdigit():
      has_numbers = True
  #Campos vazios?
  if title == '' or publisher == '' or author == '' or bio == '' or pgs_number == '' or total_amount == '':
    return {'valid' : False, 'message' : 'Campos vazios :('}
  #Título já existe em outro livro?
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
  elif year not in range(0,2023):
    return {'valid':False, 'message':'Ano inválido :('}
  #Bio tem menos de 20 caracteres?
  elif len(bio.strip()) < 20:
    return {'valid':False, 'message':'Bio deve ter ao menos 20 caracteres :('}
  #Número de páginas maior que 3000?
  elif pgs_number not in range (1,3001):
    return {'valid':False, 'message':'Número de páginas inválido :('}
  elif total_amount not in range (1,100):
    return {'valid':False, 'message':'Quantidade total deve estar entre 1 e 100 :('}
  elif total_amount < book.get_leased_amount():
    return {'valid':False, 'message':f'Quantidade total deve estar entre {book.get_leased_amount()} e 100 :('}
  else:
    return {'valid':True, 'message':f'Livro {title} alterado com sucesso :)'}