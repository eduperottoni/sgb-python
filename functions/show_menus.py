def show_initial_menu():
  print('-'*40)
  print('Faça seu login')
  print('-'*40)
  print('[1] Log in funcionário')
  print('[2] Log in estudante')
  print('[3] Log in normal')
  tipo = input('Tipo de Log in: ')
  while( tipo not in ['1','2','3']):
    print('Não entendemos sua escolha! Tente novamente...')
    tipo = input('Tipo de Log in: ')
  return int(tipo)

