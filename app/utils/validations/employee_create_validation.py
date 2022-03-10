from classes.db import db
from classes.person import Employee

def employee_create_validation(name, code, cpf, birth_date, password):
	#validação dos cpf de todos
	person_type = ["clients", "students"]
	for i in person_type:
		for person in db.get_people_dict()[i]:
			if person:
				if person.get_cpf() == cpf:
					return {'valid':False,'message':'Esse cpf já está cadastrado :('}
				
	employees_list = db.get_people_dict()['employees']
	if len(employees_list) != 0:
		for employee in employees_list:
			if employee:
				if employee.get_cpf() == cpf:
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
			db.add_people_to_dict(Employee(name=name, cpf=user, birth_date=birth_date, password=password, employee_code=code), 'employees')  
			return{'valid':True, 'message':'Funcionário cadastrado com sucesso :)'}

