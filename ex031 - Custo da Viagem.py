from time import sleep
viagem= float(input('Qual é a distância da sua viagem? '))
sleep(1)
if viagem<=200:
    curta = viagem * 0.50
    print('Você vai fazer uma viagem CURTA de {}KM'.format(viagem))
    print('Pagando um total de R${:.2f}'.format(curta))
else:
    longa = viagem * 0.45
    print('Você vai fazer uma viagem LONGA de {}KM'.format(viagem))
    print('Pagando um total de R${:.2f}'.format(longa))
