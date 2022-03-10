from classes.db import db
from classes.person import Employee

def employee_update_validation(user, name, code, cpf, birth_date, password, indice):
	#validação dos cpf de todos
	person_type = ["clients", "students"]
	for i in person_type:
		for person in db.get_people_dict()[i]:
			if person:
				if person.get_cpf() == cpf:
					return {'valid':False,'message':'Esse cpf já está cadastrado :('}
				
	employees_list = db.get_people_dict()['employees']
	if len(employees_list) != 0:
		index = -1
		for employee in employees_list:
			if employee == user:
				print("É o usuário logado!")
			index += 1
			if employee:
				if index == int(indice):
					pass
				elif employee.get_cpf() == cpf:
					return {'valid':False,'message':'Esse cpf já está cadastrado :('}
				elif employee.get_employee_code() == code:
				  return {'valid':False,'message':'Esse ID já está cadastrado :('}
	
	if name == '' or code == '' or cpf == '' or birth_date == '' or password == '':
		return{'valid':False, 'message':'Campos vazios :('}
	
	elif len(name.strip()) < 3:
		return{'valid':False, 'message':'Nome deve ter mais de 3 caracteres :('}
	
	else:
		user = ''
		for i in cpf:
			if i.isdigit():
				user+=i
				
		if len(user) != 11:
			return{'valid':False, 'message':'CPF inválido :('}
			
		elif len(code) != 5:
			return{'valid':False, 'message':'ID de funcionário inválido! Digite os 5 dígitos :('}
			
		else:
			client = db.get_people_dict()['employees'][int(indice)]
			client.set_name(name)
			client.set_cpf(user)
			client.set_birth_date(birth_date)
			client.set_password(password)
			client.set_employee_code(code)
				  
			return{'valid':True, 'message':'Funcionário atualizado com sucesso :)'}

