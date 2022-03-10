from classes.db import db

def employee_special_auth_validation(user, password):
	if user == db.special_auth['user'] and user == db.special_auth['password']:
		return {'valid':True}
	elif user == '' or password == '':
		return {'valid':False, 'message':'Campos vazios :('}
	else:
		return {'valid':False, 'message':'User ou senha incorretos :('}
