print('{:=^40}'.format(' LOJAS SALVATRUCHA '))
preco=float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opcao=int(input('Qual é a opção? '))
print('---------------------------')

if opcao==1:
    desconto=preco-(preco*0.10)
    print('Sua compra merece 10% de desconto!')
    print('De R${:.2f} caiu para R${:.2f}!'.format(preco,desconto))

elif opcao==2:
    desconto=preco-(preco*0.05)
    print('Sua compra merece 5% de desconto!')
    print('De R${:.2f} foi para {:.2f}!'.format(preco,desconto))

elif opcao==3:
    print('Parcelado em até 2x...')
    print('Preço comum de R${:.2f}'.format(preco))

elif opcao==4:
    parcelas = int(input('Quantas parcelas serão? '))
    juros=preco+(preco*0.20)
    valor=juros/parcelas
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parcelas,valor))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco,juros))

else:
    print('Número inválido!')


