import re

data = input("Digite uma data: ")
padrao = r"^\d{2}/\d{2}/\d{4}$"
valido = re.match(padrao, data)

if valido:
    dia, mes, ano = data.split('/')
    data_invertida = f'{ano}-{mes}-{dia}'
    print(f'A data formatada é: {data_invertida}')
else:
    print("Escrito incorretamente")