print('-='*15)
print('Analisador de Triângulos')
print('-='*15)
a=float(input('Primeiro segmento: '))
b=float(input('Segundo segmento: '))
c=float(input('Terceiro segmento: '))
if a<b+c and b<a+c and c<b+a:
    print('\033[1;32mOs segmentos acima PODEM formar um triângulo:', end='')
    if a==b==c:
        print('EQUILÁTERO!')
    if a!=b!=c!=a:
        print('ESCALENO!')
    if a==b!=c or b==a!=c or c==a!=b:
        print('ISÓSCELES')
else:
    print('\033[1;31mOs segmentos acima NÃO PODEM formar um triângulo!')
