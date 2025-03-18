a = int(input("Digite o valor da variavel A "))
b = int(input("Digite o valor da variavel B "))

print(f'Valores:')
print(f'A - {a}')
print(f'B - {b}')


a, b = b, a

print(f'Valores invertidos:')
print(f'A - {a}')
print(f'B - {b}')
