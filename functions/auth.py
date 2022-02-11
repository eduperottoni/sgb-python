employees = {'001': {'password': '1234@', 'name':'Luciana'} }

def auth_employee():
  id_empl = input('Insira o seu id de Funcionário:') 
  passw = input('Insira a sua senha: ')
  while True:
    if (not id_empl in employees.keys()):
      print('[ERRO] ID ou senha inválidos...')
      id_empl = input('Insira o seu id de Funcionário:') 
      passw = input('Insira a sua senha: ')
    elif (not employees[id_empl]['password'] == passw):
      print('[ERRO] ID ou senha inválidos...')
      id_empl = input('Insira o seu id de Funcionário:') 
      passw = input('Insira a sua senha: ')
    else:
      break
  print(f'Log in realizado! Bem vindo, {employees[id_empl]["name"]}')
  return {'nome':f'{employees[id_empl]["name"]}',
          'id':f'{id_empl}'}
    