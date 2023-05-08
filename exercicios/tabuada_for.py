import time

n1 = int(input('Qual tabuada você quer ver: '))
n2 = 0
for tabu in range(1,11):
    tabu*n1
    print(8*'#')
    n2+=1
    print(f'{n1}x{n2}={tabu*n1}')