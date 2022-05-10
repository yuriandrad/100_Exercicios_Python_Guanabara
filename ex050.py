soma=0
cont=0
for c in range(1,7):
    num=int(input('Digite o {} valor: '.format(c)))
    if num%2 == 0:
        #Esse mais/igual significa tipo: soma = soma + num
        soma += num
        cont += 1
print(f'Você informou {cont} números PARES e a soma foi {soma}')

