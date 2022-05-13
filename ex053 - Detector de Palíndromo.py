txt=str(input('Digite uma frase: ')).strip().upper()
palavras= txt.split()
junto=''.join(palavras)
inverso=junto[::-1]
print(f"o inverso de {txt} é {inverso}!")

if junto==inverso or inverso==junto:
    print('Temos um Palíndromo')
else:
    print('NÃO temos um Palíndromo')

#def inverter(txt)
#return txt[::-1]