from random import randint
from time import sleep
computador=randint(0,10)
print('=*=' * 20)
print('Sou seu computador!')
print("Acabei de pensar em um número entre 0 e 10, tente adivinhar!")
print('=*=' * 20)
tentativa=0
flag = 0
while flag == 0:
    jogador = int(input('Qual é o seu palpite? '))
    if computador > jogador:
        print('MAIS... Tente mais uma vez.')
        tentativa += 1
        flag += 0
    elif computador < jogador:
        print('MENOS... Tente mais uma vez.')
        tentativa += 1
        flag += 0
    elif jogador == computador:
        flag += 1
        tentativa += 1
print('\033[1;92mParabéns!!!')
print('Contando suas tentativas...')
sleep(1)
print('')
print(f'\033[1;92mVocê acertou com {tentativa} tentativas!')

