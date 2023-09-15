# Metodologia Given -- When -- Then
# "Dado uma situação, quando tal ação acontece, então resulta em algo"
import pytest
from pytest import mark
from codigo.bytebank import Funcionario


class TestClass:

    def test_property_nome_deve_retornar_o_atributo_nome_do_objeto(self):
        # Given
        nome = "Jorge"
        resultado_esperado = "Jorge"

        # When
        funcionario = Funcionario(nome, "12/03/2004", 0)
        resultado = funcionario.nome

        # Then
        assert resultado == resultado_esperado

    def test_quando_idade_recebe_16_01_2004_deve_retornar_o_valor_19(self):

        # Given -- "Contexto"
        entrada = "16/01/2004"
        esperado = 19

        # When -- "Ação"
        funcionario = Funcionario("Nome Teste", entrada, 1000)
        resultado = funcionario.idade()

        # Then -- "Então acontece"
        assert resultado == esperado

    def test_quando_o_metodo_sobrenome_recebe_Lucas_Machado_Carvalho_deve_retornar_Carvalho(self):

        # Given
        entrada = "Lucas Machado Carvalho"
        saida_esperada = "Carvalho"

        # When
        funcionario = Funcionario(entrada, "01/01/2000", 1000)
        resultado_execucao = funcionario.sobrenome()

        # Then
        assert saida_esperada == resultado_execucao

    def test_decressimo_salario_se_diretor_recebe_mais_de_100000_deve_retornar_menos_10_porcento(self):

        # Given
        entrada_salario = 100000
        nome_diretor = "Paulo Bragança"
        saida_esperada = entrada_salario - entrada_salario * 0.1

        # When
        funcionario_test = Funcionario(nome_diretor, "09/08/2000", entrada_salario)
        funcionario_test.decressimo_salarial_diretores()
        resultado = funcionario_test.salario

        # Then
        assert resultado == saida_esperada

    @mark.calcular_bonus
    def test_quando_salario_1000_calcular_bonus_deve_retornar_100(self):

        # Given
        entrada_salario = 1000
        saida_esperada = 100

        # When
        funcionario_test = Funcionario("Teste", "01/01/2001", entrada_salario)
        resultado = funcionario_test.calcular_bonus()

        # Then
        assert resultado == saida_esperada

    @mark.calcular_bonus
    def test_calcular_bonus_quando_usuario_nao_satisfaz_as_condicoes_deve_resultar_em_Exception(self):
        with pytest.raises(Exception): # Fica implicito que haverá um Exception como resultado
            # Given
            entrada_salario = 1000000

            # When
            funcionario_test = Funcionario("Teste", "01/01/2000", entrada_salario)
            resultado = funcionario_test.calcular_bonus()

            # Then
            assert resultado
