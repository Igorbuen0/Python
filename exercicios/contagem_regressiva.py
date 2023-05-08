import time
vermelho = '\033[91m'
fim = '\033[0m'

for c in range (5, 0, -1):
    print(c)
    c -=1
    time.sleep(1)
print(f'{vermelho}BUMMMMMMMMMmmmmmmmmmm! \n -----Feliz Ano Novo-----{fim}')
