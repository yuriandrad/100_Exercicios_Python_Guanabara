from random import randint
print('=-'*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*20)
cont=0
v=0
while True:
    computador = randint(0, 10)
    num=int(input('Diga um valor: '))
    pi=str(input('Par ou ímpar? [P/I] ')).upper().strip()[0]
    soma=num+computador
    resto= num % 2
    print('-'*20)
    print(f'Você jogou {num} e o computador jogou {computador}. Total de {soma}!')
    print('DEU PAR.' if soma%2==0 else 'DEU IMPAR.')
    print('-' * 20)
    if pi=='P':
        cont += 1
        if soma%2==0:
            v += 1
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            print('*'*20)
        else:
            print('Você PERDEU :P')
            break

    elif pi=='I':
        cont += 1
        if soma % 2 == 1:
            v += 1
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            print('*' * 20)
        else:
            print('Você PERDEU :P')
            break
print(f'GAME OVER! Você teve {cont} tentativas e {v} vitórias!!!')

