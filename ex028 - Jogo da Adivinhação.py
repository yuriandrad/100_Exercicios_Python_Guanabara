from random import randint
from time import sleep
computador = randint(0,5)
print('=*='*10)
print('Tente adivinhar o número que irei pensar!')
print('=*=' * 10)
jogador=int(input('Qual seu palpite? '))
print('PROCESSANDO...')
sleep(3) #tempo em segundos que vai esperar
sleep(2)
if jogador == computador:
    print('PARABÉNS VOCÊ ACERTOU!')
else:
    print('GANHEI, pensei no número {} e não em {} '.format(computador,jogador))


