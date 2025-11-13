from math import hypot

cateto_oposto = float(input('Digite o comprimento do cateto oposto: '))
cateto_adjacente = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = hypot(cateto_oposto, cateto_adjacente)

print(f'A hipotenusa do triângulo retângulo com cateto oposto {cateto_oposto} e cateto adjacente {cateto_adjacente}, é {hipotenusa:.2f}')
