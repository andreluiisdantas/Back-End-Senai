import re

padrao = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"

senha = input("Digite a senha: ")

if re.match(padrao, senha):
    print("Senha valida")
else:
    print("Senha invalida")

    if len(senha) < 8:
        print("A senha precisa ter pelo menos 8 digitos")
    elif not re.search(r"[A-Z]", senha):
        print("A senha não possui letras maiusculas")
    elif not re.search(r"[a-z]", senha):
        print("A senha não possui letras minusculas")
    elif not re.search(r"\d", senha):
        print("A senha não possui números")
    elif not re.search(r"[@$!%*?&]", senha):
        print("A senha deve conter caracteres especiais")
    else:
        print("A senha não atendeu nenhum parâmetro")