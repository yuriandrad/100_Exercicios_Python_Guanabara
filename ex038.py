num1=int(input('Digite o primeiro valor: '))
num2=int(input('Digite o segundo valor: '))
from time import sleep
sleep(1)
if num1>num2:
    print('{} é maior que {}'.format(num1,num2))
elif num2>num1:
    print('{} é maior que {}'.format(num2,num1))
else:
    print('Os valores são iguais!')
