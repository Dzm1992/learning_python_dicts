#6.1
person = {'first_name': 'Damian', 'last_name': 'Osiecki', 'age': 27, 'city': 'Bydgoszcz'}
print(person)
print('first_name')
print('last_name')
print('age')
print('city')

#6.2
print('\n')

liczba = {
	'Damian': '7', 
	'Przemek': '2', 
	'Tomek': '27', 
	'Kamil': '100', 
	'Mateusz': '321'
	}
print(liczba)

#6.3

print('\n')

glosariusz = {
	'Boolean': 'True/False', 
	'Integer': '2', 
	'Float': '1.5', 
	'PEP8': 'Formotwanie', 
	'Tuple': 'Krotka'
	}


print(list(iter(glosariusz)))


for key,value in glosariusz.items():
    print(key + ' : ' + value)
    

for x in glosariusz.keys():
	print(x + ' : ' + glosariusz[x])
    
