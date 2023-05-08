casa = float(input('Qual o valor da casa que você quer comprar: '))
while casa < 10000:
    print('O valor precisa ser maior que 10mil.')
    casa =  float(input('Qual o valor da casa que você quer comprar: '))

salario = float(input('Qual seu salário: '))
tempo = int(input('Em quantos anos voce vai pagar: '))
prestação = casa/(tempo * 12)

print(f'A prestação vai sair R${prestação:.2f} por mes')
porcento_limite = salario * 0.30

if prestação > porcento_limite:
    print('Emprestimo negado, salário incompativel com a compra!')
else:
    print('Compra efetuada com sucesso!')





