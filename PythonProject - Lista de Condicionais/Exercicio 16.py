num = int(input("Digite um número: "))

if num < 0:
    print("Não é possivel calcular a raiz quadrada de um número negativo")
elif num > 100:
    print("Número muito grande, reduza para um número menor que 100")
else:
    raiz = num ** 0.5
    print(f'A raiz quadrada do número é: {raiz:.2f}')