from classes.db import db

def employee_delete_validation(user, indice):
	employees_list = db.get_people_dict()['employees']
	
	if len(employees_list) != 0:
		index = -1
		for employee in employees_list:
			if employee == user:
				return {'valid': False, 'message':f'Operação inválida, você está logado como {employee.get_name()} :('}
			
			index += 1
			if index == int(indice):
				return {'valid':True, 'message':f'Funcionário(a) {employee.get_name()} excluído(a) :)'}
