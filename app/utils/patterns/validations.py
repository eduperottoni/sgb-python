def has_number(string):
	for i in string:
		if i.isdigit():
			return True
	return False

def has_empty_string(list):
	for string in list:
		if string == '':
			return True
	return False

def shorter_than(string, number):
	if len(string.strip()) < number:
		return True
	return False

def response_dict(valid, message):
	return {'valid':valid, 'message':message}