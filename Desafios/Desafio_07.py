#Desenvolva um prorama que leia as duas notas de um aluno, calcule e mostre a sua média:

n1 = float(input("Digite a 1ª nota: "))
n2 = float(input("Digite a 2ª nota: "))
s = n1+n2
m = s/2
print("A soma da 1ª com a 2ª nota do aluno é {}. Com isso a média é {}!".format(s,m))