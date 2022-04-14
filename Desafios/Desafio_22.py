''' Desafio: 
Crie um programa que leia o nome completo de uma pessoa e mostre:
– O nome com todas as letras maiúsculas e minúsculas.
– Quantas letras ao todo (sem considerar espaços).
– Quantas letras tem o primeiro nome. '''

nome = str(input('Digite seu nome completo: '))
nome_upper = nome.upper()
nome_lower = nome.lower()
nome_strip = nome.strip()
#nome_join = join.(nome)
nome_len = len(nome)-nome.count(' ')
nome_slip = nome.split()
nome_len2 = len(nome_slip[0])
print('Analisando seu nome ...')
print('')
print('Olá {}!\nSeu nome em maiúsculo é {}\nSeu nome em minúsculo é {}\nSeu nome tem o total de {} letras\nSeu primeiro nome é {} e tem {} letras!'.format(nome, nome_upper, nome_lower,nome_len,nome_slip[0],nome_len2))