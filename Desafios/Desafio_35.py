# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print('=-' * 20)
print('      ANALISADOR DE TRIÂNGULOS     ')
print('=-' * 20)

lado_1 = float(input('Digite o primeiro lado do triângulo: '))
lado_2 = float(input('Digite o segundo lado do triângulo: '))
lado_3 = float(input('Digite o terceiro lado do triângulo: '))

cond_1 = (int(lado_2 - lado_3) < lado_1 < (lado_2 + lado_3)) == True
cond_2 = (int(lado_1 - lado_2) < lado_3 < (lado_1 + lado_2)) == True
cond_3 = (int(lado_1 - lado_3) < lado_2 < (lado_1 + lado_3)) == True

if cond_1 == cond_2 == cond_3:
    print('')
    print('Você pode formar um triângulo!')
else:
    print('')
    print('Você não pode formar um triângulo!')