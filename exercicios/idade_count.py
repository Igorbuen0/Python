maior = 0
menor = 0

for p in range (1,7):

    ano = int(input(f'Em que ano a {p}ª pessoa nasceu? '))
    calc_idade = 2022 - ano
    if calc_idade < 18:
        menor += 1
    if calc_idade > 18:
        maior += 1

print(f'Ao todo tivemos {menor} pessoas menores de idade e {maior} maiores')