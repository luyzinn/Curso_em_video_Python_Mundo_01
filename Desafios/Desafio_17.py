#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. 
#Calcule e mostre o comprimento da hipotenusa.

from math import hypot

cateto_oposto = float(input('Digite o comprimento do Cateto Oposto: '))
cateto_adj = float(input('Digite o comprimento do Cateto Adjacente: '))
print('O seu cateto oposto é = {}\nO cateto adjacente é = {}\nA sua hipotenusa é = {:.2f}!'.format(cateto_oposto, cateto_adj, hypot(cateto_oposto, cateto_adj)))