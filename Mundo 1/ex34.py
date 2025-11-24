salario = float(input('Digite seu salário: ')) 
aumento = 0


if salario > 1250.0:
    aumento = salario * 0.10
    print(f'O salário de R${salario:.2f} agora passa para {salario + aumento:.2f}')
elif salario <= 1250.0:
    aumento = salario * 0.15
    print(f'O salário de R${salario:.2f} agora passa para R${salario + aumento:.2f}')