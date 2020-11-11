# km percorridos e dias pelos quais foi alugado, preço a pagar , carro custa 60 reais o dia , e 0,15 o km rodado

dia = int(input('Por quantos dias foi alugado: '))
km = float(input('Quando km foram rodados: '))
res = (dia * 60) + (km * 0.15)
print('Se passaram {} dias \n foram percorridos {} km \n O valor total a pagar é de R${}'.format(dia, km, res))
