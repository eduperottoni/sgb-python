from classes.db import db

def employee_delete_validation(user, indice):
	employees_list = db.get_people_dict()['employees']
	
	if user == employees_list[int(indice)]:
		return {'valid': False, 'message':f'Operação inválida, você está logado como {user.get_name()} :('}
	else:
		return {'valid':True, 'message':f'Funcionário(a) {employees_list[int(indice)].get_name()} excluído(a) :)'}
