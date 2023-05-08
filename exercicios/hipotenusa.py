import math
cp = float(input('Qual o tamanho do cateto oposto: '))
cd = float(input('Qual o tamanho do cateto adjacente: '))
hp = math.hypot(cd,cp)
print(f'A hipotenusa mede: {hp:.2f}')

