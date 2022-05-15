flag = 0

while flag == 0:
    sexo = str(input('Informe seu sexo [M/F]: ')).upper().strip()
    if sexo == 'M':
        flag += 1
    if sexo == 'F':
        flag += 1
    elif sexo != 'M' and 'F':
        print('Dados inválidos')
        flag == 0
print('-=' * 20)
print(f'Sexo "{sexo}" registrado com sucesso!')
