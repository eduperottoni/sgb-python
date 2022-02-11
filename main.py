from functions.show_menus import show_initial_menu
from functions.auth import auth_employee

# list = [{'titulo': 'teste 1234','autor':'Larissa'},
#         {'titulo': 'oi oi oi','autor':'Fernanda'},
#         {'titulo': 'te ste-test','autor':'Eduardo'},
#         {'titulo': 'te te-aut','autor':'Ana'},
#         {'titulo': 'tes gasd','autor':'Luciana'},
#         {'titulo': 'teca','autor':'Maria'}]

# busca = input('Digite sua busca: ')
# searched = []
# for i in list:
#   for x in i['titulo'].split():
#     if busca in x: 
#       if i not in searched : searched.append(i)
# print(searched)
user = 0; 

print('Seja bem vindo à Biblioteca!')
opcao = show_initial_menu()
if opcao == 1:
  user = auth_employee()
# elif opcao == 2:
#   #user = auth_student()
# else:
#   #user = auth_normal()


