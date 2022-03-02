from flask import flash, redirect
from classes.db import db
from classes.person import Student, Client

def client_update_validation(indice, client_type, name, cpf, birth_date, password, student_id_card=None):
	if client_type == 'students':
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
				client = db.get_people_dict()[client_type][int(indice)]
				client.set_name(name)
				client.set_cpf(user)
				client.set_birth_date(birth_date)
				client.set_password(password)
				client.set_student_id_card(student_id_card)
				  
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
				client = db.get_people_dict()[client_type][int(indice)]
				client.set_name(name)
				client.set_cpf(user)
				client.set_birth_date(birth_date)
				client.set_password(password)
				
				return True  
