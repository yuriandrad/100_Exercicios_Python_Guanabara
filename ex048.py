z = 0
cont= 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont= cont + 1
        z= z+c
print(f'A soma de todos os {cont} valores solicitados foi de {z}.')