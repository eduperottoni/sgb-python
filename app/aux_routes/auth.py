def auth_employee(user, password):
	if user =='' or password=='':
		flash('Campo(s) vazios :(')
		return redirect('/login/employee')
		
	elif len(password) != 5:
		flash('ID inválido!')
		return redirect('/login/employee')
		
	else:
		for i in db.get_people_dict()['employees']:
			if user == i.get_employee_code() and password == i.get_password(): 
				db.set_usertype('employee')
				db.set_user(i.get_name())
				db.set_logged(True)
				flash('employee')
				return redirect('/main')

		flash('Id de funcionário ou senha inválidos :(')
		return redirect('/login/employee')
