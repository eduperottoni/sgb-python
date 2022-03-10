from classes.db import db
from classes.publisher import Publisher

def create_publisher(corp_name, phone):
  publisher = Publisher(corp_name, phone)
  db.add_publisher_to_list(publisher)