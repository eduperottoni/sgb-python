from classes.book import supergenres, subgenres, supergenre_id_generator

def create_supergenre(supergener, subgenre):
  id = supergenre_id_generator()
  supergenres[id] = supergener
  subgenres[id] = [subgenre]

def create_subgenre(supergener, subgenre):
  subgenres[supergener].append(subgenre)