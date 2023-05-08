"""
# :s - Texto (strings)
# :d - inteiros (int)
# :f - numeros de ponto flutuante (float)
# :. (número) f - quantidade de casas decimais (float)
# : (caractere) (> ou < ou ^) (quantidade) (tipo -s, d ou f)

# > - esquerda
# < - direita
# ^ - centro
"""

nome = input('Qual seu nome: ')
while nome.isspace() == True:
    nome = input('Não deixe em branco: ')
else:
    print(f'Olá {nome.title()}')