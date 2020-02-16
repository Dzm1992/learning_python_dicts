favourite_language = {
	'janek': 'python',
	'sara': 'c',
	'edward': 'ruby',
	'paweł' : 'python',
	}


osoby = ['janek', 'sara', 'damian', 'tomek', 'paweł']




for k, v in favourite_language.items():
	if k in osoby:
		print("Ulubiony język programowania to " + k.title() + " to: " + v + "!")
	else:
		print(k.title() + ", zapraszamy do udziału w ankiecie!")



