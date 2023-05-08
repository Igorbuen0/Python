
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
crtl = 0
while crtl == 0:
    soma = 1
    mult = 2
    maior = 3
    nova = 4
    sair = 5
    print('=+=+=+=+=+=+=+=+=+=+=+=+=+=++=+=++=+=++=+=+')
    menu = int(input('\nEscolha sua opção no menu\n[1]somar\n[2]multiplicar\n[3]maior que\n[4]nova opção\n[5]sair\nQual sua opção: '))
    if menu == 1:
        print('=+=+=+=+=+=+=+=+=+=+=+=+=+=++=+=++=+=++=+=+')
        print(f'O resultado é: {num1+num2}')
    if menu == 2:
        print('=+=+=+=+=+=+=+=+=+=+=+=+=+=++=+=++=+=++=+=+')
        print(f'O resultado é: {num1*num2}')

    if menu == 3:
        max_val = max(num1,num2)
        print('=+=+=+=+=+=+=+=+=+=+=+=+=+=++=+=++=+=++=+=+')
        print(f'O número maior é: {max_val} ')

    if menu == 4:
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite outro número: '))
        print('=+=+=+=+=+=+=+=+=+=+=+=+=+=++=+=++=+=++=+=+')
    if menu == 5:
        break
    if menu > 5:
        print('Erro! Digite as opções informadas!')
        print('=+=+=+=+=+=+=+=+=+=+=+=+=+=++=+=++=+=++=+=+')
print('Fim do programa!')

