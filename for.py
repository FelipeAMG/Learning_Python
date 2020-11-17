"""Clase de for."""

names=('Abraham','Cesar','Daniel','Daniela','Diego','Edgar')

for name in names:
    print(f'Student: {name}')
else:
    print('No more names')


string = 'Felipe'

for char in string:
    if char != 'e':
        print(char)


numbers=[]

for number in range(0,21,2):
    numbers.append(number)

print(numbers)