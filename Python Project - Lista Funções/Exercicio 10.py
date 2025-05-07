def palindromos(palavra):
    palavra = palavra.upper().replace(" ", "")

    if palavra == palavra[::-1]:
        print("Pálindromo")
    else:
        print("Não é pálindromo")


palindromos("Ana Ana")
palindromos("1DSTB-SENAI")
palindromos("Subi no Onibus")
