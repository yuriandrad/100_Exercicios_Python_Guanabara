media=0
totmenor=0
nome_velho=''
maioridadehomem=0
nomevelho=''
for c in range(1,5):
    print(f'---- {c}ª PESSOA ----')
    nome=str(input('Nome: ')).strip()
    idade=int(input('Idade: '))
    sexo=str(input('Sexo [M/F]: ')).upper()
    if c == 1 and sexo=='M':
        maioridadehomem=idade
        nomevelho=nome
    if sexo=='M' and idade > maioridadehomem:
        maioridadehomem=idade
        nomevelho=nome
    if sexo=='F' and idade<20:
        totmenor += 1

    media+=idade

print('')
print(f'A média de idade do grupo é {media/4} anos')
print(f'Ao todo são {totmenor} mulheres com menos de 20 anos')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}!')
