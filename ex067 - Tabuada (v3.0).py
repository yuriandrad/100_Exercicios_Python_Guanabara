while True:
    num= int(input('Digite um número para ver sua tabuada: '))
    if num<0:
        break
    print('--'*20)
    for c in range(1,11):
        print(f'{num} x {c} = {num*c}')
    print('--' * 20)
print('==============================================')
print('Obrigado por usar esse programa, volte sempre!')