# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

print('Gerador de PA')
print('=' * 30)
primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0 :
    total = total + mais
    while cont <= total:
        print('{} > '.format(termo), end='')
        termo = termo + razão
        cont = cont + 1
    print('Pausa')
    mais = int(input('Quantermos você quer mostrar a mais ? : '))
print('O total de termos exibido foi {}'.format(total))
