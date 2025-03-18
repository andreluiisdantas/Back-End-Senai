print("Plano cartesiano")

x1 = int(input("Digite o valor do ponto x1: "))
y1 = int(input("Digite o valor do ponto y1: "))
x2 = int(input("Digite o valor do ponto x2: "))
y2 = int(input("Digite o valor do ponto y2: "))

distancia = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

print(f'A distância é: {distancia}')