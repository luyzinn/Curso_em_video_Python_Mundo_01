#Faça um algoritimo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.

sal = float(input("Qual o seu salário atual? R$ "))
nsal = sal + (sal * 0.15)
print("O seu salário atual é R$ {:.2f}. Com o novo aumento de 15%, voce receberá R$ {:.2f}".format(sal, nsal))