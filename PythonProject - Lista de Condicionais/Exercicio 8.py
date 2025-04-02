lado1 = float(input("Informe a primeira medida:"))
lado2 = float(input("Informe a segunda medida:"))
lado3 = float(input("Informe a terceira medida:"))

if (lado1 + lado2 < lado3) or (lado1 + lado3 < lado2) or (lado2 + lado3 < lado1):
    print("Nao é um triângulo")
elif (lado1 == lado2) and (lado1 == lado3):
    print("Triângulo Equilátero")
elif (lado1 == lado2) or (lado1 == lado3) or (lado2 == lado3):
    print("Triângulo Isósceles")
else:
    print("Triângulo Escaleno")