n1=float(input('Digite a primeira nota: '))
n2=float(input('Digite a segunda nota: '))
media= (n1+n2) / 2
if media<5.0:
    print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1,n2,media))
    print('\033[1;31mO aluno está REPROVADO!')

elif media>=5.0 and media<=6.9:
    print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1,n2,media))
    print('\033[1;33mO aluno está em RECUPERAÇÃO!')

elif media>=7.0:
    print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1,n2,media))
    print('\033[1;32mO aluno está APROVADO!')
