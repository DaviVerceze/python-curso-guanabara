#Reajuste salarial

salario = float(input('Qual o salário do funcionário? R$'))
aumento = (salario * 0.15)
final = (salario + aumento)

print(f'Um funcionário que ganhava R${salario}, com 15% de aumento, passa a ganhar R${final:.2f}')