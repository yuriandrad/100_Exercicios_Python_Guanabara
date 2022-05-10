print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)
primeiro=int(input('Primeiro termo: '))
razao=int(input('Razao: '))
decimo= primeiro + (10-1) * razao
for c in range(primeiro, decimo + razao , razao):
    print(f"{c}", end=' → ')
print('ACABOU')
