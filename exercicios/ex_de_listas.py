import os
print('----Lista de compras----')
lista = []
while True:
    escolha = input('Selecione uma opção\n[i]nserir [a]pagar [l]istar [s]air: ')

    if escolha.lower() == 'i' or escolha.lower() == 'inserir':
        inserir = input('valor: ')
        valor_ins = lista.append(inserir)
        print(f'Valor "{inserir}" foi inserido')


    elif escolha.lower() == 'l' or escolha.lower() == 'listar':
        for item, index in enumerate(lista):
            print(item, index)


    elif escolha.lower() == 'a' or escolha.lower() == 'apagar':
        for item, index in enumerate(lista):
            print(item, index)
        try:
            apagar = input('Digite o índice que você quer apagar: ')
            apagar = int(apagar)
            valor_del = lista.pop(apagar)
            print(f'Valor "{valor_del}" foi deletado')
        except:
            print('Valor inválido')
            continue
    elif escolha.lower() == 's' or escolha.lower() == 'sair':
        print('Fim do programa.')
        break
