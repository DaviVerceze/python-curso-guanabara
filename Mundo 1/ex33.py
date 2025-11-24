primeiro = int(input('Primeiro Valor: '))
segundo = int(input('Segundo Valor: '))
terceiro = int(input('Terceiro Valor: '))

if primeiro > segundo and primeiro > terceiro:
    print(f"O maior valor digitado foi {primeiro}")
elif segundo > primeiro and segundo > terceiro:
    print(f"O maior valor digitado foi {segundo}")
else:
    print(f"O maior valor digitado foi {terceiro}")


if primeiro < segundo and primeiro < terceiro:
    print(f"O menor valor digitado foi {primeiro}")
elif segundo < primeiro and segundo < terceiro:
    print(f"O menor valor digitado foi {segundo}")
else:
    print(f"O menor valor digitado foi {terceiro}")