#Analisador de textos

#nome = input('Digite seu nome: ')
#separar = nome.split()

#print(f'Seu nome com todas as letras maiúsculas fica: {nome.upper()}')
#print(f'Seu nome com todas as letras minúsculas fica: {nome.lower()}')
#print(f'Seu nome possui {len(nome)-nome.count(' ')}')
#print(f'Seu primeiro nome possui {len(nome.split()[0])}')

nome = str(input('Digite seu nome completo: ')).strip()
separa = nome.split()

print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é: {nome.upper()}')
print(f'Seu nome em minúsculas é: {nome.lower()}')
print(f"Seu nome tem ao todo {len(nome)-nome.count(' ')}")
print(f'Seu primeiro nome é {len(nome.split()[0])}')