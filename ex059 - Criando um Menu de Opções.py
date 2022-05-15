n1=int(input('\033[1;32mPrimeiro valor: \033[m'))
n2=int(input('\033[1;32mSegundo valor: \033[m'))
flag = 0
while flag == 0:
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    opcao=int(input('>>>>> Qual é a sua opção? '))
    if opcao == 1:
        print('\033[1;32mO resultado de {} + {} é: {}\033[m'.format(n1,n2,n1+n2))
        print('-' * 20)
        flag += 0
    elif opcao == 2:
        print('\033[1;32mO resultado de {} x {} é: {}\033[m'.format(n1, n2, n1 * n2))
        print('-' * 20)
        flag += 0
    elif opcao == 3:
        if n1>n2:
            print(f'\033[1;32m{n1} é maior que {n2}!\033[m')
        elif n2>n1:
            print(f'\033[1;32m{n2} é maior que {n1}!\033[m')
        elif n1==n2:
            print('	\033[1;31mOs valores são iguais!\033[m')
        print('-' * 20)
        flag += 0
    elif opcao == 4:
        n1=int(input('\033[1;91mDigite seu primeiro NOVO valor: \033[m'))
        n2=int(input('\033[1;91mDigite seu segundo NOVO valor: \033[m'))
        flag += 0
    elif opcao == 5:
        print('\033[1;31mFinalizando o programa...\033[m')
        from time import sleep
        sleep (2)
        print('\033[1;33mObrigado por usar nosso programa!!! :)\033[m')
        print('\033[1;32mTenha um ótimo dia.\033[m')
        flag += 1
    else:
        print('\033[1;31mDigite um número válido.\033[m')
        flag += 0


