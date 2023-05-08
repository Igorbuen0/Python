class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

print(f'{bcolors.FAIL}CONVERSOR DE NÚMERO DECIMAIS EM BIN/OCT/HEX{bcolors.RESET}')


numero = int(input(f'{bcolors.OK}Digite um número inteiro: {bcolors.RESET}'))
menu = int(input(f'{bcolors.OK}Escolha qual será sua base de conversão: \n 1-binário \n 2-octal \n 3-hexadecimal \n aguardando: {bcolors.RESET}'))
bi = 1
ot = 2
hx = 3

if menu == 1:
    print(f'{bcolors.FAIL}O número {numero} em binario é:{bcolors.RESET}',bin(numero))
elif menu == 2:
    print(f'{bcolors.FAIL}O número {numero} em binario é:{bcolors.RESET}',oct(numero))
elif menu == 3:
    print(f'{bcolors.FAIL}O número {numero} em binario é:{bcolors.RESET}',hex(numero))
