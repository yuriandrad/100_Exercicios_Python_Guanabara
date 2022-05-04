prod=float(input('Qual é o preço do produto? R$'))
desc=float(input('Qual a porcentagem de desconto? '))
vf0=prod*(desc/100)
vf=prod-vf0
print('O produto que valia R${:.2f}, com desconto de {}%, agora vale R${:.2f}'.format(prod, desc, vf))


