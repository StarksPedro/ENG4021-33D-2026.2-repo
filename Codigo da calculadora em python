import math

def operacaoInvalida(n1, n2, Op):
    if Op == '/' and n2 == 0:
        print("Não é possível dividir por zero, digite outro número ou escolha outra operação")
        return True
    elif Op == 'V' and n1 < 0:
        print("Não é possível calcular a raiz quadrada de um número negativo, digite outro número ou escolha outra operação")
        return True
    elif Op == 'R' and n1 < 0 and int(n2) % 2 == 0:
        print("Não é possível calcular a raiz de indice par de um número negativo, digite outro número ou escolha outra operação")
        return True
    elif Op == 'R' and n1 >= 0 and n2 == 0:
        print("Não é possível calcular a raiz de indice zero, digite outro número ou escolha outra operação")
        return True
    return False


def decideConta(n1, n2, Op):
    if Op == '+':
        result = n1 + n2
        print(f"O resultado da operação é: {result:.2f}")
    elif Op == '-':
        result = n1 - n2
        print(f"O resultado da operação é: {result:.2f}")
    elif Op == '*':
        result = n1 * n2
        print(f"O resultado da operação é: {result:.2f}")
    elif Op == '/':
        result = n1 / n2
        print(f"O resultado da operação é: {result:.2f}")
    elif Op == '**':
        result = n1**n2
        print(f"O resultado da operação é: {result:.2f}")
    elif Op == 'V':
        result = math.sqrt(n1)
        print(f"O resultado da operação é: {result:.2f}")
    elif Op == 'R':
        if n1 < 0 and (int(n2) % 2 == 1 or int(n2) % 2 == -1):
            n1 = n1 * -1
            result = n1**(1/n2)
            result = result * -1
            print(f"O resultado da operação é: {result:.2f}")
        else:
            result = n1**(1/n2)
            print(f"O resultado da operação é: {result:.2f}")
    else:
        print("Operador inválido, digite outro operador")


def NumeroOperador():
    n1 = float(input("Digite um número:"))
    Op = input("Digite um operador matemático (+, -, *, /, **, V(sqrt), R(sqrtIndiceN):").strip()
    n2 = float(input("Digite um número:"))
    OpI= operacaoInvalida(n1, n2, Op)
    DcdC= decideConta(n1, n2, Op)

    if OpI is not True:
        DcdC


NumeroOperador()