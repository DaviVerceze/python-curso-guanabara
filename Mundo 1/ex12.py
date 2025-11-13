preço = float(input('Qual o preço do produto? R$'))
desconto = (preço * (0.05))
final = preço - desconto

print(f'O produto que custava R${preço:.2f}, na promoção com desconto de 5% vai custar R${final:.2f}')
