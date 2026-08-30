def escolhaDeOperação(n1,n2,Operador):
    while True:
        operador= input("Escolha uma das operações:\n adição \n subtração \n multiplicação \n divisão\n exponenciação \n raidiciação\n divisão inteira\n porcentagem ou digite 0 para encerrar:").lower()
        if operador == "adição":
            Adição = calcula_soma(n1,n2)
        elif operador == "subtração":
            Subtração = calcula_subtração(n1,n2)
        elif operador == "multiplicação":
            Multiplicação = calcula_multiplicação(n1,n2)
        elif operador == "divisão":
            Divisão = calcula_divisão(n1,n2)
        elif operador == "exponenciação":
            Exponenciação = calcula_exponenciação(n1,n2)
        elif operador == "radiciação":
            Radiciação = calcula_radiciação(n1,n2)
        elif operador == "divisão inteira":
            DivisãoInteira = calcula_divisão_inteira(n1,n2)
        elif operador == "porcentagem":
            Porcentagem = calcula_porcentagem(n1,n2)
        elif operador == "0":
            print("Operação encerrada")
            break