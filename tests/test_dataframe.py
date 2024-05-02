import numpy as np
import pyjaguar as pj
import pytest

# Arrays para teste
a = np.array(["a", "b", "c"])
b = np.array(["c", "d", None])
c = np.random.rand(3)
d = np.array([True, False, True])
e = np.array([1, 2, 3])

# DataFrame para teste
df = pj.DataFrame({"a": a, "b": b, "c": c, "d": d, "e": e})


class TesteCriacaoDataFrame:

    @pytest.mark.parametrize("entrada", [
        ([1, 2, 3]),
        ({1: 5, "b": 10}),
        ({"a": np.array([1]), "b": 10}),
        ({"a": np.array([1]), "b": np.array([[1]])})
    ])
    def test_tipos_entrada_invalidos(self, entrada):
        # Testa se tipos de entrada inválidos levantam exceções
        with pytest.raises((TypeError, ValueError)):
            pj.DataFrame(entrada)

    def test_tipos_entrada_validos(self):
        # Testa a criação do DataFrame com tipos de entrada válidos.
        pj.DataFrame({"a": np.array([1]), "b": np.array([1])})

    @pytest.mark.parametrize("dados", [
        ({"a": np.array([1, 2]), "b": np.array([1])})
    ])
    def test_comprimento_array_invalido(self, dados):
        # Testa se um comprimento de array inválido levanta uma exceção.
        with pytest.raises(ValueError):
            pj.DataFrame(dados)

    def test_comprimento_array_valido(self):
        # Testa a criação do DataFrame com comprimento de array válido.
        pj.DataFrame({"a": np.array([1, 2]), "b": np.array([5, 10])})

    def test_unicode_para_object(self):
        # Testa a conversão de unicode para object.
        a_object = a.astype("O")
        assert np.array_equal(df._dados["a"], a_object)
        assert np.array_equal(df._dados["b"], b)
        assert np.array_equal(df._dados["c"], c)
        assert np.array_equal(df._dados["d"], d)
        assert np.array_equal(df._dados["e"], e)

    def test_numero_linhas(self):
        # Testa o número de linhas do DataFrame.
        assert len(df) == 3

    def test_colunas(self):
        # Testa as colunas do DataFrame.
        assert df.colunas == ["a", "b", "c", "d", "e"]

    @pytest.mark.parametrize("colunas, esperado_exception", [
        (5, TypeError),
        (["a", "b"], ValueError),
        ([1, 2, 3, 4, 5], TypeError),
        (["f", "f", "g", "h", "i"], ValueError),
        (["f", "g", "h", "i", "j"], None),
        (["a", "b", "c", "d", "e"], None)
    ])
    def test_nome_colunas(self, colunas, esperado_exception):
        # Testa a atribuição de nomes de colunas.
        if esperado_exception:
            with pytest.raises(esperado_exception):
                df.colunas = colunas
        else:
            df.colunas = colunas
            assert df.colunas == colunas
    
    def test_dimensao(self):
        # Testa as dimensões do DataFrame.
        assert df.dimensao == (3, 5)

    def test_para_array(self):
        # Testa a conversão do DataFrame para numpy.
        valores = np.column_stack((a, b, c, d, e))
        assert np.array_equal(df.para_array, valores)

    def test_tipos_dados(self):
        # Testa os tipos de dados das colunas do DataFrame.
        colunas_esperadas = np.array(["a", "b", "c", "d", "e"])
        tipos_esperados = np.array(["object", "object", "float64", "bool", "int64"])
        
        df_esperado = df.tipos_dados
        df_resposta = pj.DataFrame({"Coluna": colunas_esperadas, "Tipo": tipos_esperados})

        assert np.array_equal(df_esperado._dados["Coluna"], df_resposta._dados["Coluna"])
        assert np.array_equal(df_esperado._dados["Tipo"], df_resposta._dados["Tipo"])