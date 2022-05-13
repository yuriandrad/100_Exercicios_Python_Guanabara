from datetime import date
ano = date.today().year
print('--------------------------------------------------')
nasc=int(input('Informe seu ano de nascimento: '))
idade= ano-nasc
print('Quem nasceu em {}, tem {} anos em {}.'.format(nasc,idade,ano))

if idade == 18:
    print('\033[1;33mVocê tem que se alistar IMEDIATAMENTE!\033[m')

elif idade<18:
    saldo = 18 - idade
    print('\033[1;32mAinda falta(m) {} ano(s) para o alistamento!\033[m'.format(saldo))
    anoo= ano + saldo
    print('Seu alistamento será em {}'.format(anoo))

elif idade>18:
    saldo = idade - 18
    print('\033[1;31mVocê já deveria ter se alistado há {} anos!\033[m'.format(saldo))
    anoo= ano - saldo
    print('Seu alistamento foi em {}'.format(anoo))
