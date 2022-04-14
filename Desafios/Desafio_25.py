#Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome

nome = str(input('Digite o seu nome completo: ')).strip().upper()
silva = ('SILVA' in nome)
print('Seu nome tem Silva? {}'.format(silva))