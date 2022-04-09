#Crie um programa que leia quanto dineiro uma pessoa tem na carteira e mostre quantos doláres ela pode comprar
# Dolar hoje (09/04/22) = R$ 4,70

v = float(input("Quanto em real voce quer converter? R$"))
d = v / 4.70
print("O valor de {:.2f} reais é igual a {:.2f} dólares!".format(v,d))


