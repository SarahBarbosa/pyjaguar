import numpy as np
import pytest
import pyjaguar as pj

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
        with pytest.raises((TypeError, ValueError)):
            pj.DataFrame(entrada)

    def test_tipos_entrada_validos(self):
        pj.DataFrame({"a": np.array([1]), "b": np.array([1])})

    @pytest.mark.parametrize("dados", [
        ({"a": np.array([1, 2]), "b": np.array([1])})
    ])

    def test_comprimento_array_invalido(self, dados):
        with pytest.raises(ValueError):
            pj.DataFrame(dados)

    def test_comprimento_array_valido(self):
        pj.DataFrame({"a": np.array([1, 2]), "b": np.array([5, 10])})

    def test_unicode_para_object(self):
        a_object = a.astype("O")
        assert np.array_equal(df._dados["a"], a_object)
        assert np.array_equal(df._dados["b"], b)
        assert np.array_equal(df._dados["c"], c)
        assert np.array_equal(df._dados["d"], d)
        assert np.array_equal(df._dados["e"], e)

    def test_numero_linhas(self):
        assert len(df) == 3
