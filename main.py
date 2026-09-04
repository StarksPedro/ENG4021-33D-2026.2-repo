def calcula_multiplicação(n1, n2):
	return n1 * n2

def calcula_divisão(n1, n2):
	return n1 / n2

def calcula_soma(x,y):
    return x+y

def calcula_porcentagem(x,y):
    return (x/100)*y

def escolhaDeOperação():
    while True:
        operador= input("Escolha uma das operações:\n adição \n subtração \n multiplicação \n divisão\n exponenciação \n raidiciação\n divisão inteira\n porcentagem\n ou\n digite 0 para encerrar:").lower()
        if operador == "0":
            print("Operação encerrada")
            break
        n1= float(input("Digite o primeiro número:"))
        n2= float(input("Digite o segundo número:")) 
        if operador == "adição":
            print("----------------")
            print("\n")
            print(calcula_soma(n1,n2))
            print("\n")
            print("----------------")
            
        elif operador == "subtração":
            print("----------------")
            print("\n")
            print(calcula_subtração(n1,n2))
            print("\n")
            print("----------------")
            
        elif operador == "multiplicação":
            print("----------------")
            print("\n")
            print(calcula_multiplicação(n1,n2))
            print("\n")
            print("----------------")
            
        elif operador == "divisão":
          if n2 == 0:
            print("Não existe divisão por 0")
                  return 
            print("----------------")
            print("\n")
            print(calcula_divisão(n1,n2))
            print("\n")
            print("----------------")
            
        elif operador == "exponenciação":
            print("----------------")
            print("\n")
            print(calcula_exponenciação(n1,n2))
            print("\n")
            print("----------------")
            
        elif operador == "radiciação":
            print("----------------")
            print("\n")
            print(calcula_radiciação(n1,n2))
            print("\n")
            print("----------------")
            
        elif operador == "divisao inteira":
            print("----------------")
            print("\n")
            print(calcula_divisão_inteira(n1,n2))
            print("\n")
            print("----------------")
            
        elif operador == "porcentagem":
            print("----------------")
            print("\n")
            print(calcula_porcentagem(n1,n2))
            print("\n")
            print("----------------")
          

escolhaDeOperação()
