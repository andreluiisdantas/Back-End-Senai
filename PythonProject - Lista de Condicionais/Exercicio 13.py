temperatura = float(input("Digite a temperatura em graus Celsius: "))

if temperatura < 10:
    print("Frio")
elif temperatura <= 25:
    print("Aconchegante")
elif temperatura <= 40:
    print("Quente")
else:
    print("Muito quente")