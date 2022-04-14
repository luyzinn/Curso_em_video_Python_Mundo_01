#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = str(input('Digite o nome de uma cidade: ')).strip().lower()
santo_cidade = ('santo' in cidade)
print(santo_cidade)
