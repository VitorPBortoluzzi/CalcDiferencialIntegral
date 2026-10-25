def ler_input(mensagem, tipo=float):
    while True:
        try:
            return tipo(input(mensagem).replace(",","."))
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

def derivada():
    grau = ler_input("Digite o grau do polinomio: ", int)

    if grau < 0:
        print("Erro: o grau do polinomio não pode ser negativo.")
        return

    v = []

    for i in range(grau, -1, -1):
        coeficiente = ler_input(f"Coeficiente de x^{i}: ", float)
        v.insert(0, coeficiente)

    d = []

    for i in range(1, len(v)):
        d.append(i * v[i])

    if not d:
        d = [0]

    print("Vetor:", v)
    print("f(x)  =", formatar_polinomio(v))
    print("f'(x) =", formatar_polinomio(d))


def formatar_numero(n):
    if n == int(n):
        return str(int(n))
    return str(round(n,4))

def formatar_polinomio(p):
    termos = []

    # Percorre os coeficiente do maior para o menor expoente;
    for i in range(len(p) -1 , -1, -1):
        coeficiente = p[i]

        # Ignora os termos cujo coeficiente é zero.
        if coeficiente == 0:
            continue

        c = abs(coeficiente)
        c_str = formatar_numero(c)

        if i == 0:
            termo = c_str

        elif i == 1:
            termo = "x" if c == 1 else f"{c_str}x"

        else:
            termo = f"x^{i}" if c == 1 else f"{c_str}x^{i}"

        if not termos:
            if coeficiente < 0:
                termo = "-" + termo

        else:
            sinal = " - " if coeficiente < 0 else " + "
            termo = sinal + termo

        termos.append(termo)

    return "".join(termos) if termos else "0"

def menu():
    print("\n======Calculadora de Derivada de Polinomios======")
    print("\t 1 - Calcular derivada de um polinômio")
    print("\t-1 - Sair")
        
def main():
    opcao = 0

    while opcao != -1:
        menu()
        opcao = ler_input("Escolha uma opção: ", int)

        match opcao:
            case 1:
                derivada()
            case -1:
                print("Encerrando o programa.")
            case _:
                print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()