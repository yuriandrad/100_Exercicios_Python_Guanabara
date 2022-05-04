print('-='*15)
print('Analisador de Triângulos')
print('-='*15)
a=float(input('Primeiro segmento: '))
b=float(input('Segundo segmento: '))
c=float(input('Terceiro segmento: '))
if a<b+c and b<a+c and c<b+a:
    print('Os segmentos acima PODEM formar um triângulo!')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo!')



