# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Qual o seu salário atual? '))
cores = {   'limpa':'\033[m',
            'vermelho em negrito':'\033[1;31m',
            'azul em negrito':'\033[1;34m' ,
            'amarelo em negrito':'\033[1;33m' ,
            'branco em negrito':'\033[1;30m',
            'roxo em negrito':'\033[1;35m',
            'verde em negrito':'\033[1;32m',
            'ciano em negrito':'\033[1;36m',
            'vermelho em negrito':'\033[1;31m',
            'azul em negrito':'\033[1;34m' ,
            'amarelo em negrito':'\033[1;33m' ,
            'branco em negrito':'\033[1;30m',
            'roxo em negrito':'\033[1;35m',
            'verde em negrito':'\033[1;32m',
            'ciano em negrito':'\033[1;36m',
            'vermelho sublinhado':'\033[4;31m',
            'azul sublinhado':'\033[4;34m',
            'amarelo sublinhado':'\033[4;33m',
            'branco sublinhado':'\033[4;30m',
            'roxo sublinhado':'\033[4;35m',
            'verde sublinhado':'\033[4;32m',
            'ciano sublinhado':'\033[4;36m'
        }
if salario < 1250:
    aumento = (salario * .15) + salario
    print('Seu novo salário atual é {:.2f} .. com aumento de 15% .. seu novo salário é {:.2f}'. format(salario, aumento))
else:
    aumento = (salario * .10) + salario
    print('Seu novo salário atual é {:.2f} .. {}com aumento de 10% {}.. seu novo salário é {:.2f}'. format(salario, cores['verde em negrito'], cores['limpa'], aumento))

