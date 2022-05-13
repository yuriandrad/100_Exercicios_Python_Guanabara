from datetime import date
ano = date.today().year
print('--------------------------------------------------')
nasc=int(input('Ano de Nascimento: '))
idade=ano-nasc
print('O atleta tem {} anos'.format(idade))

if 0< idade <=9:
    print('Classificação: MIRIM')

elif 9< idade <=14:
    print('Classificação: INFANTIL')

elif 14< idade <=19:
    print('Classificação: JÚNIOR')

elif 19< idade <=25:
    print('Classificação: SÊNIOR')

elif idade>25:
    print('Classificação: MASTER')
