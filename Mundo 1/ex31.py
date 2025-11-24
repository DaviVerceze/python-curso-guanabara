#Custo da viagem

d = float(input('Digite a distância da sua viagem: '))
p = d * 0.5
l = d * 0.45

print(f'Você está prestes a começar uma viagem de {d}Km')

if d <= 200:
    print(f'O preço dessa passagem será de: R${p:.2f}')
else:
    print(f'O preço dessa passagem será de: R$ {l:.2f}')
