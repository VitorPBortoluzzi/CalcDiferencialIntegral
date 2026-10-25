# Derivada de polinômio
# Nome: <seu nome>
# Data: <data>
#
# O polinômio fica guardado num vetor, e a posição de cada número
# é o expoente do x:
#   3x^2 + 2x + 12  ->  v = [12, 2, 3]
#                 posição:   0   1  2
#
# Pra derivar eu uso a regra do tombo: (a * x^n)' = n * a * x^(n-1)


def ler_input(mensagem, tipo=float):
    # fica perguntando até o usuário digitar um número de verdade
    # troco a vírgula por ponto pra aceitar 2,5 também
    while True:
        try:
            return tipo(input(mensagem).replace(",", "."))
        except ValueError:
            print("Entrada inválida. Digite um número válido.")


def derivada():
    grau = ler_input("Digite o grau do polinomio: ", int)

    if grau < 0:
        print("Erro: o grau do polinomio não pode ser negativo.")
        return

    v = []

    # o usuário digita do maior expoente pro menor, mas o vetor
    # precisa ficar com a posição = expoente, então insiro sempre no começo
    for i in range(grau, -1, -1):
        coeficiente = ler_input(f"Coeficiente de x^{i}: ", float)
        v.insert(0, coeficiente)

    # aqui é a derivada em si
    # começo do 1 porque a constante (posição 0) vira zero e some
    # cada coeficiente é multiplicado pelo próprio expoente
    # ex: v = [12, 2, 3] -> d = [1*2, 2*3] = [2, 6]
    d = []
    for i in range(1, len(v)):
        d.append(i * v[i])

    # se era só uma constante, não sobra nada na lista, então a derivada é 0
    if not d:
        d = [0]

    print("Vetor:", [formatar_numero(c) for c in v])
    print("f(x)  =", formatar_polinomio(v))
    print("f'(x) =", formatar_polinomio(d))


def formatar_numero(n):
    # os coeficientes são float, então 3 viraria 3.0
    # essa função tira o .0 e deixa 2.5 como está
    if n == int(n):
        return str(int(n))
    return str(round(n, 4))


def formatar_polinomio(p):
    # transforma o vetor em texto, tipo "3x^2 + 2x + 12"
    termos = []

    # vai do maior expoente pro menor, que é como a gente escreve
    for i in range(len(p) - 1, -1, -1):
        coeficiente = p[i]

        # termo com coeficiente 0 não aparece
        if coeficiente == 0:
            continue

        # uso o valor absoluto porque o sinal eu coloco depois
        c = abs(coeficiente)
        c_str = formatar_numero(c)

        if i == 0:
            termo = c_str
        elif i == 1:
            # x^1 se escreve só x, e 1x vira x
            termo = "x" if c == 1 else f"{c_str}x"
        else:
            termo = f"x^{i}" if c == 1 else f"{c_str}x^{i}"

        # o primeiro termo só ganha "-" se for negativo
        # os outros entram com " + " ou " - " na frente
        if not termos:
            if coeficiente < 0:
                termo = "-" + termo
        else:
            sinal = " - " if coeficiente < 0 else " + "
            termo = sinal + termo

        termos.append(termo)

    # se todos eram zero, o polinômio é 0
    return "".join(termos) if termos else "0"


def menu():
    print("\n======Calculadora de Derivada de Polinomios======")
    print("\t 1 - Calcular derivada de um polinômio")
    print("\t-1 - Sair")


def main():
    opcao = 0

    # repete o menu até digitar -1
    while opcao != -1:
        menu()
        opcao = ler_input("Escolha uma opção: ", int)

        # match/case é o "switch" do Python (precisa da versão 3.10 ou mais)
        match opcao:
            case 1:
                derivada()
            case -1:
                print("Encerrando o programa.")
            case _:  # qualquer outra coisa (o "default")
                print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()