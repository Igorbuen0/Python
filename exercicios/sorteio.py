import random
import time
n1 = input('Digite um nome: ')
n2 = input('Digite outro nome: ')
n3 = input('Digite mais um nome: ')
n4 = input('Digite o ultimo nome: ')
lista = [n1, n2, n3, n4]
sort = random.choice(lista)


print('-------------------')
print('Sorteandooooo....')
print('-------------------')
time.sleep(3)
print(f'O aluno sorteado foi: <!--{sort}--!>')