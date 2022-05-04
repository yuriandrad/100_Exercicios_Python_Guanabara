casa=int(input('Valor da casa: R$'))
salario=int(input('Salário do comprador: R$'))
anos=int(input('Quantos anos de financiamento? '))
parcela= casa / (anos*12)
minimo=salario * (30/100)
print('Para pagar uma casa de \033[4;32mR${:.2f}\033[m, em {} anos...'.format(casa,anos))
from time import sleep
sleep(1)
print('A prestação será de \033[4;32mR${:.2f}\033[m por mês!'.format(parcela))
if parcela <= minimo:
    print('\033[1;32mPassou dos 30%, PODE COMPRAR!!!\033[m')
else:
    print('\033[1;31mNão passou dos 30%, NÃO PODE COMPRAR!!!\033[m')

