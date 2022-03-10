from flask import flash, redirect
from classes.db import db

def employee_auth_validation(char, password):
	if char == '' or password == '':
		return {'valid':False, 'message':'Campo(s) vazios :('}
	
	else:	
		user = ''
		for i in char:
			if i.isdigit():
				user+=i
				
		if len(user) != 5:
			return {'valid':False, 'message':'ID inválido :('}
			
		else:
			for i in db.get_people_dict()['employees']:
				if i:
					if user == i.get_employee_code() and password == i.get_password(): 
						db.set_usertype('employee')
						db.set_user(i)
						db.set_logged(True)
						return {'valid':True}

			return {'valid':False, 'message':'Id ou senha inválidos :('}
