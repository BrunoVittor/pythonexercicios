# A Confederação Nacional de Natação precisa de um programa,
# que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER
'''from datetime import date

atual = date.today().year
ano = int(input('Digite o ano de nascimento do atleta: '))
idade = atual - ano
if idade <= 9:
    print('O atleta têm {} anos Categoria MIRIN !'.format(idade))
elif idade <= 14:
    print('O atleta têm {} anos Categoria INFANTIL !'.format(idade))
elif idade <= 19:
    print('O atleta têm {} anos Categoria JÙNIOR !'.format(idade))
elif idade <= 25:
    print('O atleta têm {} anos Categoria SÊNIOR !'.format(idade))
else:
    print('O atleta têm {} anos Categoria MASTER !'.format(idade))'''



# A Confederação Nacional de Natação precisa de um programa,
# que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER

from datetime import date

date = date.today().year

nascimento = int(input('Digite o ano de nscimento: '))
idade = date - nascimento
if idade <= 9:
    print('Mirin')
elif idade <= 14:
    print('Infantil')
elif idade <= 19:
    print('Júnior')
elif idade <= 25:
    print('Sênior')
else:
    print('Master')

