import re

cpf = input("Digite seu CPF: ")
padrao = r"^\d{3}.\d{3}.\d{3}-\d{2}$"
valido = re.match(padrao, cpf)

if valido:

    validacao_digito1 = ((int(cpf[0]) * 10) + (int(cpf[1]) * 9) + (int(cpf[2]) * 8) + (int(cpf[4]) * 7) + (int(cpf[5]) * 6) + (int(cpf[6]) * 5) + (int(cpf[8]) * 4) + (int(cpf[9]) * 3) + (int(cpf[10]) * 2)) % 11
    validacao_digito2 = ((int(cpf[0]) * 11) + (int(cpf[1]) * 10) + (int(cpf[2]) * 9) + (int(cpf[4]) * 8) + (int(cpf[5]) * 7) + (int(cpf[6]) * 6) + (int(cpf[8]) * 5) + (int(cpf[9]) * 4) + (int(cpf[10]) * 3) + (int(cpf[12]) * 2)) % 11

    if validacao_digito1 >= 2:
        digito1 = 11 - validacao_digito1
    else:
        digito1 = 0

    if validacao_digito2 >= 2:
        digito2 = 11 - validacao_digito2
    else:
        digito2 = 0

    if int(cpf[12]) == digito1 and int(cpf[13]) == digito2:
        print("CPF valido")
    else:
        print("CPF Invalido")
else:
    print("Não escrito corretamente")