nome = str(input('Digite seu nome completo: ')).strip()
print()
print('Analisando seu nome...')
print('.')
print('.')
print('.')
print('Seu nome em maiúsculo é: '),print(nome.upper())
print('----------------------')
print('Seu nome em minúsculo é: '),print((nome.lower()))
print('----------------------')
print('Seu nome possui ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('----------------------')
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e possui {} letras'.format(separa[0], len(separa[0])))




