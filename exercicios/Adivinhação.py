import random
import time


azul = '\033[94m'
verde = '\033[92m'
amarelo = '\033[93m'
vermelho = '\033[91m'
fim = '\033[0m'

famarelo = '\033[1;43m'
fverde = '\033[1;42m'
fvermelho = '\033[1;41m'
fazul = '\033[1;44m'

num = random.randint(0,5)
print('Vou pensar em um número de 0 a 5. Tente adivinhar....')
print(f'{fvermelho}{azul}______________________________________________________{fim}')

pc = int(input('Que número eu pensei: '))
while pc < 0 or pc > 5:
    print('O número precisa ser entre 0 e 5!!')
    print(f'{fvermelho}{azul}______________________________________________________{fim}')
    pc = int(input('Que número eu pensei: '))
    print(f'{fvermelho}{azul}______________________________________________________{fim}')
if pc == num:
    print(f'{amarelo}Sorteando!!!{fim}')
    print(f'{fvermelho}{azul}______________________________________________________{fim}')
    time.sleep(2)
    print(f'{famarelo}{verde}Parabéns!!! o número era {num}...!{fim}')

else:
    print(f'{fazul}{amarelo}Sorteandoooo!!!{fim}')
    print(f'{fvermelho}{azul}______________________________________________________{fim}')
    time.sleep(2)
    print(f'{fverde}{vermelho}Errouuuuuuuu!{fim}')
