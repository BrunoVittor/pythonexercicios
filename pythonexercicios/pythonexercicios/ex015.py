# km percorridos e dias pelos quais foi alugado, preço a pagar , carro custa 60 reais o dia , e 0,15 o km rodado

'''dia = int(input('Por quantos dias foi alugado: '))
km = float(input('Quando km foram rodados: '))
res = (dia * 60) + (km * 0.15)
print('Se passaram {} dias \n foram percorridos {} km \n O valor total a pagar é de R${}'.format(dia, km, res))'''

'''dia = int(input('Quantidad de dias: '))
km = float(input('kilometros percorridos: '))
res = (dia * 60) + (km * 0.15)
print(f'O aluguel foi de {dia} e foram rodads {km}km, o valor foi de {res}')'''





print('-='*10)
print("Bruno's rent a car")
print('-='*10)
print('''TABELA DE PREÇOS 
        
R$ 60,00 por dia
R$ 0,15 por kilometro rodado ''')
dia = int(input('Dias utilizados: '))
km = float(input('Kilometros utilizados: '))
res = (dia * 60) + (km * 0.15)
print(f'O valor final foi de R${res}')