import numpy as np
import pyjaguar as pj
import pytest

pytestmark = pytest.mark.filterwarnings("ignore")

# Arrays para teste
a = np.array(["a", "b", "c"])
b = np.array(["c", "d", None])
c = np.random.rand(3)
d = np.array([True, False, True])
e = np.array([1, 2, 3])

# DataFrame para teste
df = pj.DataFrame({"a": a, "b": b, "c": c, "d": d, "e": e})

class TesteCriacaoDataFrame:

    def teste_tipos_de_entrada(self):
        with pytest.raises(TypeError):
            # Lista como entrada
            pj.DataFrame([1, 2, 3])

        with pytest.raises(TypeError):
            # Dicionário com chaves não string
            pj.DataFrame({1: 5, 'b': 10})

        with pytest.raises(TypeError):
            # Valor não-Array no dicionário
            pj.DataFrame({'a': np.array([1]), 'b': 10})

        with pytest.raises(ValueError):
            # Array multidimensional
            pj.DataFrame({'a': np.array([1]), 'b': np.array([[1]])})

        # Construção correta. Sem erro.
        pj.DataFrame({'a': np.array([1]), 'b': np.array([1])})