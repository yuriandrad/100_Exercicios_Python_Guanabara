nome=str(input('Qual é o seu nome completo? ')).strip().upper()
print('---------------------------')
print('A letra A aparece {} vezes na frase'.format(nome.count('A')))
print('A primeira letra A apareceu na posição {}'.format(nome.find('A')+1))
print('A última letra A apareceu na posição {}'.format(nome.rfind('A')+1))