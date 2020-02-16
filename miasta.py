#6.11

cities = {
	'Bydgoszcz': {
		'Kraj': 'Polska',
		'Populacja': 350000,
		'Fakt': 'Brda',
		},
	'Gdansk': {
		'Kraj': 'Polska',
		'Populacja': 450000,
		'Fakt': 'Morze',
		},
	'Poznan': {
		'Kraj': 'Polska',
		'Populacja': 400000,
		'Fakt': 'Warta'
		}
	}
	


for city, city_info in cities.items():
	print(city, city_info)
print('\t')
	


#6.12
for k, v in cities.items():
	print('Miasto: ' + k)
	for d, f in v.items():
		print(d,'-', f)
	print('\t')
	
