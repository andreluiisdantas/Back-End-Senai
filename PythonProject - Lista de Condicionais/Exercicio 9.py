valor = float(input("Digite o valor da compra: R$ "))

if valor < 100:
    valor_final = valor - (valor * 0.05)
    print("O desconto será de 5%")
    print(f'Valor atual: R$ {valor_final:.2f}')
elif valor <= 500:
    valor_final = valor - (valor * 0.1)
    print("O desconto será de 10%")
    print(f'Valor atual: R$ {valor_final:.2f}')
else:
    valor_final = valor - (valor * 0.15)
    print("O desconto será de 15%")
    print(f'Valor atual: R$ {valor_final:.2f}')