# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços:

nome = str(input('Digite o nome: ')).strip().upper()
palavras = nome.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso = inverso + junto[letra]
print(junto, inverso)
if junto == inverso:
    print('A frase {} é igual a {} portanto é um Palindromo'.format(junto, inverso))
else:
    print('A frase {} não é gual a {}, portanto, não é um palindromo'.format(junto, inverso))
