#6.8

pet_0 = {'Pies': 'Michał'}
pet_1 = {'Owca': 'Mateusz'}
pet_2 = {'Kot': 'Maciej'}

pets = [pet_0, pet_1, pet_2]

for pet in pets:
	print(pet)
	
for pet in pets:
	for k, v in pet.items():
		print(k, v)
