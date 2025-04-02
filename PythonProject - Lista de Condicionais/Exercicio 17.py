import re

data = input("Digite uma data: ")
padrao = r"^\d{2}/\d{2}/\d{4}$"
valido = re.match(padrao, data)

if valido:
    dia, mes, ano = data.split('/')
    data_invertida = f'{ano}-{mes}-{dia}'

    if (int(ano) % 4 == 0 and int(ano) % 100 != 0) or (int(ano) % 400 == 0):
        if int(mes) == 2:
            if int(dia) >= 1 or int(dia) <= 29:
                print(f'A data formatada é: {data_invertida}')
            else:
                print("Dia invalida")
        elif int(mes) == 1 or int(mes) == 3 or int(mes) == 5 or int(mes) == 7 or int(mes) == 8 or int(mes) == 10 or int(
                mes) == 12:
            if int(dia) >= 1 or int(dia) <= 31:
                print(f'A data formatada é: {data_invertida}')
            else:
                print("Dia invalida")
        elif int(mes) == 4 or int(mes) == 6 or int(mes) == 9 or int(mes) == 11:
            if int(dia) >= 1 or int(dia) <= 30:
                print(f'A data formatada é: {data_invertida}')
            else:
                print("Dia invalida")
        else:
            print("Mês invalido")
    else:
        if int(mes) == 2:
            if int(dia) >= 1 or int(dia) <= 2:
                print(f'A data formatada é: {data_invertida}')
            else:
                print("Dia invalida")
        elif int(mes) == 1 or int(mes) == 3 or int(mes) == 5 or int(mes) == 7 or int(mes) == 8 or int(mes) == 10 or int(
                mes) == 12:
            if int(dia) >= 1 or int(dia) <= 31:
                print(f'A data formatada é: {data_invertida}')
            else:
                print("Dia invalida")
        elif int(mes) == 4 or int(mes) == 6 or int(mes) == 9 or int(mes) == 11:
            if int(dia) >= 1 or int(dia) <= 30:
                print(f'A data formatada é: {data_invertida}')
            else:
                print("Dia invalida")
        else:
            print("Mês invalido")
else:
    print("Escrito incorretamente")