#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
#É necessário usar a conversao é preciso transformar de grau para radiano

from math import sin, cos, tan, radians

angulo = float(input('Digite o angulo que voce deseja: '))
print('O angulo digitado foi: {}\nSeu cosseno é {:.2f}\nSeu seno é {:.2f}\nSua tangente é {:.2f}.'.format(angulo,cos(radians(angulo)),sin(radians(angulo)),tan(radians(angulo))))