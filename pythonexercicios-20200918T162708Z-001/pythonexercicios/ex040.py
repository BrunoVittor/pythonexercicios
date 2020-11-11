# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO


n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
média = (n1 + n2) / 2
if média <= 5.0:
    print('A sua média foi de {} você foi \033[31mREPROVADO\033[m !!!!!'.format(média))
elif média == 5.5 or média < 7:
    print('Sua média foi de {:.1f} você está de \033[33mRECUPERACÃO\033[m !!!!!!!'.format(média))
elif média >= 7.0:
    print('A sua média foi {} você foi \033[32mAPROVADO\033[m !!!!!!'.format(média))
