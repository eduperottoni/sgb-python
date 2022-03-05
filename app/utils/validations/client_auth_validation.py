from flask import flash, redirect
from classes.db import db

def client_auth_validation(type, char, password):
	if char == '' or password == '':
		flash('Campo(s) vazios :(')
		return False
	
	else:
		user = ''
		for i in char:
			if i.isdigit():
				user+=i
				
		if len(user) != 11:
			flash('CPF inválido :(')
			return False  
	 
		else:
			if db.get_people_dict()[(type+"s")]:
				for i in db.get_people_dict()[(type+"s")]:
					if user == i.get_cpf() and password == i.get_password(): 
						db.set_usertype(type)
						db.set_user(i)
						db.set_logged(True)
						return True

				flash('Usuário ou senha inválidos :(')
				return False  
