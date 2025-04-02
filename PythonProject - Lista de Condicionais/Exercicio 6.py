nota = float(input("Digite a nota do aluno "))

if nota > 10:
    print("Nota invalida")
elif nota < 0:
    print("Nota invalida")
else:
    if nota >= 9:
        print("Nota: A")
    elif nota >= 7:
        print("Nota: B")
    elif nota >= 5:
        print("Nota: C")
    elif nota >= 3:
        print("Nota: D")
    else:
        print("Nota: E")