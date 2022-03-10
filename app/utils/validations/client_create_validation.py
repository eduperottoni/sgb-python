from classes.db import db
from classes.person import Student, Client

def client_create_validation(name, cpf, birth_date, password, is_student, student_id_card):
	if is_student == '1':
		client_type = 'students'
	else:
		client_type = 'clients'
	
	#validação dos cpf de todos	
	person_type = ['employees', 'clients', 'students']
	for i in person_type:
		for person in db.get_people_dict()[i]:
			if person:
				if person.get_cpf() == cpf and i != client_type:
					return {'valid':False,'message':'Esse CPF já está cadastrado :('}
				
	students_list = db.get_people_dict()['students']
	if len(students_list) != 0:
		for student in students_list:
			if student:
				if student.get_cpf() == cpf:
					return {'valid':False,'message':'Esse cpf já está cadastrado:('}
				elif student.get_student_id_card() == student_id_card:
					return {'valid':False,'message':'Número de carteirinha repetido :('}  
	
	clients_list = db.get_people_dict()['clients']
	if len(clients_list) != 0:
		for client in clients_list:
			if client:
				if client.get_cpf() == cpf:
					return {'valid':False,'message':'Esse CPF já está cadastrado:('}
	
	##estudantes				
	if client_type == 'students':
		if name == '' or cpf == '' or birth_date == '' or password == '' or student_id_card == '':
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
				
			elif len(student_id_card) != 6:
				return{'valid':False, 'message':'Carteirinha de estudante inválida! Digite os 6 dígitos :('}
				
			else:
				db.add_people_to_dict(Student(name=name.title(), cpf=user, birth_date=birth_date, password=password, student_id_card=student_id_card), 'students')  
				return{'valid':True, 'message':f'Estudante {name.title()} cadastrado com sucesso :)'}

	##clientes
	else:
		if name == '' or cpf == '' or birth_date == '' or password == '':
			return{'valid':False, 'message':'Campo(s) vazios :('}
		
		else:
			user = ''
			for i in cpf:
				if i.isdigit():
					user+=i
					
			if len(user) != 11:
				return{'valid':False, 'message':'CPF inválido :('}  
		 
			else:
				db.add_people_to_dict(Client(name=name.title(), cpf=user, birth_date=birth_date, password=password), 'clients')
				return{'valid':True, 'message':f'Cliente {name.title()} cadastrado com sucesso :)'}   
