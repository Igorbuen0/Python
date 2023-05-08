preç = float(input('Qual valor do produto: '))

desconto = preç * 5 / 100
valor = preç - desconto


print(f'O produto custa {preç}, mas na promoção com desconto de {desconto:.2f} vai custar {valor:.2f}')