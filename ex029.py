carro=float(input('Qual a velocidade atual do carro? '))
multa=(carro-80) *7
if carro<=80:
    print('Tenha um bom dia, dirija com responsabilidade!')
else:
    print('LEVOU MULTA! PASSOU DOS 80km!')
    print('Sua multa foi de R${:.2f}.'.format(multa))


