import numpy as np


def assert_igual_df(df1, df2):
    assert df1.colunas == df2.colunas

    for valores1, valores2 in zip(df1._dados.values(), df2._dados.values()):
        tipo = valores1.dtype.kind
        if tipo == "f":  
            np.testing.assert_allclose(valores1, valores2)
        else: 
            np.testing.assert_array_equal(valores1, valores2)