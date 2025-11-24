frase = input('Digite uma frase: ')

frase = frase.upper()

print(f"Na frase aparecem {frase.count('A')} vezes a letra A")
print(f"A letra A aparece pela primeira vez na posição {frase.find('A') + 1}")
print(f"A letra A aparece pela última vez na posição {frase.rfind('A')}")