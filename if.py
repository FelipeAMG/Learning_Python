"""Clase de If/Else/Elif."""

my_number = int(input('Ingresa un numero entero'))

if 5>my_number:
    print(f'5 es mayor que {my_number}')
elif 5==my_number:
    print(f'{my_number} es igual 5')
else:
    print(f'5 es menor que {my_number}')
