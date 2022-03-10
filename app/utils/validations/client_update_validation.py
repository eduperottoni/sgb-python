from flask import flash, redirect
from classes.db import db
from classes.person import Student, Client

def client_update_validation(indice, client_type, name, cpf, birth_date, password, student_id_card=None):
	#validação dos cpf de todos
	person_type = ["employees", "clients", "students"]
	for i in person_type:
		for person in db.get_people_dict()[i]:
			if person:
				if person.get_cpf() == cpf and i != client_type:
					return {'valid':False,'message':'Esse CPF já está cadastrado :('}

	clients_list = db.get_people_dict()[client_type]
	if len(clients_list) != 0:
		index = -1
		for client in clients_list:
			index += 1
			if person.get_cpf() == cpf and index != int(indice):
				return {'valid':False,'message':'Esse CPF já está cadastrado :('}
			elif client_type == 'students':
				if client.get_student_id_card() == student_id_card and index != int(indice):
					return {'valid':False,'message':'Número de carteirinha repetido :('}  
	
	if client_type == 'students':
		if name == '' or cpf == '' or birth_date == '' or password == '' or student_id_card == '':
			return {'valid':False,'message':'Campo(s) vazios :('} 
		
		elif len(name.strip()) < 3:
			return{'valid':False, 'message':'Nome deve ter mais de 3 caracteres :('}
		
		else:
			user = ''
			for i in cpf:
				if i.isdigit():
					user+=i
					
			if len(user) != 11:
				return {'valid':False,'message':'CPF inválido :('}   
			
			elif len(student_id_card) != 6:
				return {'valid':False,'message':'Carteirinha de estudante inválida! Digite os 6 dígitos :('} 
		 		
			else:
				client = db.get_people_dict()[client_type][int(indice)]
				client.set_name(name)
				client.set_cpf(user)
				client.set_birth_date(birth_date)
				client.set_password(password)
				client.set_student_id_card(student_id_card)
				  
				return {'valid':True,'message':f'Cliente {name} modificado com sucesso :)'}  
				 
	else:
		if name == '' or cpf == '' or birth_date == '' or password == '':
			return {'valid':False,'message':'Campo(s) vazios :('} 
		
		else:
			user = ''
			for i in cpf:
				if i.isdigit():
					user+=i
					
			if len(user) != 11:
				return {'valid':False,'message':'CPF inválido :('} 
		 
			else:
				client = db.get_people_dict()[client_type][int(indice)]
				client.set_name(name)
				client.set_cpf(user)
				client.set_birth_date(birth_date)
				client.set_password(password)
				
				return {'valid':True,'message':f'Cliente {name} modificado com sucesso :)'}  
