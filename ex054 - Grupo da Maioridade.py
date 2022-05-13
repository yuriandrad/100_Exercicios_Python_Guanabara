from datetime import date
totmaior=0
totmenor=0
for pess in range(1,8):
    z=int(input(f'Em que ano a {pess}ª pessoa nasceu? '))
    idade=date.today().year - z
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print(f'No total foram {totmaior} MAIORES de idade e {totmenor} MENORES de idade!')

