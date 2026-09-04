def calcula_exponenciação(n1,n2):
	return n1**n2

def calcula_subtração(n1,n2):
	return n1-n2

def divisão_inteira(n1,n2):
	return n1//n2

def calcula_resto(n1,n2):
    return n1 % n2

def calcula_radiciação(n1, n2):
     if n1 < 0 and (int(n2) % 2 == 1 or int(n2) % 2 == -1):
            n1 = n1 * -1
            result = n1**(1/n2)
            result = result * -1
     else:
         result = n1 ** (1/n2)
    return result

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
        operador= input("Escolha uma das operações:\n adição \n subtração \n multiplicação \n divisão\n exponenciação \n raidiciação\n divisão inteira\n porcentagem\n resto\n ou\n digite 0 para encerrar:").lower()
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
            if n2==0:
                print("não existe divisão por 0)
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
            if n2==0:
                print("não existe raiz de indice 0)
                      return
            elif n1<0 and n2%2 == 0:
                print("Não existe raiz paz de numero negativo)
                return
                
            print("----------------")
            print("\n")
            print(ccalcula_radiciação(n1,n2))
            print("\n")
            print("----------------")
            
        elif operador == "divisao inteira":
            if n2==0:
            print("Não existe divisão por 0)
            return
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

        elif operador == "resto":
            if n2== 0:
               print("Não existe resto de divisão por 0")
               return
            print("----------------")
            print("\n")
            print(calcula_resto(n1,n2))
            print("\n")
            print("----------------")
          

escolhaDeOperação()

