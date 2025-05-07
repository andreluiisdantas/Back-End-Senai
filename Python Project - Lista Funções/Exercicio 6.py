def desconto(valor):
    valor_final = valor - (valor * 0.1)
    return valor_final

print(f'Produto 1: R$ {desconto(50):.2f}')
print(f'Produto 2: R$ {desconto(120):.2f}')
print(f'Produto 3: R$ {desconto(200):.2f}')