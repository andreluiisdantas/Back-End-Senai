idade = int(input("Digite sua idade: "))

if idade < 16:
    print("Não eleitor")
elif idade >= 18 and idade < 71:
    print("Voto obrigatório")
else:
    print("Voto não obrigatório")