dias = int(input('Quantos dias alugados? '))
km = int(input('Quantos Km rodados? '))
por_dia = dias * 60
por_km = km * 0.15
total = por_dia + por_km

print(f'O total a pagar é de R${total:.2f}')