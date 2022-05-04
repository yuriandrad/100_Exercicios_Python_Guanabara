sal=float(input('Qual é o salário do funcionário? R$'))
aum=sal+(sal*(15/100))
print('O salário que era R${:.2f}, com aumento de 15%, pulou para R${:.2f}'.format(sal, aum))
