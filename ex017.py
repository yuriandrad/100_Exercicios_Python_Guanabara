co=float(input('Comprimento do cateto oposto: '))
ca=float(input('Comprimento do cateto adjacente: '))
import math
hip= ((co**2) + (ca**2))
print('A hipotenusa mede {:.2f}'.format(math.sqrt(hip)))


