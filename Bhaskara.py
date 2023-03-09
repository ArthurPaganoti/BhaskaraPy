from math import sqrt
valorA = int(input('Digite o valor de A:'))
valorB = int(input('Digite o valor de B:'))
valorC = int(input('Digite o valor de C:'))
delta = (valorB**2)-(4*valorA*valorC)

if delta < 0:
    print('Está equação não possui resultados reais \n' )

elif delta == 0:
    print('Está equação possui apenas um resultado real, ou possui dois resultados iguais \n')

elif delta > 0:
    print('Está equação possui dois resultados distintos reais \n')

valorX1 = -valorB + (sqrt(delta)) / (2*valorA)
valorX2 = -valorB - (sqrt(delta)) / (2*valorA)

print('O valor do X1 é:{:.1f} \nO valor do X2 é :{:.1f}'.format(valorX1,valorX2))