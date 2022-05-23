tot1=tot2=cont=0
menor=0
barato=''
print('-'*15)
print('LOJA SUPER BARATÃO')
print('-'*15)
while True:
    nome=str(input('Nome do Produto: '))
    preco=float(input('Preço: R$'))
    cont += 1
    tot1 += preco
    if preco>1000:
        tot2 += 1
    continuar=' '
    if cont == 1:
        menor=preco
        barato=nome
    else:
        if preco<menor:
            menor=preco
            barato=nome
    while continuar not in 'SN':
        continuar=str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar=='N':
        break
print('----------FIM DO PROGRAMA----------')
print(f'R${tot1:.2f} foi o total gasto na compra.')
print(f'{tot2} produtos acima de mil reais.')
print(f'O produto mais barato foi {barato}, custando {menor:.2f}.')

