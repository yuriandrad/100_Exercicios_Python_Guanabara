print('+----------------------+')
print('Índice de Massa Corporal')
print('+----------------------+')
peso=int(input('Digite seu peso (Kg): '))
altura=float(input('Digite sua altura (m): '))
imc= peso / (altura ** 2)
print("=======================================")
print('Com um IMC de {:.1f} foi constatado: '.format(imc))
from time import sleep
sleep(1)
if imc<18.5:
    print('ABAIXO DO PESO!')
elif 18.5 <= imc < 25:
    print('PESO IDEAL!')
elif 25 <= imc < 30:
    print('SOBREPESO!')
elif 30 <= imc < 40:
    print('OBESIDADE!')
else:
    print('\033[1;31mOBESIDADE MÓRBIDA, CUIDADO!!!\033[m')

