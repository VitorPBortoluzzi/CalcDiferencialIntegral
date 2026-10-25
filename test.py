import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

import CalculadoraDerivada_rulePotencia as polinomio
from CalculadoraDerivada_rulePotencia import ler_input, formatar_numero, formatar_polinomio, main


def avaliar(p, x):
    """Valor do polinômio p (índice = expoente) em x."""
    return sum(c * x**i for i, c in enumerate(p))


def rodar(funcao, entradas):
    """Executa a função com entradas simuladas e devolve o texto impresso."""
    saida = io.StringIO()
    with patch("builtins.input", side_effect=entradas), redirect_stdout(saida):
        funcao()
    return saida.getvalue()


class TestDerivada(unittest.TestCase):
    def test_exemplo_do_enunciado(self):
        saida = rodar(polinomio.derivada, ["2", "3", "2", "12"])
        self.assertIn("Vetor: [12.0, 2.0, 3.0]", saida)
        self.assertIn("f(x)  = 3x^2 + 2x + 12", saida)
        self.assertIn("f'(x) = 6x + 2", saida)

    def test_grau_tres_com_negativos(self):
        saida = rodar(polinomio.derivada, ["3", "-2", "5", "-1", "-7"])
        self.assertIn("f(x)  = -2x^3 + 5x^2 - x - 7", saida)
        self.assertIn("f'(x) = -6x^2 + 10x - 1", saida)

    def test_constante_vira_zero(self):
        saida = rodar(polinomio.derivada, ["0", "5"])
        self.assertIn("f(x)  = 5", saida)
        self.assertIn("f'(x) = 0", saida)

    def test_grau_um_negativo(self):
        saida = rodar(polinomio.derivada, ["1", "-1", "0"])
        self.assertIn("f(x)  = -x", saida)
        self.assertIn("f'(x) = -1", saida)

    def test_decimais_com_virgula(self):
        saida = rodar(polinomio.derivada, ["2", "2,5", "0", "1"])
        self.assertIn("f(x)  = 2.5x^2 + 1", saida)
        self.assertIn("f'(x) = 5x", saida)

    def test_coeficiente_lider_zero(self):
        saida = rodar(polinomio.derivada, ["2", "0", "0", "0"])
        self.assertIn("f(x)  = 0", saida)
        self.assertIn("f'(x) = 0", saida)

    def test_grau_negativo_mostra_erro(self):
        saida = rodar(polinomio.derivada, ["-1"])
        self.assertIn("Erro", saida)
        self.assertNotIn("f'(x)", saida)

    def test_entrada_invalida_repete_pergunta(self):
        saida = rodar(polinomio.derivada, ["abc", "1", "2", "3"])
        self.assertIn("Entrada inválida", saida)
        self.assertIn("f(x)  = 2x + 3", saida)
        self.assertIn("f'(x) = 2", saida)

    def test_vetor_derivada_e_definicao_de_limite(self):
        # Captura os vetores v e d passados para formatar_polinomio
        with patch.object(polinomio, "formatar_polinomio",
                          wraps=polinomio.formatar_polinomio) as espiao:
            rodar(polinomio.derivada, ["3", "-2", "5", "-1", "-7"])

        v = espiao.call_args_list[0].args[0]
        d = espiao.call_args_list[1].args[0]

        self.assertEqual(v, [-7, -1, 5, -2])
        self.assertEqual(d, [-1, 10, -6])

        # f'(x) ≈ (f(x+h) -