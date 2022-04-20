#Nessa aula, vamos aprender como utilizar estruturas condicionais simples e compostas nos seus programas em Python.
#Condicionais if e else

#Exemplo 01

tempo = int(input('Quantos anos seu carro tem? '))
if tempo >=3:
    print('Seu carro é velho')
else: 
    print('Seu carro é novo')

#Exemplo 02

nome = str(input('Escreva seu nome: '))
if nome == 'Luiz':
    print('Belo nome')
else:
    print('Voce tem um nome tao normal nao é?')
print('Obrigado pela sua colaboraçao')

#Exemplo 03

print('Vamos ao cálculo da sua média')
nota_1 = float(input('Digite sua primeira nota: '))
nota_2 = float(input('Digite sua segunda nota: '))
soma_nota = nota_1 + nota_2
media_nota = (nota_1 + nota_2) / 2

print('A soma das suas notas é {:.2f} e a média é {:.2f}.. entao:'.format(soma_nota, media_nota))

if media_nota <= 6:
    print('Voce esta reprovado .. estude mais um pouco!')
else:
    print('Parabéns!! Voce esta aprovado!!')

