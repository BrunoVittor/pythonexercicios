# comando .is

n = input('Digite algo: ')
print('O tipo primitivo é: ', type(n))
print('{} só tem espaços? {}'.format(n, n.isspace()))
print('{} é numérico? {}'.format(n, n.isnumeric()))
print('{} é alphabético? {}'.format(n, n.isalpha()))
print('{} é alphanumérico? {}'.format(n, n.isalnum()))
print('{} é ascii? {}'.format(n, n.isascii(),))
print('{} é decimal? {}'.format(n, n.isdecimal()))
print('{} é digitável? {}'.format(n, n.isdigit()))
print('{} é minuscúlo? {}'.format(n, n.islower()))
print('{} é maiscúlo? {}'.format(n, n.isupper()))