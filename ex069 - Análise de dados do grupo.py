cont1 = cont2 = cont3 = 0
while True:
    print('-='*10)
    print('CADASTRE UMA PESSOA')
    print('-='*10)
    idade=int(input('Idade: '))
    if idade>=18:
        cont1 += 1
    sexo=str(input('Sexo: [M/F] ')).upper().strip()
    if sexo=='M':
        cont2 += 1
    if sexo=='F' and idade<20:
        cont3 += 1
    print('-'*20)
    continuar=str(input('Quer continuar? [S/N] ')).upper().strip()
    if continuar=='N':
        break
print('-' * 20)
print(f'{cont1} pessoas tem mais de 18 anos.')
print(f'{cont2} homens cadastrados.')
print(f'{cont3} mulheres com menos de 20 anos.')
#while not in



