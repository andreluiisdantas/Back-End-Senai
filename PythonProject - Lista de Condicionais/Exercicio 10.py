ano = int(input("Digite o ano: "))

if ano % 4 == 0:
    print("Ano bissexto")
elif ano % 100 == 0 and 400:
    print("Ano Bisexxto")
else:
    print("Ano não é bissexto")