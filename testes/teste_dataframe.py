import numpy as np
from numpy.testing import assert_array_equal
import pytest

import pyjaguar as pj

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

    def teste_tipos_entrada(self):
        with pytest.raises(TypeError):
            # Lista como entrada
            pj.DataFrame([1, 2, 3])

        with pytest.raises(TypeError):
            # Dicionário com chaves não string
            pj.DataFrame({1: 5, "b": 10})

        with pytest.raises(TypeError):
            # Valor não-Array no dicionário
            pj.DataFrame({"a": np.array([1]), "b": 10})

        with pytest.raises(ValueError):
            # Array multidimensional
            pj.DataFrame({"a": np.array([1]), "b": np.array([[1]])})

        # Construção correta. Sem erro.
        pj.DataFrame({"a": np.array([1]), "b": np.array([1])})
    
    def teste_comprimento_array(self):
        # Arrays de comprimentos diferentes
        with pytest.raises(ValueError):
            pj.DataFrame({"a": np.array([1, 2]), "b": np.array([1])})
        
        # Construção correta. Sem erro.                    
        pj.DataFrame({"a": np.array([1, 2]), "b": np.array([5, 10])})
    
    def teste_unicode_para_object(self):
        a_object = a.astype("O") 

        # Verificando se "a" foi convertido corretamente
        assert_array_equal(df._dados["a"], a_object)

        # Verificando "b"
        assert_array_equal(df._dados["b"], b)

         # Verificando "c"
        assert_array_equal(df._dados["c"], c)

         # Verificando "d"
        assert_array_equal(df._dados["d"], d)

         # Verificando "e"
        assert_array_equal(df._dados["e"], e)
    
    def teste_nlinhas(self):
        assert len(df) == 3