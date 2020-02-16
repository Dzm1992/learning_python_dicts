#6.9

favourite_places = {
	'Adam': ['Berlin', 'Warszawa', 'Poznan'],
	'Jacek': ['Chojnice', 'Hajnowka', 'Bydgoszcz'],
	'Ola': ['Gdansk', 'Gdynia', 'Sopot'],
	}


for osoba in favourite_places:
	print('\n' + osoba + ":")
	for miejsce in favourite_places[osoba]:
		print(miejsce)
