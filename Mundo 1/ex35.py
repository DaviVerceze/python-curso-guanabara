#Analisando triângulo v1.0

primeiro = float(input('Primeiro seguimento: '))
segundo = float(input('Segundo seguimento: '))
terceiro = float(input('Terceiro seguimento: '))

if primeiro + segundo > terceiro and segundo + terceiro > primeiro and terceiro + primeiro > segundo:
    print('Este triângulo pode ser formado!')
else:
    print('Este triângulo não pode ser formado!')
