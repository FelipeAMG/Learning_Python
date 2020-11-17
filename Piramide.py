"""Piramide"""

number=int(input('Ingrese un numero'))

for x in range(number + 1):
	print(x*str(x))
for x in range(number - 1,0,-1):
	print(x*str(x))