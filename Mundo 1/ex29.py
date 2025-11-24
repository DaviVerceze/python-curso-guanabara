#Radar eletrônico

v = int(input('Digite a velocidade que o carro estava: '))
multa = (v - 80)


if v <= 80:
    print('Tenha um bom dia! Dirija com segurança!')
else:
    print(f'Você foi multado! O limite era de 80Km/h, você deve pagar uma multa de R${multa * 7},00')