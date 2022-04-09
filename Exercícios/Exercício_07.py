n1 = float(input ('Qual a primeira nota do aluno: '))
n2 = float(input ('Qual a segunda nota do aluno: '))
media = (n1 + n2) / 2
#É preciso lembrar do parentese, devido a ordem de precedência
print('A soma da primeira nota {}, com a segunda nota {} é igual a {}. A média é {:.2f}' .format(n1, n2, (n1+n2), media))
