flag=0
cont=0
contt=0
while flag == 0:
    num=(int(input('Digite um número [999 para parar]: ')))
    contt += 1
    cont += num
    if num==999:
        flag += 1
        cont -= 999
        contt -= 1
print(f'Você digitou {contt} números e sua soma foi {cont}.')

