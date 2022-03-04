from classes.db import db

def client_delete_validation(client_type, indice):
	client = db.get_people_dict()[client_type][int(indice)]
	
	if client.has_books():
		return {'valid': False, 'message':'Cliente possui livros alugados :('}

	else:
		return {'valid':True, 'message':f'Cliente {client.get_name()} excluído(a) :)'}
