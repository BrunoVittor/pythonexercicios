# faça um programa que leia um ângulo quaqluer e mostre na tela o seu ceno cosseno e tangente desse angulo

from math import sin,cos,radians,tan
angulo = float(input('Digite o angulo: '))
sen = sin(radians(angulo))
print('O angulo de {} têm o seno de {:.2f}'.format(angulo, sen))
cos = cos(radians(angulo))
print('O cosseno de {} t~em o consseno de {:.2f}'.format(angulo, cos))
tan = tan(radians(angulo))
print('O ângulo de {} t~em a tangente de {:.2f}'.format(angulo, tan))