from flask import flash, redirect
from classes.db import db
from classes.person import Student, Client

def client_create_validation(name, cpf, birth_date, password, student, student_id_card):
	if student == '1':
		if name == '' or cpf == '' or birth_date == '' or password == '' or student_id_card == '':
			flash('Campo(s) vazios!')
			return False
		
		else:
			user = ''
			for i in cpf:
				if i.isdigit():
					user+=i
					
			if len(user) != 11:
				flash('CPF inválido!')
				return False  
			
			elif len(student_id_card) != 6:
				flash('Carteirinha de estudante inválida! Digite os 6 dígitos.')
				return False
				
			else:
				db.add_people_to_dict(Student(name=name, cpf=user, birth_date=birth_date, password=password, student_id_card=student_id_card), 'students')  
				return True  
	else:
		if name == '' or cpf == '' or birth_date == '' or password == '':
			flash('Campo(s) vazios!')
			return False
		
		else:
			user = ''
			for i in cpf:
				if i.isdigit():
					user+=i
					
			if len(user) != 11:
				flash('CPF inválido!')
				return False  
		 
			else:
				db.add_people_to_dict(Client(name=name, cpf=user, birth_date=birth_date, password=password), 'clients')
				flash('Cliente cadastrado com sucesso!') 
				return True  
