#from math import factorial
#n1=(int(input('Digite um valor: ')))
#print(factorial(n1))

from math import factorial
n=int(input('Digite um número para calcular seu fatorial: '))
c=n
f = 1
print(f'Calculando {n}! = ',end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c>1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
