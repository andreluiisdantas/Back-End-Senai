num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if num1 > num2 and num2 > num3:
    print("A lista esta em ordem decrescente")
elif num2 > num1 and num3 > num2:
    print("A lista esta em ordem crescente")
else:
    print("A lista esta em uma ordem invalida")