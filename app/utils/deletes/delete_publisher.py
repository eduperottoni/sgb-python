from classes.db import db

def delete_publisher(publisher_id):
  publisher_id = int(publisher_id)
  db.delete_publisher_from_list(publisher_id)