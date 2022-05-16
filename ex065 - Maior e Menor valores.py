flag=0
cont=0
soma=0
maior=0
menor=0
while flag==0:
    num=int(input('Digite um número: '))
    cont += 1
    soma += num
    if num>maior:
        maior=num
    resp=str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if resp=='N':
        flag +=1
print('Você digitou {} números e a média foi {:.2f}'.format(cont,soma/cont))
print(f'O maior valor foi {maior}!')


