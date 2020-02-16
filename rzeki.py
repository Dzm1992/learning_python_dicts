rzeki = {'Wisła': 'Polska', 'Nil': 'Egipt', 'Amazonka': 'Brazylia'}

for rzeka, kraj in rzeki.items():
	print(rzeka + " przepływa przez " + kraj + ".")

print("\n")

for rzeka in rzeki.keys():
	print(rzeka)
	
print("\n")

for kraj in rzeki.values():
	print(kraj)
