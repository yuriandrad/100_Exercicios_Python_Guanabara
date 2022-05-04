n1=float(input('Digite a primeira nota: '))
n2=float(input('Digite a segunda nota: '))
media=(n1+n2)/2
if media>=7:
    print('Aluno \033[1;32maprovado!')
if media<7:
    print('Aluno \033[1;31mreprovado!')
if media==10:
    print('\033[1;34mO aluno é foda pra caralho!')