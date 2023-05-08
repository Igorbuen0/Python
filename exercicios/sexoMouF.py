sexo = input('Digite M ou F: ').upper()
masc = 'M'
fem = 'F'

while sexo != 'M' and sexo != 'F':
    sexo = input('Apenas M ou F:  ').upper()
if sexo == masc:
    print('Voce é masculino')
if sexo == fem:
    print('Voce é feminino')
