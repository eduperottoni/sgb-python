from flask import flash, redirect
from classes.db import db

def employee_auth_validation(char, password):
	if char == '' or password == '':
		flash('Campo(s) vazios!')
		return False
	
	else:	
		user = ''
		for i in char:
			if i.isdigit():
				user+=i
				
		if len(user) != 5:
			flash('ID inválido!')
			return False
			
		else:
			for i in db.get_people_dict()['employees']:
				if user == i.get_employee_code() and password == i.get_password(): 
					db.set_usertype('employee')
					db.set_user(i)
					db.set_logged(True)
					return True

			flash('Id ou senha inválidos!')
			return False
